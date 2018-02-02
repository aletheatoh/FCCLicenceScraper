# FCC Archive Webscraping
Code to webscrape data from the Federal Communications Commission (FCC)'s Universal Licensing Archive System. 
## Built With
- Python 2.7
- Selenium 3.7.0
## Getting Started
### Preresquisites
- Python 2.7 (Version used for CS101 @ Duke) 
- An IDE 
- Selenium & Webdiver (i.e. Chrome, FireFox, Safari) extension
- xlrd (to read in data from excel spreadsheet database)
- xlwt (to generate excel spreadsheet output)
#### Important Note
- This webscraper was built on a Mac OS X. If you're using another operating system, the Windows command line is different from that of terminal for Mac OS X. (Working on instructions for other operating systems and browsers)
- This webscraper was built using chromedriver. If you want to use a different browser you will need to install the appropriate webdriver extension. 
- This webscraper was built using Python 2.7, which does not easily read unicode strings. At present, this webscraper is not able to scrape data for 1510 companies whose names have non-ascii characters. It is recommended to explore if it is better to switch to Python 3 which has more unicode support. 
### Installing
Install the following:
- Python 2.7 (if you followed the Eclipse installation guide below you can skip this step)
  - Download from [python.org](https://www.python.org/downloads/) itself
  - Note that python comes pre-installed on Mac OS X
- IDE: 
  - [PyCharm](https://www.jetbrains.com/pycharm/)
  - [Eclipse](https://docs.google.com/document/d/1LgylwTTQiDQpF8kz0_L068G1jE8IYSIcQk-vlwcbUvU/edit) - installation guide for CS101
- Selenium, xlrd & xlwt
  - If you have already installed python or if you are using Mac OS X, it is easiest to use ```pip``` on the command line. 
  - First, open terminal and type ```python get-pip.py```
  - To install selenium type ```pip install selenium```. If it doesn't work, try ```sudo easy_install selenium ```
  - To install the xlrd & xlwt packages, type ```pip install xlrd``` and ```pip install xlwt```
  - You will have to manually install your webdriver extension. [This video](https://www.youtube.com/watch?v=XFVXaC41Xac) show you how to install and setup chromedriver on a Mac OS. 
  

Next, click on 'Clone or Download':
<p><img width="446" alt="screen shot 2018-02-02 at 7 59 23 pm" src="https://user-images.githubusercontent.com/22549537/35732222-99d93e68-0853-11e8-837e-82e40b77a0ba.png"></p>

If you're not familiar with Github and cloning repositories, you can simply click 'Download ZIP', unzip the folder, and open the **inner folder 'WebScraping' on your IDE**. Importantly, make sure that all the python modules are in the same directory on your IDE. 

## Running the Web Scraper
### Overview
#### Stating the file path
Basically, whenever you are opening a file, you need to reference the path of your directory. 
It is usually easiest if the file is in your current directory, as you simply have to state the file name, for example:
```
data = open_workbook('data.xlsx') 
```
If the file is located in another directory, you will need to state the file path, for example:
```
data = open_workbook('/Users/alethea/Documents/data.xlsx') 
```
However with chromedriver this is a little trickier. Chromedriver requires you to include the ChromeDriver location in your PATH environment variable:
```
chromedriver_path = '/Users/alethea/Documents/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path)
```
#### Code crashing?
Considering the fact that there are 4382 companies, you will mostly encounter TimeOutErrors. 
Fret not, the code has been designed such that in such an event, you can just run the code on companies you have not searched yet while retaining all previously scraped data. The code saves the output data spreadsheet each time it has successfully scraped data for one company. 
### What to amend in the code to work on your local environment
You only need to amend the following lines in **WebScraperMain.py**:
- Line 149: change ```chromedriver_path = '/Users/alethea/Documents/chromedriver'``` to state your ChromeDriver location
- Line 152: change ```data = open_workbook('data.xlsx')``` to state the file path of the excel workbook of licensees if it is not in your current directory
- Lines 70 & 183: change ```wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')``` to state which directory you want your data output to be located in. 
- Line 153: **state the file path of your output data in** ```visited_file = open_workbook('/Users/alethea/Documents/Spreadsheet_test.xls')``` **which is the same as the one stated in Lines 70 & 183**. This will make your life a lot easier in the event the code crashes.
**Finally, run WebScraperMain.py to scrape the data!**
