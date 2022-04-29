import streamlit as st
#from data import dataset
from dashboad import dataframe

#dataframe = dataframe()

def analysis_section():

    #st.text('Bellow we analyse retweet accounts')
    st.line_chart(dataframe.most_retweets)
    