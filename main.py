import requests
import csv
from bs4 import BeautifulSoup

with open('url.txt', 'r') as file:
    urls = file.read().splitlines()

for url in urls:
    line_uid = url.split(',')[1]
    try:
        response = requests.get(url.split(',')[0])
        soup = BeautifulSoup(response.text, 'html.parser')
        decoded_line_uid = line_uid[1:]  # Remove the 'U' prefix
        decoded_line_uid = decoded_line_uid.zfill(len(line_uid) - 1)  # Pad with leading zeros
        decoded = "U" + decoded_line_uid

        h1_tag = soup.find('h1', class_='title-page').text
        span_tag_name = soup.find_all('span', class_='col-xs-6 col-sm-7')[2].get_text(strip=True) 
        span_tag_customer_name = soup.find_all('span', class_='col-sm-8 col-xs-6')[2].get_text(strip=True) 
        span_tag_phone = soup.find_all('span', class_='col-sm-8 col-xs-6')[3].get_text(strip=True) 

        with open('data.csv', 'a', encoding='utf-8-sig', newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow([str(line_uid), str(decoded), str(h1_tag), str(span_tag_name), str(span_tag_customer_name), span_tag_phone])
    except ValueError:
        print("Invalid Status Error")

print("Create File data.csv Successfully!")
