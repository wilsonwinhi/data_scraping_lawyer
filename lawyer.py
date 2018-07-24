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

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

# opener = AppURLopener()
# response = opener.open('https://www.martindale.com/Criminal-law-lawyers/los-angeles/california/')

# parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(response, 'html.parser')

#for name_box in soup.find_all('ul', attrs={'class': 'attorneys'}):
    #print(name_box)
    #print("\n")

## for states, i guess i'll just write separate script

## for CA for instance, i'll first loop through
## area of practice
## city
## to find attorney info

# put dictionary into list
# list of dictionary


CA_link = []
with open('lawyer_url.csv','w') as file:
    for city in CA_city:
        city_parse = city.replace(" ", "-")
        city_parse = city_parse.replace(".", "")
        # print(city_parse)
        for area in practice_area:
            area_parse = area.replace(" ", "-")
            area_parse = area_parse.replace(",", "")
            area_parse = area_parse.replace("/", "-")
            #print(city_parse)
            #print(area_parse)
            tmp_url = 'https://www.martindale.com/' + area_parse + '-lawyers/' + city_parse + '/california/'
            # print(tmp_url)
            opener = AppURLopener()
            response = opener.open(tmp_url)
            soup = BeautifulSoup(response, 'html.parser')
            for name_box in soup.find_all('ul', attrs={'class': 'attorneys'}):
                text = str(name_box)
                #print(text)
                #print(type(text))
                #print(text.find('https'))
                #print(text.index('<div'))
                url = text[text.find('href=') + 6: text.find('<div') - 3]
                print(url)
                file.write(url)
                file.write('\n')
