import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

model = pickle.load(open('best_model.pkl','rb'))

st.set_page_config(layout="wide")

st.title("Customer Churn Prediction")

st.divider()

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    Name = st.text_input("Name")
with col2:
    Age = st.number_input("Age", value=0, format="%d")
with col3:
    Gender = st.radio(
        "Gender",
        ('Female', 'Male'))
with col4:
    Location = st.radio(
        "Location",
        ('Chicago', 'Houston', 'Los Angeles', 'Miami', 'New York'))
with col5:
    Subscription_Length_Months = st.number_input("Subscription_Length_Months", value=0, format="%d")
with col6:
    Monthly_Bill = st.number_input("Monthly_Bill ")
with col7:
    Total_Usage_GB = st.number_input("Total_Usage_GB")

st.divider()

if st.button('Predict'):


    user_data = {
        "Name": [Name],
        "Age": [Age],
        "Gender": [Gender],
        "Location": [Location],
        "Subscription_Length_Months": [Subscription_Length_Months],
        "Monthly_Bill": [Monthly_Bill],
        "Total_Usage_GB": [Total_Usage_GB]
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(user_data)


    # Mapping Gender with 0 and 1
    gender_mapping = {"Male": 0, "Female": 1}
    df["Gender"] = df["Gender"].map(gender_mapping)

    # Mapping Location with 0, 1, 2, and 3
    location_mapping = {"Houston": 0, "Los Angeles": 1, "Miami": 2, "New York": 3,"Chicago":4}
    df["Location"] = df["Location"].map(location_mapping)

    x = df.drop(['Name'], axis=1)
    result=model.predict(x)
    if result:
        st.write("customer will churn")
    else:
        st.write("Customer will not churn")
