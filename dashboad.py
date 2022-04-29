import streamlit as st
import pandas.io.sql as sqlio
import mysql.connector
from analy_visu import *

st.set_page_config(page_title="Tweets Analysis Dashboard",
                   page_icon=":bar_chart:", layout="wide")
dataframe = mysql.connector.connect(host='localhost', user='root', password='Dalia@1234BWIZA', database='tweets', buffered=True)
print(dataframe)
# cursor = conn.cursor()
# query = '''SELECT * FROM tweetinformation'''
# df_tweet = data = sqlio.read_sql_query(query, conn)



SIDEBAR_OPTION_PROJECT_WIKI = "Project Wiki"
SIDEBAR_OPTION_ANALYSIS = "Data Analysis & Visualisation"
SIDEBAR_OPTION_FORECAST = "Predict"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_WIKI, SIDEBAR_OPTION_ANALYSIS, SIDEBAR_OPTION_FORECAST]

def main():
    st.sidebar.success("Please choose an option bellow.")
    SIDEBAR_STATUS = st.sidebar.selectbox('Menu Option', SIDEBAR_OPTIONS)

    if SIDEBAR_STATUS == SIDEBAR_OPTION_PROJECT_WIKI:
        st.text("Welcome to week0 assesiment project")
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_ANALYSIS:
        st.text("Welcome to the data analysis and vidualization")
        analysis_section()

    elif SIDEBAR_STATUS == SIDEBAR_OPTION_FORECAST:
        st.text("Welcome to the model prediction")

    else:
        pass



main()