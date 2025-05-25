URL_BASE = "https://pivarski-princeton.s3.us-east-1.amazonaws.com/us-election-analysis/"


async def download(filename, base=URL_BASE):
    import pyodide.http

    response = await pyodide.http.pyfetch(
        f"{base}{filename}", method="GET", cache="no-store", priority="high"
    )
    return await response.memoryview()


async def json_zip(filename, base=URL_BASE):
    import io
    import json
    import zipfile

    subfilename = ".".join(filename.split("/")[-1].split(".")[:-1])
    with zipfile.ZipFile(io.BytesIO(await download(filename, base))) as zf:
        with zf.open(subfilename) as file:
            return json.load(file)



async def geojson_zip(filename, base=URL_BASE):
    import geopandas as gpd
    import io
    import zipfile

    subfilename = ".".join(filename.split("/")[-1].split(".")[:-1])
    with zipfile.ZipFile(io.BytesIO(await download(filename, base))) as zf:
        with zf.open(subfilename) as file:
            return gpd.read_file(file)


async def parquet(filename, base=URL_BASE):
    from tqdm import tqdm
    import geopandas as gpd
    import json
    import pandas as pd
    import pyarrow as pa
    import pyarrow.parquet as pq
    import shapely

    file = pq.ParquetFile(pa.BufferReader(await download(filename, base)))

    crsid = json.loads(file.schema.to_arrow_schema().metadata[b"geo"])["columns"][
        "geometry"
    ]["crs"]["id"]
    parts = []
    for row_group in tqdm(range(file.metadata.num_row_groups)):
        table = file.read_row_group(row_group)

        parts.append(
            gpd.GeoDataFrame(
                {name: table[name] for name in file.schema.names if name != "geometry"},
                geometry=[
                    shapely.from_wkb(x.as_buffer().to_pybytes())
                    for x in table["geometry"]
                ],
                crs=f"{crsid['authority']}:{crsid['code']}",
            )
        )

    return pd.concat(parts)


async def csv_zip(filename, base=URL_BASE):
    import io
    import pandas as pd
    import zipfile

    subfilename = ".".join(filename.split("/")[-1].split(".")[:-1])
    with zipfile.ZipFile(io.BytesIO(await download(filename))) as zf:
        with zf.open(subfilename) as file:
            return pd.read_csv(file, low_memory=False)
