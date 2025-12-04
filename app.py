import streamlit as st
import scrap_data
import process_data as preprocess
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pickle
import os
# import torch
import datetime
# import torch.nn as nn
# import torch.nn.functional as F
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

# Inject Bootstrap 5
st.markdown("""
<style>
    .block-container {
        padding: 0px 0px 0px 0px;
        max-width: 90% !important;
        width: 90% !important;
        text-align: center;
    }
    .btn-padding-top {
    padding-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# --- Navbar Header ---
# === MAIN CONTAINER ===
# === MAIN FULL-WIDTH CONTAINER ===
st.markdown("""<div class="container-fluid p-0 m-0">""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar navbar-expand-lg rounded mb-4" style="background-color: #e3f2fd;">
  <div class="container-fluid">
        <h2><strong>Dashboard</strong></h2>
        <h5 class="text-center">Compair Absolute error and percentage error from  Actual Price and Predicted Price</h5>
  </div>
</nav>
""", unsafe_allow_html=True)

# --- Search Form ---

with st.form("flight_search"):
    st.markdown("### ✈️ Flight Search")
    col1, col2, col3, col4, col5, col6 = st.columns([1,3,3,1,2, 2])
    class_map = {
        'e': 'Economy',
        'w': 'Premium Economy',
        'b': 'Business'
    }
    airport_fullname = {
        "BOM": "Chhatrapati Shivaji Maharaj International Airport, Mumbai",
        "DEL": "Indira Gandhi International Airport, Delhi",
        "BLR": "Kempegowda International Airport, Bengaluru",
        "HYD": "Rajiv Gandhi International Airport, Hyderabad",
        "CCU": "Netaji Subhas Chandra Bose International Airport, Kolkata",
        "MAA": "Chennai International Airport, Chennai",
        "AMD": "Sardar Vallabhbhai Patel International Airport, Ahmedabad",
        "PNQ": "Pune International Airport, Pune",
        "GOI": "Dabolim Airport, Goa",
        "COK": "Cochin International Airport, Kochi"
    }
    with col1:
        trip_type = st.selectbox("Trip Type", ["One Way", "Round Trip"])
    with col2:
        origin = st.selectbox("From", options= list(airport_fullname.keys()), format_func= lambda x: airport_fullname[x] )
    with col3:
        destination = st.selectbox("To", options= list(airport_fullname.keys()), format_func= lambda x: airport_fullname[x] )
    with col4:
        depart_date = st.date_input("Depart", datetime.date.today())
    with col5:
        cubin =  st.selectbox(
            "Travel Class",
            options=list(class_map.keys()),  # ['e', 'w', 'b']
            format_func=lambda x: class_map[x]  # Show label instead of key
        )
    with col6:
        st.markdown('<div class="btn-padding-top">', unsafe_allow_html=True)
        submit = st.form_submit_button("Search", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)



# --- Show Results only after Submit ---
if submit:
    st.subheader(f"Flights {origin} → {destination} on {depart_date.strftime('%d-%m-%Y')} {class_map[cubin]}")
    df = scrap_data.fetch_data_from_source(origin, destination, depart_date.strftime('%d%m%Y'), cubin)
    print(df.head())
    df_copy = df.copy()
    #df = preprocess.preprocess_of_data(df)
    print(df.head())

st.markdown("</div>", unsafe_allow_html=True)