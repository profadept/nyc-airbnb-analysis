# NYC Airbnb Market Analysis

This project analyzes the key factors that drive prices across NYC 2019 Airbnb listings, 
examining whether location, room type, or host behaviour is the dominant
price signal. The dataset covers 48,895 listings spread across five boroughs,
collected in 2019 and sourced from Kaggle's NYC Airbnb Open Data. The notebook
walks through data cleaning, exploratory analysis, and three focused questions
that each challenge assumptions about how the short-term rental market actually works.

## Key Findings

- **Location alone does not determine price.** Staten Island, despite having the
fewest listings of any borough, commands a higher median price than the Bronx;
volume and price move independently across the NYC market.

- **Room type is the strongest price driver.** Entire homes/apartments carry a median
price of USD 160, sitting USD 115 above shared rooms at USD 45 across every borough without
exception. Room type is a more reliable price signal than location.

- **More listings means less engagement.** Hosts managing larger portfolios generate
fewer reviews per listing. The individual attention that drives guest engagement
does not scale with listing count.

## Project Structure

```
nyc-airbnb-analysis/
├── data/                          # Raw and processed data files (gitignored)
├── figures/                       # Generated charts (gitignored)
├── notebooks/
│   └── NYC_Airbnb_EDA.ipynb       # Main analysis notebook
├── scripts/
│   └── download_data.py           # Kaggle dataset downloader
├── pyproject.toml                 # Project dependencies and metadata
├── README.md
└── uv.lock                        # Locked dependency versions
```

## Setup

Requires [uv](https://docs.astral.sh/uv/). Clone the repo and sync dependencies:

```bash
git clone git@github.com:profadept/nyc-airbnb-analysis.git
cd nyc-airbnb-analysis
uv sync
```

## Dataset

Data sourced from [Kaggle — NYC Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).

Two ways to get it:

**Option 1 — Manual download**
Create a `data/` folder in the project root, download and unzip from the Kaggle 
link above, then place `AB_NYC_2019.csv` inside it.

**Option 2 — Download script**
Place your Kaggle credentials at `~/.kaggle/kaggle.json`, then run:

```bash
uv run python scripts/download_data.py
```

Then launch the notebook:

```bash
uv run jupyter lab
```

## Tech Stack
- Python 3.14
- pandas, NumPy, seaborn, matplotlib
- Jupyter Lab
- uv for dependency management


## License

MIT License — project code only. Dataset subject to Kaggle.
