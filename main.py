from ast import If
import streamlit as st
import pandas as pd
import visualitation as vs
import plotly.express as px



st.write("""
# Visualisasi Data
""")
# if you dont know how to read the go to this site https://docs.streamlit.io/

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

year = st.selectbox('What year you want to visualize ?',('---- Select ----','2020', '2021'), key='year')

coloum_array = (
        '---- Select ----',
        'Tahap Pmb',
        'Asal Sekolah',
        'Pilihan Prodi 1',
        'Pilihan Prodi 2'
    )

coloum = st.selectbox('How would you like to be filter?', coloum_array, key='filter')

if coloum != '---- Select ----' :
    if coloum == 'Tahap Pmb':
        vs.asal_sekolah()
    elif coloum == 'Asal Sekolah':
        vs.unit()
    elif coloum == 'Pilihan Prodi 1':
        vs.jurusan_pertama()
    # st.dataframe(df)
    # st.table(df)
    


