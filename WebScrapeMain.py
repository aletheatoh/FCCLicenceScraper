'''
Created on 6 Nov 2017

@author: alethea
'''

'''

UPDATES
- subSearch function works: able to successfully select all the required radio service code options + input subsidiary name + click search

TO NOTE: 
- Take into account header row
- Output into excel spreadsheet
- Take into account time needed to load webpage
- Check if empty
- Need to add track row number for each call sign in excel spreadsheet
- sub names as rows

'''
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

chromedriver_path = '/Users/alethea/Documents/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path)

url = 'http://wireless2.fcc.gov/UlsApp/LicArchive/searchArchive.jsp'
driver.get(url)

# helper function for scraping initial subsidiary data
def extractData():
    
    # TODO: MODIFY
    callsignID = driver.find_elements_by_xpath() # call sign/lease ID
    name = driver.find_elements_by_xpath() # names
    frn = driver.find_elements_by_xpath() # FRN
    radioService = driver.find_elements_by_xpath() # radio service
    status = driver.find_elements_by_xpath() # status
    version = driver.find_elements_by_xpath() # version
    lastActionDate = driver.find_elements_by_xpath() # last action date 
    # loop to add all to excel spreadsheet
    
    callsignIDCount = len(callsignID) # how many call sign IDs
    # after adding to spreadsheet
    
    # add counter for rownum
    for each in callsignID:
        # click call sign ID
        button = driver.find_element_by_css_selector()
        button.click()
        
        callSignData()
    
    # click next
    button = driver.find_element_by_css_selector()
    button.click()
    
    # if no next, click 'new search'
    button = driver.find_element_by_css_selector()
    button.click()

def subSearch(subsidiary):
    rsc = Select(driver.find_element_by_xpath("//select[@name='radioservicecode']"))
    # AH, AT, AW, CN, CW, CY, LD, SG, SL, SP, SY, TZ, WP, WU, WX, WY, WZ 
    rsc.select_by_value("AH")
    rsc.select_by_value("AT")
    rsc.select_by_value("AW")
    rsc.select_by_value("CN")
    rsc.select_by_value("CW")
    rsc.select_by_value("CY")
    rsc.select_by_value("LD")
    rsc.select_by_value("SG")
    rsc.select_by_value("SL")
    rsc.select_by_value("SP")
    rsc.select_by_value("SY")
    rsc.select_by_value("TZ")
    rsc.select_by_value("WP")
    rsc.select_by_value("WU")
    rsc.select_by_value("WX")
    rsc.select_by_value("WY")
    rsc.select_by_value("WZ")
    
    # fill out input name of subsidiary
    inputSub = driver.find_element_by_xpath("//input[@name='fiOwnerName']")
    inputSub.send_keys("hello") # input subsidiary
    
    # click search button
    search = driver.find_element_by_xpath("//input[@src='external/buttons/newsearch-blue.gif']")
    search.click()
    
    extractData() 

def callSignData(rowNum):
    # scrape market section
    market = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[8]/td[2]")
    submarket = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[9]/td[2]")
    
    # scrape dates section
    grant = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]")
    effective = driver.find_elements_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[2]")
    lastAction = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[13]/td[2]")
    expiration = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[4]")
    cancellation = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[4]")
    
    # scrape buildout deadlines
    firstBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[2]")
    secondBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[4]")
    
    # scrape licensee ID
    licenseeID = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[4]/td/table/tbody/tr[2]/td[2]")
    
    # click 'market' tab
    marketTab = driver.find_element_by_xpath("//a[@href='licenseMarketSum.jsp?licKey=5621871&amp;archive=Y']")
    marketTab.click()
    # NOTE: Market tab takes quite long to load
    
    # scrape auction data - just the text and not the link
    auction = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]")
    
    # go back to main tab
    driver.back() 
    
    # click 'return to results'
    returnToResults = driver.find_element_by_xpath("//a[@href='results.jsp?curPage=1&amp;reqPage=1&amp;licSearchKey=licSearcKey2017107176515']")
    returnToResults.click()
    
    
    
driver.quit()

