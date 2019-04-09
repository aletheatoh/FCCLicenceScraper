'''
Created on 1 Feb 2018

@author: alethea

This is a helper function to scrape data for subsidiaries with termination pending statuses


'''

def tp_status(driver, ws1, rowNum, colNum):
    print "tp status"

    cs_or_lease = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[1]/td[1]")
    cs_or_lease_id = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[1]/td[2]")
    ws1.row(rowNum).write(1, 'TP status' + " " + cs_or_lease.text.strip() + ": " + cs_or_lease_id.text.strip())

    market = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[8]/td[2]")
    ws1.row(rowNum).write(colNum, market.text.strip())
    submarket = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[9]/td[2]")
    ws1.row(rowNum).write(colNum+1, submarket.text.strip())
    channelBlock = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[8]/td[4]")
    ws1.row(rowNum).write(colNum+2, channelBlock.text.strip())
    associatedFreq = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[9]/td[4]")
    ws1.row(rowNum).write(colNum+3, associatedFreq.text.strip())
#     wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')

    # scrape dates section
    grant = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[11]/td[2]")
    ws1.row(rowNum).write(colNum+4, grant.text.strip())
    effective = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[12]/td[2]")
    ws1.row(rowNum).write(colNum+5, effective.text.strip())
    expiration = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[11]/td[4]")
    ws1.row(rowNum).write(colNum+6, expiration.text.strip())
    cancellation = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[12]/td[4]")
    ws1.row(rowNum).write(colNum+7, cancellation.text.strip())

    # scrape buildout deadlines
    firstBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[15]/td[2]")
    ws1.row(rowNum).write(colNum+8, firstBD.text.strip())
    secondBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[3]/td/table/tbody/tr[15]/td[4]")
    ws1.row(rowNum).write(colNum+9, secondBD.text.strip())
#     wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')

    # scrape licensee ID
    licenseeID = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[5]/td/table/tbody/tr[2]/td[2]")
    ws1.row(rowNum).write(colNum+10, licenseeID.text.strip())
#     wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')

    # click 'market' tab
    marketTab = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[1]/tbody/tr[2]/td/a[2]")
    marketTab.click()
    # NOTE: Market tab takes quite long to load

    # scrape auction data - just the text and not the link
    auction = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[5]/td[2]")
    ws1.row(rowNum).write(colNum+11, auction.text.strip())
#     wb.save('/Users/alethea/Downloads/Spreadsheet_test.xls')

    print "CS or lease: " + cs_or_lease.text.strip()
    print "CS or lease Id: " + cs_or_lease_id.text.strip()
    print "Market: " + market.text.strip()
    print "Submarket: " + submarket.text.strip()
    print "Channelblock: " + channelBlock.text.strip()
    print "Associated Frequency: " + associatedFreq.text.strip()
    print "Grant: " + grant.text.strip()
    print "Effective: " + effective.text.strip()
    print "Expiration: " + expiration.text.strip()
    print "Cancellation: " + cancellation.text.strip()
    print "First BD: " + firstBD.text.strip()
    print "Second BD: " + secondBD.text.strip()
    print "Auction: " + auction.text.strip()
