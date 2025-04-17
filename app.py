"""
This project provides a platform to explore and analyze car-related data.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
vehicles_df = pd.read_csv('./vehicles.csv')

# Set the title of the app
st.header("Vehicle Data Analysis")
st.subheader("Explore the dataset and visualize the data")

# Set the options for the user to select the type of plot they want to create
st.write("Select the type of plot you want to create")
hist_button = st.checkbox("Histogram")
disp_button = st.checkbox("Scatter plot")
st.write("You can select multiple options.")

# If the user selects a histogram, create a histogram plot
if hist_button:
    st.write('Creating histogram for the dataset of car sells')
    fig = px.histogram(vehicles_df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# If the user selects a scatter plot, create a scatter plot
if disp_button:
    st.write('Creating scatter plot for the dataset of car sells')
    # Create a scatter plot
    fig = px.scatter(vehicles_df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
