import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Create a dashboard title
st.title("Bike Sharing Dashboard")

# Create a sidebar 
with st.sidebar:
    # Menambahkan gambar sepeda 
    st.image("Sepeda.png")

#Converts 'dteday' to datetime type
day_df['dteday'] = pd.to_datetime(day_df['dteday']) 

#Calculate monthly data
monthly_counts = day_df.groupby(day_df['dteday'].dt.to_period('M'))['cnt'].max().reset_index()

#Pertanyaan 1 
st.header("Pertanyaan 1: How has the company's sales performance been in recent years?")
st.subheader("Monthly Counts")

#Create visualizations Graph of Number of Customers per Month in 2012
fig, ax = plt.subplots(figsize=(24, 5))
sns.pointplot(data=monthly_counts, x='dteday', y='cnt', ax=ax, color="#90CAF9", marker='o', errorbar=None)
ax.set_xlabel('Month')
ax.set_ylabel('Sum')
ax.set_title('Graph of Number of Customers per Month in 2012')
st.pyplot(fig)

#Pertanyaan 2
st.header("Pertanyaan 2: How effective is bike sharing over a 24-hour period?")
st.subheader("Hourly Counts")

#Create visualizations Bike Sharing over a 24-hour period
fig, ax = plt.subplots(figsize=(25,10))
sns.pointplot(data=hour_df, x='hr', y='cnt', hue='workingday', errorbar=None, ax=ax, palette=['red', 'blue'])
ax.set(title='Bike Sharing over a 24-hour period')
ax.set_ylabel('cnt')
ax.set_xlabel('hr')
st.pyplot(fig)
