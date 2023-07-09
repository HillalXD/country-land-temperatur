
# Indonesia temperature forecast

This project use to predict temperature in indonesia on spesific month and year

## Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [xgboost](https://xgboost.readthedocs.io/en/stable/)
- [streamlit](https://streamlit.io/)

## Usage

first, you can clone this git repository

```
git clone https://github.com/HillalXD/country-land-temperature.git
```

then navigate your command to this directory

```
cd country-land-temperature
```

after that run `app.py` to use streamlit app

```
streamlit run app.py
```


## Code 
- Template code is provided in the `temperature.ipynb` notebook file.
- `land-temperature.csv` in provide data source for training model
- `xgboost.pkl` is trained classifier model file
- `app.py` is streamlit web application to user input features for model predicting 


## Dataset features

for doing prediction you need to input this features:

| features  | explanation  | 
| :-------- | :------- | 
| month | month in number |
| year | year for energy consumption forecast|




