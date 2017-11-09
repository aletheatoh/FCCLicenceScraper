'''
Created on 8 Nov 2017

@author: alethea
'''

from Dictionary import createDict
from xlrd import open_workbook

from DictObject import yearEntry

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import xlwt
wb = xlwt.Workbook(encoding="utf-8")
ws1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True)
    
rowTracker = 1

def extractData():
    global rowTracker

    # number of rows = number of call sign/lease IDs: -2 from row_count two remove header/footer rows
    row_count = len(driver.find_elements_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[1]/tbody[1]/tr")) - 2
    
    # number of cols - need to use tr[2<=x<=row_count-1] and not header row, and -1 to remove row number
#     col_count = len(driver.find_elements_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[1]/tbody[1]/tr[2]/td")) - 1
#     
    # loop works, now just need to 
    for numR in range(2,row_count+2):
        row = driver.find_elements_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[1]/tbody[1]/tr[" + str(numR) + "]/td")
        numC = 0
        for value in row:
            if numC > 0:
                ws1.row(rowTracker).write(numC, value.text)
            numC += 1
    
        callSignDataButton = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[1]/tbody/tr[" + str(numR) + "]/td[2]/a")
        callSignDataButton.click()  

        callSignData(rowTracker,numC)
        
        rowTracker += 1
    
    try:
        nextPage = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[2]/tbody/tr/td/table/tbody/tr/td[3]/a")
        nextPage.click()
        extractData() # recursive function
    except:
        pass

def callSignData(rowNum,colNum):
    # scrape market section
    market = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[8]/td[2]")
    ws1.row(rowNum).write(colNum, market.text)
    submarket = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[9]/td[2]")
    ws1.row(rowNum).write(colNum+1, submarket.text)
        
    # scrape dates section
    grant = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]")
    ws1.row(rowNum).write(colNum+2, grant.text)
    effective = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[2]")
    ws1.row(rowNum).write(colNum+3, effective.text)
    lastAction = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[13]/td[2]")
    ws1.row(rowNum).write(colNum+4, lastAction.text)
    expiration = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[4]")
    ws1.row(rowNum).write(colNum+5, expiration.text)
    cancellation = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[4]")
    ws1.row(rowNum).write(colNum+6, cancellation.text)
        
    # scrape buildout deadlines
    firstBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[2]")
    ws1.row(rowNum).write(colNum+7, firstBD.text)
    secondBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[4]")
    ws1.row(rowNum).write(colNum+8, secondBD.text)
        
    # scrape licensee ID
    licenseeID = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[4]/td/table/tbody/tr[2]/td[2]") 
    ws1.row(rowNum).write(colNum+9, licenseeID.text)
        
    # click 'market' tab
    marketTab = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[1]/tbody/tr[2]/td/a[2]")
    marketTab.click()
    # NOTE: Market tab takes quite long to load
    
    # scrape auction data - just the text and not the link
    auction = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]")
    ws1.row(rowNum).write(colNum+10, auction.text)
    
    # return to results    
    returnToResults = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/span[3]/a[2]")
    returnToResults.click()

def subSearch(sub):
    
    # update rows
    rowTracker = 1
    
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
    inputSub.send_keys(sub) # input subsidiary
    
    # click search button
    search = driver.find_element_by_xpath("//input[@src='external/buttons/newsearch-blue.gif']")
    search.click()
    
    extractData()
    
    # go back to new search
    newSearch = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/span[1]/a[2]")
    newSearch.click()

if __name__ == '__main__':
    chromedriver_path = '/Users/alethea/Documents/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    data = open_workbook('web-scraping.xlsx')
       
    url = 'http://wireless2.fcc.gov/UlsApp/LicArchive/searchArchive.jsp'
    driver.get(url)
    
    headerRow = ["Call Sign/Lease ID", "Name", "FRN", "Radio Service", "Status", "Version", "Last Action Date", "Market", "Submarket", "Channel Block", "Associated Frequencies (MHz)", "Grant", "Effective", "Expiration", "Cancellation", "1st Buildout Deadline", "2nd Buildout Deadline", "Licensee ID", "Auction"]
    for i in range(1,20):
        ws1.row(0).write(i, headerRow[i-1])
    
    for subsidiary in createDict(data):
        subSearch(subsidiary)
    
    wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')
    
    
