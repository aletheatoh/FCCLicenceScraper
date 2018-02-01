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

### Important Note
At present, this webscraper is not able to scrape data for 1510 companies whose names have non-ascii characters. This webscraper was built using Python 2.7, which does not easily read unicode strings. It might be better to switch to Python 3, whose default encoding is UTF-8. 
