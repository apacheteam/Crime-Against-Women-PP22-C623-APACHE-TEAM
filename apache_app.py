import pandas as pd
import numpy as np
import streamlit as st

import warnings
warnings.filterwarnings('ignore')


# App title
st.title("CRIMES AGAINST WOMEN IN INDIA")

data_url = ('https://raw.githubusercontent.com/apacheteam/Crime-Against-Women-PP22-C623-APACHE-TEAM/'
            'master/crimes_against_women_2001-2014.csv')
#data_url = (r'C:\Users\Tomi\datasets\crimes_against_women_2001-2014.csv')

@st.cache
def load_data():
    data = pd.read_csv(data_url)
    return data

# Let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load data

dataset = load_data()

# Notify the reader that the data was successfully loaded.
data_load_state.text("Loading data...done! (using st.cache)")

# Start of Data Analysis and Visualizations
if st.checkbox('View raw data'):
    # Inspect the raw data
    st.subheader('Dataset')
    st.write(dataset)
    st.write(dataset.shape)

    # Show rape cases per year
    st.subheader('Number of rape cases per year')
    # hist_values = np.histogram(dataset[''])
    # st.bar_chart(hist_values)



# Prediction selectbox

#state = st.sidebar.selectbox('Please select a state you\'re interested in:', (unique_states))

state = st.sidebar.selectbox(
    'Select a state you\'re interested in: ',
    (unique_states)
)

#crime = st.sidebar.selectbox('select a crime:', ('rape',
       #'kidnapping_and_abduction', 'dowry_deaths', 'assault_on_women',
       #'insult_to_modesty', 'cruelty_by_husband_or_relatives',
       #'importation_of_girls'))


