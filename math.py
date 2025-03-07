import streamlit as st
import pandas as pd

# Streamlit App Title
st.title("Random Sampling of Participants")

# Upload CSV File
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the first few rows of the dataframe
    st.subheader("Your Data")
    st.write(df.head())

    # Check if there are at least 80 rows
    if len(df) >= 80:
        # Button to trigger random sampling
        if st.button('Select 80 Random Participants'):
            # Randomly select 80 participants
            random_sample = df.sample(n=80, random_state=42)
            
            # Display the sampled data
            st.subheader("80 Randomly Selected Participants")
            st.write(random_sample)
    else:
        st.error("Your dataset should have at least 80 participants.")

