import json
import os
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI

# Load ENV Vars
_ = load_dotenv(find_dotenv())

# Update KAGGLE_CONFIG_DIR with absolute path
os.environ["KAGGLE_CONFIG_DIR"] = str(Path(os.getenv("KAGGLE_CONFIG_DIR")).absolute())
print(os.environ["KAGGLE_CONFIG_DIR"])

app = FastAPI()


@app.post("/fetch_data")
async def fetch_data() -> dict:
    import kaggle

    source_dataset = "kaggle/meta-kaggle"
    source_file_name = "Users.csv"
    download_path = "/tmp/"
    download_file_path = f"{download_path}/{source_file_name}.zip"
    # {source_dataset.lower().replace("/", "_")}_{source_file_name.lower()}

    kaggle.api.authenticate()
    kaggle.api.dataset_download_file(
        dataset=source_dataset,
        file_name=source_file_name,
        path=download_path,
    )

    with ZipFile(download_file_path) as zf:
        for file in zf.namelist():
            if not file.endswith(".csv"):  # optional filtering by filetype
                continue
            with zf.open(file) as f:
                df = pd.read_csv(f)

    return {"data": json.dumps(df.to_json())}
