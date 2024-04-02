import streamlit as st 
import yfinance as yf
import pandas as pd
import datetime
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)
st.header('Trading Strategies and Indicators by **RCA Capital**')

st.markdown(
    """
    **RCA Capital Strategies App**

    
    In this app you'll find the following strategies:
    

    * Scalping
    * Big Dog Consolidations
    * Swing Trading Breakouts

    **👈 Select a strategy from the sidebar** 

"""
)