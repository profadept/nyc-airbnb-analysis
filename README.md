# 🏙️ NYC Airbnb Data Analysis
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)

Exploratory Data Analysis of **New York City Airbnb listings**, focusing on pricing, availability, host behavior, and neighborhood patterns across the five boroughs.

## 📊 Project Overview
This project explores the **NYC Airbnb Open Data** dataset to answer questions about pricing, neighborhood trends, availability, and host behavior. The analysis follows a complete professional workflow suitable for portfolio use.

## 🧰 Tools and Libraries
Python 3.11  
Pandas, NumPy  
Matplotlib, Seaborn  
Jupyter Notebook  
Conda environment  

## 🧱 Project Structure
nyc-airbnb-analysis/
├── data/  
├── figures/  
├── notebooks/  
│   └── NYC_Airbnb_EDA.ipynb  
├── environment.yml  
├── requirements.txt  
├── .gitignore  
└── README.md  

## ⚙️ Setup Instructions
### Conda
conda env create -f environment.yml  
conda activate nyc-airbnb-env  

### pip
python -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  

## 📥 Dataset
Download from Kaggle:  
https://www.kaggle.com/datasets/airbnb/new-york-city  
Place the CSV inside the **data/** folder.

## 🔍 EDA Outline
1. Import & Setup  
2. Data Overview  
3. Cleaning & Fixes  
4. Feature Engineering  
5. Univariate Analysis  
6. Bivariate Analysis  
7. Summary & Insights  

## 📈 Key Insights
- Manhattan has the highest price levels.  
- Brooklyn shows strong listing volume at moderate prices.  
- Cheaper listings attract more guest reviews.  
- Host activity varies sharply by portfolio size.  
- Availability shows seasonal and behavioral patterns.

## 🧾 License
MIT License for project code.  
Dataset licensed by Kaggle and Inside Airbnb.
