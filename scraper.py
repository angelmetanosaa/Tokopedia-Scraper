import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def get_data(self, keyword, total_pages):
        base_url = f'https://www.tokopedia.com/search?q={keyword}'
        data = []

        for page in range(1, total_pages + 1):
            page_url = f'{base_url}&page={page}'
            self.driver.get(page_url)
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
            time.sleep(2)

            # Parse halaman
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            # Scrap halaman website
            for item in soup.find_all('div', class_='css-54k5sq'):
                try:
                    # Scrap nama produk
                    product_name_element = item.find('div', class_='prd_link-product-name css-3um8ox')
                    product_name = product_name_element.text.strip() if product_name_element else ''
                    if not product_name:
                        continue  # Melanjutkan ke iterasi berikutnya jika tidak ada nama produk

                    # Scrap URL Gambar
                    image_element = item.find('div', class_='pcv3_img_container css-1mygogd')
                    image_url = image_element.find('img')['src'] if image_element else ''

                    # Scrap Harga Normal
                    price_normal_element = item.find('div', class_='prd_label-product-slash-price css-xfl72w')
                    price_normal = price_normal_element.text.strip() if price_normal_element else ''

                    # Scrap Diskon
                    discount_element = item.find('div', class_='prd_badge-product-discount css-1xelcdh')
                    discount = discount_element.text.strip() if discount_element else ''
                    
                    # Scrap Harga Diskon
                    price_element = item.find('div', class_='prd_link-product-price css-h66vau')
                    price_discount = price_element.text.strip() if price_element else ''

                    # Jika tidak ada diskon, pindahkan data dari kolom Harga Diskon ke kolom Harga Normal
                    if not discount:
                        price_normal = price_discount
                        price_discount = ''

                    # Cek apakah ada rating atau tidak
                    rate_element = item.find('span', class_='prd_rating-average-text css-t70v7i')
                    rate = rate_element.text.strip() if rate_element else ''

                    # Cek apakah ada item terjual atau tidak
                    sold_element = item.find('span', class_='prd_label-integrity css-1sgek4h')
                    sold = sold_element.text.strip() if sold_element else '0'

                    # Scrap detail alamat
                    location_element = item.find('span', class_='prd_link-shop-loc css-1kdc32b flip')
                    location = location_element.text.strip() if location_element else ''
                    
                    seller_element = item.find('span', class_='prd_link-shop-name css-1kdc32b flip')
                    seller = seller_element.text.strip() if seller_element else ''

                    data.append(
                        {
                            'Produk': product_name,
                            'URL Gambar': image_url,
                            'Penjual' : seller,
                            'Lokasi': location,
                            'Harga Normal': price_normal or '0',  # Jika tidak ada, isi dengan '0'
                            'Diskon': discount or '',  # Jika tidak ada diskon, nilai default adalah string kosong
                            'Harga Diskon': price_discount or '0',  # Jika tidak ada, isi dengan '0'
                            'Rate': rate or '0',  # Jika tidak ada, isi dengan '0'
                            'Terjual': sold or '0'  # Jika tidak ada, isi dengan '0'
                        }
                    )
                except AttributeError as e:
                    print(f"Error: {e}")
                    continue  # Melanjutkan ke iterasi berikutnya jika terjadi AttributeError

            time.sleep(1)

        self.driver.close()

        return data

if __name__ == '__main__':
    keyword = input("Masukkan keyword produk yang ingin Anda cari di Tokopedia: ")
    total_pages = int(input("Masukkan jumlah halaman yang ingin Anda scraping: "))

    scraper = Scraper()
    data = scraper.get_data(keyword, total_pages)
    
    df = pd.DataFrame(data)
    df.to_csv('dataset.csv', index=False)
