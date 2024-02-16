# Tokopedia Scraper menggunakan BeautifulSoup

## Tujuan Kode
Tujuan dari kode ini adalah melakukan web scraping pada situs Tokopedia untuk mendapatkan informasi produk berdasarkan kata kunci tertentu. Pengguna diminta untuk memasukkan kata kunci produk yang ingin dicari dan jumlah halaman yang ingin di-scrape. Setelah itu, program akan melakukan scraping pada setiap halaman Tokopedia untuk mengumpulkan data produk seperti nama produk, URL gambar, penjual, lokasi penjual, harga normal, diskon (jika ada), harga diskon, rating produk, dan jumlah produk yang terjual.

## Teknis Program
Teknisnya, program menggunakan Selenium untuk mengotomatisasi browser Chrome dan BeautifulSoup untuk melakukan parsing HTML dari halaman web. Selenium digunakan untuk mengakses halaman web Tokopedia, sementara BeautifulSoup digunakan untuk mengekstrak informasi yang dibutuhkan dari halaman tersebut. Kemudian, data yang terkumpul akan disimpan dalam bentuk dataframe menggunakan Pandas dan diekspor ke dalam file CSV maupun JSON.

## Tahapan Running
Berikut adalah tahapan untuk menjalankan dan mendeploy aplikasi Streamlit yang Anda miliki:

1. **Membuat Environment**
   
   Buka terminal atau command prompt, lalu jalankan perintah berikut untuk membuat environment baru dengan nama `tokopedia-scraper`:
   ```
   conda create --name tokopedia-scraper python=3.8
   ```

2. **Aktifkan Environment**
   
   Setelah environment dibuat, aktifkan environment tersebut dengan menjalankan perintah berikut:
   ```
   conda activate tokopedia-scraper
   ```

3. **Install Dependensi**
   
   Pastikan Anda telah menginstal semua dependensi yang diperlukan. Untuk menginstal Streamlit dan dependensinya, jalankan perintah berikut di terminal atau command prompt:
   ```
   pip install streamlit
   pip install selenium
   pip install pandas
   ```

4. **Menyimpan Kode**
   
   Simpan kode yang Anda berikan dalam satu file, misalnya `deploy_scraper.py`.

5. **Jalankan Aplikasi**
    
   Buka terminal atau command prompt, arahkan ke direktori tempat Anda menyimpan file `deploy_scraper.py`, dan jalankan perintah berikut:
   ```
   streamlit run deploy_scraper.py
   ```

6. **Gunakan Aplikasi**
   
   Setelah menjalankan perintah di atas, Anda akan melihat URL lokal yang bisa Anda buka di browser. Buka URL tersebut, dan Anda akan melihat antarmuka aplikasi Streamlit. Masukkan kata kunci produk dan jumlah halaman yang ingin Anda scraping, lalu klik tombol "Mulai Scraping". Tunggu beberapa saat dan jika sudah selesai maka Anda dapat mengunduh file tersebut dalam format JSON maupun CSV.
