import streamlit as st
from scraper import Scraper
import pandas as pd
import base64

def main():
    st.title("Tokopedia Scraper")
    st.write("Aplikasi ini memungkinkan Anda untuk melakukan scraping data produk dari Tokopedia.")

    # Input keyword dan jumlah halaman dari user
    keyword = st.text_input("Masukkan keyword produk yang ingin Anda cari di Tokopedia:")
    total_pages = st.number_input("Masukkan jumlah halaman yang ingin Anda scraping:", min_value=1, step=1)

    # Tombol untuk memulai scraping
    if st.button("Mulai Scraping"):
        scraper = Scraper()
        data = scraper.get_data(keyword, total_pages)
        
        # Konversi data menjadi DataFrame
        df = pd.DataFrame(data)

        # Tampilkan DataFrame
        st.write("Data Hasil Scraping:")
        st.dataframe(df)

        # Tombol untuk mengunduh hasil sebagai CSV atau JSON
        if not df.empty:
            st.write("Download Data:")
            st.write("Klik tautan di bawah ini untuk mengunduh file.")
            st.markdown(get_table_download_link(df, file_type='csv'), unsafe_allow_html=True)
            st.markdown(get_table_download_link(df, file_type='json'), unsafe_allow_html=True)

def get_table_download_link(df, file_type='csv'):
    """
    Membuat tautan unduhan untuk DataFrame sebagai file CSV atau JSON.

    Parameters:
        df (pandas.DataFrame): DataFrame yang akan diunduh.
        file_type (str): Tipe file yang diinginkan, 'csv' atau 'json'.

    Returns:
        str: Tautan unduhan dalam format HTML.
    """
    if file_type == 'csv':
        csv = df.to_csv(index=False)
        file_extension = "csv"
    elif file_type == 'json':
        csv = df.to_json(indent=4)
        file_extension = "json"
    
    b64 = base64.b64encode(csv.encode()).decode()  # Encode ke base64
    href = f'<a href="data:file/csv;base64,{b64}" download="dataset.{file_extension}">Unduh file {file_extension.upper()}</a>'
    return href

if __name__ == '__main__':
    main()
