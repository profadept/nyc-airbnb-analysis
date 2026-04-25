"""
download_data.py
Run with: uv run python scripts/download_data.py
Requires: ~/.kaggle/kaggle.json
"""

from pathlib import Path
import kaggle

DATASET = "dgomonov/new-york-city-airbnb-open-data"
DEST = Path("data")

if __name__ == "__main__":
    if not DATASET:
        raise ValueError(
            "DATASET is empty, open scripts/download_data.py and set it before running"
        )
    DEST.mkdir(parents=True, exist_ok=True)
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(DATASET, path=DEST, unzip=True)
    print(f"→ {DEST}")
