import csv
import urllib.request
from bs4 import BeautifulSoup

practice_area = []
with open('practice_area.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = " ", quotechar = "|")
    for row in reader:
        city = ' '.join(row)
        city = city[city.index(',') + 2: -1]
        practice_area.append(city)
practice_area = practice_area[1::]

for area in practice_area:
    tmp = area.replace(" ", "-")
    tmp = tmp.replace(",", "")
    print(tmp)
