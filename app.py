import streamlit as st
from dotenv import load_dotenv
import os

import pandas as pd

from db import Database

load_dotenv()

with Database(os.getenv('DATABASE_URL')) as pg:
    pg.create_table()

    st.title('Quote Generator')

    df = pd.read_sql('SELECT * FROM quotes', pg.con)
    st.dataframe(df)