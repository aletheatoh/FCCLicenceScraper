# FCC Archive Webscraping
Code to webscrape data from the Federal Communications Commission (FCC)'s Universal Licensing Archive System. 
## Built With
- Python 2.7
- Selenium 3.7.0
## Getting Started
### Preresquisites
- An IDE (Most Duke Students who have done CS101 and/or CS201 use Eclipse)
- Python 2.7 (Version used for CS101 @ Duke) 
- Selenium & Webdiver (i.e. Chrome, FireFox, Safari) extension
- xlrd (to read in data from excel spreadsheet database)
- xlwt (to generate excel spreadsheet output)
### Installing

#### Important Note
This webscraper was built using Python 2.7, which does not easily read unicode strings. At present, this webscraper is not able to scrape data for 1510 companies whose names have non-ascii characters. It might be better to switch to Python 3 which has more unicode support. 

[Key differences between Python 2.7 and Python 3](https://www.digitalocean.com/community/tutorials/python-2-vs-python-3-practical-considerations-2)
## Running the Web Scraper
```
chromedriver_path = '/Users/alethea/Documents/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path)
data = open_workbook('data.xlsx') 
```
