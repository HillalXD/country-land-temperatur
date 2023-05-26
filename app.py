import pickle
import streamlit as st
import pandas as pd



with open('xgboost.pkl', 'rb') as f:
    model = pickle.load(f)

def app():
    st.title('Energy Consumption Prediction')


    inputs = {
        'month': st.number_input('Select Month', min_value=1, max_value=12),
        'year': st.number_input('Select Year', min_value=1983, max_value=2025)
    }

    df = pd.DataFrame(inputs, index=[0])
    prediction = model.predict(df)


    st.write("predicted average temperature in this month : {}".format(prediction[0]))

if __name__ == '__main__':
    app()
