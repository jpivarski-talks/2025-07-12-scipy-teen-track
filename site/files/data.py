from collections import defaultdict
import json
import pyodide.http
import zipfile

from tqdm import tqdm
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import shapely.geometry
import shapely.ops

URL_BASE = "https://pivarski-princeton.s3.us-east-1.amazonaws.com/us-election-analysis/"

async def download(filename, base=URL_BASE):
    response = await pyodide.http.pyfetch(
        f"{base}{filename}", method="GET", cache="no-store", priority="high"
    )
    return await response.memoryview()
