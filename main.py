"""WTO Table Grabber

This script scrapes data from the WTO website by simulating browser interaction
using selenium. This data cannot be simply scraped using a typical web-scraping
package like BeautifulSoup because the relevant information is dynamically
generated and updated.
"""

import urllib.request
import csv
import os.path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

urls = ["https://www.wto.org/english/tratop_e/covid19_e/trade_related_goods_measure_e.htm",
        "https://www.wto.org/english/tratop_e/covid19_e/trade_related_ip_measure_e.htm",
        "https://www.wto.org/english/tratop_e/covid19_e/trade_related_services_measure_e.htm"]

def gen_file_name(url):
    """Generates the name for the CSV file

    This function extracts the last element in the url's path and removes the
    file extension
    """
    parsed_url = urlparse(url)
    last_path = os.path.split(parsed_url.path)[1]
    return last_path.split('.')[0]

def get_data_and_write_csv(url):
    """Retrieve the data from the given url and write it to a CSV"""
    with webdriver.Firefox() as driver:
        # Fetch the resource
        driver.get(url)

        # Wait up to 5 seconds until table is generated
        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        )

        table = driver.find_element_by_id("dataTable")
        thead = table.find_element(By.TAG_NAME, 'thead')
        head_trs = thead.find_elements(By.TAG_NAME, 'tr')

        tbody = table.find_element(By.TAG_NAME, 'tbody')
        trs = tbody.find_elements(By.TAG_NAME, 'tr')

        # Write each row to a csv file
        with open(gen_file_name(url) + '.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for tr in head_trs:
                header_row_data = []
                ths = tr.find_elements(By.TAG_NAME, 'th')
                for th in ths:
                    header_row_data.append(th.text)
                writer.writerow(header_row_data)

            for tr in trs:
                row_data = []
                tds = tr.find_elements(By.TAG_NAME, 'td')
                for td in tds:
                    row_data.append(td.text)
                writer.writerow(row_data)

def main():
    for url in urls:
        get_data_and_write_csv(url)

if __name__ == '__main__':
    main()
