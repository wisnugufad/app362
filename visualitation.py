from turtle import title
import streamlit as st
import pandas as pd
import plotly.express as px

def get_visual(kriteria):
    read_xls = pd.read_excel('data.xlsx', sheet_name='Sheet1')

    xls = pd.DataFrame(read_xls, columns=['TAHAP PMB',
        'ASAL SEKOLAH',
        'PILIHAN PRODI 1',
        'PILIHAN PRODI 2',
        'PEKERJAAN AYAH',
        'PEKERJAAN IBU',
        'PROVINSI',
        'JENIS KELAMIN',
        'AGAMA',
        'TAHUN',
        'PROGRAM DITERIMA'])
    xls.dropna(inplace=True)

    tahun = xls['TAHUN'].unique().tolist()
    tahun.insert(0, "---- Select ----")

    year = st.selectbox('What year ?',tahun, key='year')

    if year != '---- Select ----':
        xls = xls.loc[xls['TAHUN']==year]
        df = xls.groupby([kriteria])[kriteria].count()
    else:
        df = xls.groupby([kriteria])[kriteria].count()

    cell_name = xls[kriteria].unique().tolist()
    

    title = "DATA MASUK MAHASISWA BERDASARKAN " + kriteria

    pie_chart = px.pie(df, title=title, values=kriteria, names=cell_name)
    st.plotly_chart(pie_chart)
    

    cell_name = xls[kriteria].unique().tolist()

    # df = px.data.tips()
    # fig = px.bar(df, x=cell_name, y='PROGRAM DITERIMA', barmode="group")
    # st.plotly_chart(fig)
    # fig.show()
    
    cell_name.insert(0, "---- Select ----")

    coloum_filter = st.selectbox('How would you like to be filter?', cell_name, key='filter_dataframe')
    
    if year != '---- Select ----':
        if coloum_filter != '---- Select ----' :
            rs_df = xls.loc[xls[kriteria] == coloum_filter, xls['TAHUN']==year]
        else:
            rs_df = xls.loc[xls['TAHUN']==year]
    else:
        rs_df = xls
        
    st.dataframe(rs_df)

# def asal_sekolah():
#     xls.dropna(inplace=True)
#     sekolah = xls['Tahap PMB'].unique().tolist()

#     df = xls.groupby(['Tahap PMB'])['Tahap PMB'].count()

#     pie_chart = px.pie(df, title="Data Masuk mahasiswa berdasarkan tahap PMB", values="Tahap PMB", names=sekolah)
#     st.plotly_chart(pie_chart)

#     st.dataframe(xls)


# def unit():
#     xls.dropna(inplace=True)
#     unit = xls['UNIT'].unique().tolist()

#     df = xls.groupby(['UNIT'])['UNIT'].count()

#     pie_chart = px.pie(df, title="Data Masuk mahasiswa berdasarkan tahap PMB", values="UNIT", names=unit)
#     st.plotly_chart(pie_chart)

#     st.dataframe(xls)

# def jurusan_pertama():
#     # xls.dropna(inplace=True)
#     fils = xls['Pilihan Prodi 2'].unique().tolist()

#     df = xls.groupby(['Pilihan Prodi 2'])['Pilihan Prodi 2'].count()

#     pie_chart = px.pie(df, title="Data Masuk mahasiswa berdasarkan tahap PMB", values="Pilihan Prodi 2", names=fils)
#     st.plotly_chart(pie_chart)

#     st.dataframe(xls)