import pandas as pd
import numpy as np
import streamlit as st
import time


# App title
st.title("CRIMES AGAINST WOMEN IN INDIA")

data_url = ('https://raw.githubusercontent.com/apacheteam/Crime-Against-Women-PP22-C623-APACHE-TEAM/'
            'master/crimes_against_women_2001-2014.csv')
#data_url = (r'C:\Users\Tomi\datasets\crimes_against_women_2001-2014.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    return data

# Let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load data
st.subheader('Select data size')
rows_to_load = st.slider('Number of samples (rows)', 1000, 10677, 5000)
dataset = load_data(rows_to_load)

# Notify the reader that the data was successfully loaded.
data_load_state.text("Loading data...done! (using st.cache)")

# Start of Data Analysis and Visualizations
if st.checkbox('Show Analysis'):
    # Inspect the raw data
    st.subheader('Raw data')
    st.write(dataset)

    # Show rape cases per year
    st.subheader('Number of rape cases per year')
    #hist_values = np.histogram(dataset[''])
    #st.bar_chart(hist_values)

    # plot a line chart for rape cases
    rape_data = pd.DataFrame(dataset.groupby('year')['rape'].sum())
    st.line_chart(rape_data['rape'])

# Prediction selectbox
df = pd.DataFrame({
    'first column': ['Rape', 'Kidnapping and Abduction', 'Dowry Deaths'],
    'second column': [2015, 2016, 2022]
    })

option1 = st.sidebar.selectbox(
    'Crime: ',
     df['first column'])

option2 = st.sidebar.selectbox(
    'Year: ',
    df['second column'])

'Predict number of ', option1, 'in the year ', str(option2)

st.button('PREDICT')


print('Debug: Complete')


