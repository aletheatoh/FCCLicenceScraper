'''
Created on 8 Nov 2017

@author: alethea
'''


'''
1) Import packages
'''
from xlrd import open_workbook # to read in data from excel spreadsheet database
import xlwt # to output data on excel spreadsheet 
from selenium import webdriver
from selenium.webdriver.support.ui import Select

'''
2) Import helper functions from other python modules
'''
from Dictionary import createDict
from Visited import visited
from tp_status import tp_status # to scrape data for companies with tp status
from lease_id import lease_id # to scrape data for companies with lease ID
from call_sign import call_sign # to scrape data for companies with call sign

'''
3) Create the excel spreadsheet to output data 
'''
wb = xlwt.Workbook(encoding="utf-8")
ws1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)  # sheet 1 contains all the webscraped data
ws2 = wb.add_sheet('Sheet 2', cell_overwrite_ok=True)  # sheet 2 contains two list of subsidiary companies: 1) returned results 2) did not return results

# write the header row in bold font
font = xlwt.Font()
font.bold = True
style = xlwt.XFStyle() 
style.font = font 
    
# create header row in spreadsheet
headerRow = ["Subsidiary", "Call Sign/Lease ID", "Name", "FRN", "Radio Service", "Status", "Version", "Last Action Date", "Market", "Submarket", "Channel Block", "Associated Frequencies (MHz)", "Grant", "Effective", "Expiration", "Cancellation", "1st Buildout Deadline", "2nd Buildout Deadline", "Licensee ID", "Auction"]
for i in range(0, len(headerRow)):
    ws1.row(0).write(i, headerRow[i], style)
          
ws2.row(0).write(0, "Returned Results", style)
ws2.row(0).write(1, "No Results", style)

'''
4) Initialize global variable
'''

rowTracker = 1  # to track row in excel spreadsheet
subTracker = ""  # to track subsidiary we are currently searching

subsWithResults = set([])  # set of subsidiaries that are returning results

row_noResults = 1

def extractData(sub):
    global rowTracker
    global subTracker
    global row_noResults
    
    subTracker = sub # update global var
    
    # number of rows = number of call sign/lease IDs: -2 from row_count two remove header/footer rows
    row_count = len(driver.find_elements_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[1]/tbody[1]/tr")) - 2
    
    # no search results
    if row_count + 2 == 0:  
        ws2.row(row_noResults).write(1, sub)
        row_noResults += 1
        wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')
        
    # row num needs to start from 2 to exclude header row, and write subsidiary name in col 0
    for numR in range(2, row_count + 2):
        row = driver.find_elements_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[1]/tbody[1]/tr[" + str(numR) + "]/td")
        numC = 0
        for value in row:
            if numC == 0:
                ws1.row(rowTracker).write(numC, sub)
                subsWithResults.add(sub)  # keep adding subsidiaries that return results to set
            elif numC > 0:
                ws1.row(rowTracker).write(numC, value.text.strip())
            wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')
            numC += 1
            
        callSignDataButton = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[1]/tbody/tr[" + str(numR) + "]/td[2]/a")
        callSignDataButton.click()  
         
        callSignData(rowTracker, numC)
        wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')
        
        rowTracker += 1
        
    try:  # recursive function 
        nextPage = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table/tbody/tr[5]/td/table[2]/tbody/tr/td/table/tbody/tr/td[3]/a")
        nextPage.click()
        extractData(sub) 
    except:
        pass
    
def callSignData(rowNum, colNum):
    try:
        # need to determine if call sign or component(s) of call sign is in termination pending status
        tp = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]")
        if tp.text.strip() == "This call sign or a component(s) of this call sign is in termination pending status for failure to meet the buildout requirement.":
            # call sign or component(s) of call sign is in tp status
            tp_status(driver, ws1, rowNum, colNum) # imported from tp_status.py
        
        else:  # next determine if call sign or lease ID
            license_details = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[1]/tbody/tr[2]/td/a[1]")
          
            # lease ID
            if license_details.text.strip() == "License Details": 
                lease_id(driver, ws1, rowNum, colNum) # imported from lease_id.py
                
            else:
                # call sign
                call_sign(driver, ws1, rowNum, colNum) # imported from call_sign.py
        
        # return to results    
        returnToResults = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/span[3]/a[2]")
        returnToResults.click()
        
    except:
        pass   
         
def subSearch(sub): 
    # click the required radio service code options
    rsc = Select(driver.find_element_by_xpath("//select[@name='radioservicecode']"))
    radioServiceCodes = ["AH", "AT", "AW", "CN", "CW", "CY", "LD", "SG", "SL", "SP", "SY", "TZ", "WP", "WU", "WX", "WY", "WZ"] 
    for value in radioServiceCodes:
        rsc.select_by_value(value)
    
    # fill out input name of subsidiary
    inputSub = driver.find_element_by_xpath("//input[@name='fiOwnerName']")
    inputSub.send_keys(sub)  # input subsidiary
    
    # click search button
    search = driver.find_element_by_xpath("//input[@src='external/buttons/newsearch-blue.gif']")
    search.click()
    
    # start web scraping the subsidiary data
    extractData(sub)
    
    # go back to new search
    newSearch = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td/span[1]/a[2]")
    newSearch.click()

if __name__ == '__main__':
    chromedriver_path = '/Users/alethea/Documents/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    data = open_workbook('data.xlsx')  
    
    visited_file = open_workbook('Results_So_Far.xlsx') 
    
    url = 'http://wireless2.fcc.gov/UlsApp/LicArchive/searchArchive.jsp'
    driver.get(url)

    '''
    4 test cases:
    1) 'Pegasus Guard' - typical subsidiary with call sign, average-size output 
    * note that it is NOT in the prescribed lists of companies!
    2) 'T-Mobile License LLC' - typical subsidiary with call sign, much bigger output
    3) 'NEXTEL WEST CORP' - subsidiary has call signs with TP status
    4) 'MetroPCS AWS, LLC' - subsidiary has lease ID
    '''
    # 1) test case - average subsidiary
#     subSearch("Pegasus Guard")
    
    # 2) test case - large output
#     subSearch("T-Mobile License LLC")

    # 2) test case - TP status
#     subSearch("NEXTEL WEST CORP")

    # 4) test case - lease ID
#     subSearch("MetroPCS AWS, LLC")

#     companies_left = createDict(data) - visited(visited_file)

    # actual implementation: createDict(data) returns a set of all the subsidiary companies (so this removes duplicates)
    for subsidiary in createDict(data):
        subSearch(subsidiary)
    wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')

#     subsWithResults = subsWithResults.union(visited(visited_file))
    
#     idx1 = 1
#     for sub in subsWithResults:
#         ws2.row(idx1).write(0, sub)
#         idx1+=1
    
    wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')
    
    driver.quit()
