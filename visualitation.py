import streamlit as st
import pandas as pd
import plotly.express as px

xls = pd.read_excel('data.xlsx', sheet_name='Sheet1')

def asal_sekolah():
    xls.dropna(inplace=True)
    sekolah = xls['Tahap PMB'].unique().tolist()

    df = xls.groupby(['Tahap PMB'])['Tahap PMB'].count()

    pie_chart = px.pie(df, title="Data Masuk mahasiswa berdasarkan tahap PMB", values="Tahap PMB", names=sekolah)
    st.plotly_chart(pie_chart)

    st.dataframe(xls)


def unit():
    xls.dropna(inplace=True)
    unit = xls['UNIT'].unique().tolist()

    df = xls.groupby(['UNIT'])['UNIT'].count()

    pie_chart = px.pie(df, title="Data Masuk mahasiswa berdasarkan tahap PMB", values="UNIT", names=unit)
    st.plotly_chart(pie_chart)

    st.dataframe(xls)

def jurusan_pertama():
    # xls.dropna(inplace=True)
    fils = xls['Pilihan Prodi 2'].unique().tolist()

    df = xls.groupby(['Pilihan Prodi 2'])['Pilihan Prodi 2'].count()

    pie_chart = px.pie(df, title="Data Masuk mahasiswa berdasarkan tahap PMB", values="Pilihan Prodi 2", names=fils)
    st.plotly_chart(pie_chart)

    st.dataframe(xls)