import streamlit as st
import pandas as pd

df = pd.read_csv('car_data.csv')

car_name = st.sidebar.text_input("Car Name")

car_transmission = st.sidebar.multiselect("Transmission", ['Manual', 'Automatic'], default=['Manual', 'Automatic'])

car_price = st.sidebar.slider("Selling Price", 0, 100, (0,20))

car_year = st.sidebar.slider("Year", 2000, 2024, (2000,2010))

if st.sidebar.button("Submit"):
    filtered_df = df
    if car_name:
        filtered_df = filtered_df[df['Car_Name'].str.contains(car_name, case=False, na=False)]
    filtered_df = filtered_df[filtered_df['Transmission'].isin(car_transmission)]
    filtered_df = filtered_df[(filtered_df['Selling_Price'] >= car_price[0]) & (filtered_df['Selling_Price'] <= car_price[1])]
    filtered_df = filtered_df[(filtered_df['Year'] >= car_year[0]) & (filtered_df['Year'] <= car_year[1])]
    
    st.dataframe(filtered_df)
else:
    st.dataframe(df)

