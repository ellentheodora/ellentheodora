import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Create a dashboard title
st.title("Bike Sharing Dashboard")

day_df['dteday'] = pd.to_datetime(day_df['dteday']) 

# Create a sidebar
st.sidebar.header("Select a Visualization")
viz_type = st.sidebar.selectbox("Select a visualization type", ["Monthly Counts", "Hourly Counts", "Scatterplot"])

# Create a monthly counts visualization
if viz_type == "Monthly Counts":
    monthly_counts = day_df.groupby(day_df['dteday'].dt.to_period('M'))['cnt'].max().reset_index()
    fig, ax = plt.subplots(figsize=(24, 5))
    sns.pointplot(data=monthly_counts, x='dteday', y='cnt', ax=ax, color="#90CAF9", marker='o', err_kws={'alpha': 0})
    ax.set_xlabel('Month')
    ax.set_ylabel('Sum')
    ax.set_title('Graph of Number of Customers per Month in 2012')
    st.pyplot(fig)

# Create an hourly counts visualization
elif viz_type == "Hourly Counts":
    fig, ax = plt.subplots(figsize=(25,10))
    sns.pointplot(data=hour_df, x='hr', y='cnt', hue='workingday', errorbar=None, ax=ax, palette=['red', 'blue'])
    ax.set(title='Bike Sharing over a 24-hour period')
    ax.set_ylabel('cnt')
    ax.set_xlabel('hr')
    st.pyplot(fig)

# Create a scatterplot visualization
elif viz_type == "Scatterplot":
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.scatterplot(data=day_df, x='dteday', y='cnt', ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.set_title('Scatterplot of Bike Sharing Data')
    st.pyplot(fig)

# Create a histogram visualization
st.header("Histogram of Bike Sharing Data")
fig, ax = plt.subplots(figsize=(10, 8))
sns.histplot(data=day_df, x='cnt', ax=ax)
ax.set_xlabel('Count')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Bike Sharing Data')
st.pyplot(fig)

# Create a lineplot visualization
st.header("Lineplot of Bike Sharing Data")
fig, ax = plt.subplots(figsize=(10, 8))
sns.lineplot(data=day_df, x='dteday', y='cnt', ax=ax)
ax.set_xlabel('Date')
ax.set_ylabel('Count')
ax.set_title('Lineplot of Bike Sharing Data')
st.pyplot(fig)