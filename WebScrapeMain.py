'''
Created on 6 Nov 2017

@author: alethea
'''

'''
TO NOTE: 
- Take into account header row
- Output into excel spreadsheet
- Take into account time needed to load webpage
- Check if empty

'''
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'http://wireless2.fcc.gov/UlsApp/LicArchive/searchArchive.jsp'
driver = webdriver.Chrome()
driver.get(link)

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
    rsc = driver.find_element_by_id("//select[@name='radioservicecode']")
    all_options = rsc.find_elements_by_tag_name('option') # all radio service code options

    # create a set with all radio service code we need to select     
    # AH, AT, AW, CN, CW, CY, LD, SG, SL, SP, SY, TZ, WP, WU, WX, WY, WZ  
    rscSet = set([])
    rscSet.add('AH - AWS-H Block (at 1915-1920 MHz and 1995-2000 MHz)')
    rscSet.add('AT - AWS-3 (1695-1710 MHz, 1755-1780 MHz, and 2155-2180 MHz)')
    rscSet.add('AW - AWS (1710-1755 MHz and 2110-2155 MHz)')
    rscSet.add('CN - PCS Narrowband')
    rscSet.add('CW - PCS Broadband')
    rscSet.add('CY - 1910-1915/1990-1995 MHz Bands, Market Area')
    rscSet.add('LD - Local Multipoint Distribution Service')
    rscSet.add('SG - Conventional Public Safety 700 MHz')
    rscSet.add('SL - Public Safety 700 MHZ Band-State License')
    rscSet.add('SP - 700 MHz Public Safety Broadband Nationwide License')
    rscSet.add('SY - Trunked Public Safety 700 MHz')
    rscSet.add('TZ - 24 GHz Service')
    rscSet.add('WP - 700 MHz Upper Band (Block D)')
    rscSet.add('WU - 700 MHz Upper Band (Block C)')
    rscSet.add('WX - 700 MHz Guard Band')
    rscSet.add('WY - 700 MHz Lower Band (Blocks A, B & E)')
    rscSet.add('WZ - 700 MHz Lower Band (Blocks C, D)')
    
    for option in all_options:
        if option.text in rscSet: 
            option.click() # select() in earlier versions of webdriver
            
    # fill out input - input subName
    inputSub = driver.find_element_by_xpath("//input[@name='fiOwnerName']")
    inputSub.send_keys(subsidiary) # input subsidiary
    
    # click 'Search'
    search = driver.find_element_by_xpath("//input[@src='external/buttons/newsearch-blue.gif']")
    # or should we use button = driver.find_element_by_css_selector() ?
    search.click()
    
    extractData() 

def callSignData():
    # market, dates, and buildout deadlines scrape data
    
    # market section
    market = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[8]/td[2]")
    submarket = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[9]/td[2]")
    
    # dates section
    grant = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]")
    effective = driver.find_elements_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[2]")
    lastAction = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[13]/td[2]")
    expiration = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[4]")
    cancellation = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[4]")
    
    # buildout deadlines
    firstBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[2]")
    secondBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[4]")
    
    # licensee ID
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

