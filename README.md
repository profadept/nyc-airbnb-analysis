# NYC Airbnb Market Analysis — 2019

This project analyses the key factors that drive prices across NYC 2019 Airbnb
listings, examining whether location, room type, or host behaviour is the dominant
price signal. The dataset covers 48,895 listings spread across five boroughs,
collected in 2019 and sourced from Kaggle's NYC Airbnb Open Data. The notebook
walks through data cleaning, exploratory analysis, and three focused questions
that each challenge assumptions about how the short-term rental market actually works.

## Key Findings

- **Location alone does not determine price.** Staten Island, despite having the
fewest listings of any borough, commands a higher median price than the Bronx,
volume and price move independently across the NYC market.

- **Room type is the strongest price driver.** Entire home/apartments carry a median
price of `$160`, sitting `$115` above shared rooms at `$45`. Across every borough without
exception, room type is a more reliable price signal than location.

- **More listings means less engagement.** Hosts managing larger portfolios generate
fewer reviews per listing, the individual attention that drives guest engagement
does not scale with listing count.

## Project Structure

```
nyc-airbnb-analysis/
├── data/
│   ├── AB_NYC_2019.csv
│   └── AB_NYC_2019.parquet
├── figures/
├── notebooks/
│   └── NYC_Airbnb_EDA.ipynb
├── scripts/
│   └── download_data.py
├── pyproject.toml
└── README.md
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

## License

MIT License — project code only. Dataset subject to Kaggle and Inside Airbnb terms.
