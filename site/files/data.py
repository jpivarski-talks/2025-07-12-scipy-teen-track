URL_BASE = "https://pivarski-princeton.s3.us-east-1.amazonaws.com/us-election-analysis/"

async def download(filename, base=URL_BASE):
    import pyodide.http

    response = await pyodide.http.pyfetch(
        f"{base}{filename}", method="GET", cache="no-store", priority="high"
    )
    return await response.memoryview()
