install.packages("xml2")
library(xml2)
install.packages("rvest")
library(rvest)
install.packages("tidyverse")
install.packages("purrr")
library(purrr)

# get the city (CA, PA)
city_base_url<- "https://www.martindale.com/by-location/california-lawyers/"
city_page <- read_html(city_base_url)
CA_city <- "#cityPanelAll .navigable"
CA_city_vec <- html_text(html_nodes(city_page, CA_city))
CA_city_vec

CA_city_df <- data.frame(CA_city_vec)
write.csv(CA_city_df,'CA_city.csv')

city_base_url<- "https://www.martindale.com/by-location/pennsylvania-lawyers/"
city_page <- read_html(city_base_url)
PA_city <- "#cityPanelAll li"
PA_city_vec <- html_text(html_nodes(city_page, PA_city))
PA_city_vec

PA_city_df <- data.frame(PA_city_vec)
write.csv(PA_city_df,'PA_city.csv')

# get practice area
practice_area_base_url<- "https://www.martindale.com/areas-of-law/"
practice_area_page <- read_html(practice_area_base_url)
practice_area <- "#aopPanelAll a"
practice_area_vec <- html_text(html_nodes(practice_area_page, practice_area))
practice_area_vec

practice_area_df <- data.frame(practice_area_vec)
write.csv(practice_area_df,'practice_area.csv')

# if i'm already in the attorney's page, can i extract the info i need?

attorney_base_url<- "https://www.martindale.com/los-angeles/california/daniel-j-kolodziej-117753-a/"
attorney_page <- read_html(attorney_base_url)
attorney <- ".experience-value"
test <- ".attorney-info-brd a , address , .attorney-info-brd > ul li:nth-child(1)"
attorney_vec <- html_text(html_nodes(attorney_page, attorney))
test_vec <- html_text(html_nodes(attorney_page, test))
attorney_vec
test_vec
practice_area_df <- data.frame(practice_area_vec)
write.csv(practice_area_df,'practice_area.csv')

#step 1: get a url
url<- "https://www.martindale.com/by-location/california-lawyers/"

#step 2: load html
page <- read_html(url)

#step 3: get node ID of data
test <- ".srr-title strong , h1"
city <- "#cityPanelAll .navigable"
#main_title_id <- "h1"
# author_id <- ".results-block__author"
# date_id <- ".results-block__time--toc"
# issue_id <- ".results-block__toc-issue-heading"
# year_id <- "#Year"
#test_id <- '#Year'

#step 4: actually get the data using html_node

###format html_nodes(page, id)

main_title_vec <- html_text(html_nodes(page, main_title_id))
# author_vec <- html_text(html_nodes(page, author_id))
# date_vec <- html_text(html_nodes(page, date_id))
# issue_vec <- html_text(html_nodes(page, issue_id))
# year_vec <- html_text(html_nodes(page, year_id))
test_vec <- html_text(html_nodes(page, test))
city_vec <- html_text(html_nodes(page, city))
#main_title_vec
#author_vec
#date_vec
#issue_vec 
#year_vec
test_vec
city_vec

#Step 5: package the information into something useful
df <- data.frame(city_vec)
colnames(df) <- c("Title", "Author", "Date", "Issue", "Year")
str(df)

write.csv(df, 'test.csv')
View(df)

##Step 6:

print(page)