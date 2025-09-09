import streamlit as st
import pandas as pd
import requests


st.sidebar.title("My Covid Tracker")

def local_css(file_name):
    with open(file_name) as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")


st.markdown("<h1 class='title'>🦠 COVID-19 Tracker</h1>", unsafe_allow_html=True)

st.markdown(
    "<p class='instruction-text'>Enter a country name to get the latest COVID-19 statistics.</p>",
    unsafe_allow_html=True
)

country = st.text_input("", "Sri Lanka")

if st.button("Get Data"):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.markdown(f"<div class='metric-card cases'>Total Cases: {data['cases']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-card deaths'>Deaths: {data['deaths']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-card recovered'>Recovered: {data['recovered']}</div>", unsafe_allow_html=True)

    else:
        st.error("Country not found!")