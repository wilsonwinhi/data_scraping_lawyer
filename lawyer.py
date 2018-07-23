# import libraries-------------------------------------------------------
import urllib.request
from bs4 import BeautifulSoup
import csv

# CA city list-----------------------------------------------------------
CA_city = []
with open('CA_city.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = " ", quotechar = "|")
    for row in reader:
        city = ' '.join(row)
        city = city[city.index(',') + 2: -1]
        CA_city.append(city)
CA_city = CA_city[1::]

# PA city list-----------------------------------------------------------
PA_city = []
with open('PA_city.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = " ", quotechar = "|")
    for row in reader:
        city = ' '.join(row)
        city = city[city.index(',') + 2: -1]
        PA_city.append(city)
PA_city = PA_city[1::]


# practice area list-----------------------------------------------------------
practice_area = []
with open('practice_area.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = " ", quotechar = "|")
    for row in reader:
        city = ' '.join(row)
        city = city[city.index(',') + 2: -1]
        practice_area.append(city)
practice_area = practice_area[1::]

#----------------------------------------------------------------------
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('https://www.martindale.com/Criminal-law-lawyers/los-angeles/california/')

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(response, 'html.parser')

#for name_box in soup.find_all('ul', attrs={'class': 'attorneys'}):
    #print(name_box)
    #print("\n")

## for states, i guess i'll just write separate script

## for CA for instance, i'll first loop through
## area of practice
## city
## to find attorney info
for city in CA_city:
    city_parse = city.replace(" ", "-")
    city_parse = city_parse.replace(".", "")
    # print(city_parse)
    for area in practice_area:
        area_parse = area.replace(" ", "-")
        area_parse = area_parse.replace(",", "")
        # print(area_parse)
        tmp_url = 'https://www.martindale.com/' + area_parse + '-lawyers/' + city_parse + 'california/'
        print(tmp_url)
