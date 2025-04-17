import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
vehicles_df = pd.read_csv('./vehicles.csv')

# Set the title of the app
st.header("Vehicle Data Analysis")
st.subheader("Explore the dataset and visualize the data")

hist_button = st.button("Create Histogram")
if hist_button:
    st.write('Creating histogram for the dataset of car sells')
    fig = px.histogram(vehicles_df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.checkbox("Scatter plot")
if disp_button:
    st.write('Creating scatter plot for the dataset of car sells')
    # Create a scatter plot
    fig = px.scatter(vehicles_df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
