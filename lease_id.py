'''
Created on 1 Feb 2018

@author: alethea

This is a helper function to scrape data for subsidiaries with lease IDs

'''

def lease_id(driver, ws1, rowNum, colNum):
    print "lease id"

    cs_or_lease = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]")
    print "CS or lease: " + cs_or_lease.text.strip()

    cs_or_lease_id = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]")
    print "CS or lease Id: " + cs_or_lease_id.text.strip()
    ws1.row(rowNum).write(1, cs_or_lease.text.strip() + ": " + cs_or_lease_id.text.strip())

    # scrape dates section
    grant = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td/table/tbody/tr[5]/td[2]")
    print "Grant: " + grant.text.strip()
    ws1.row(rowNum).write(colNum+4, grant.text.strip())

    effective = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td/table/tbody/tr[6]/td[2]")
    print "Effective: " + effective.text.strip()
    ws1.row(rowNum).write(colNum+5, effective.text.strip())

    expiration = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td/table/tbody/tr[5]/td[4]")
    print "Expiration: " + expiration.text.strip()
    ws1.row(rowNum).write(colNum+6, expiration.text.strip())

    cancellation = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td/table/tbody/tr[6]/td[4]")
    print "Cancellation: " + cancellation.text.strip()
    ws1.row(rowNum).write(colNum+7, cancellation.text.strip())

    # go to market tab
    marketTab = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/a[2]")
    marketTab.click()

    market = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td[1]/table[1]/tbody/tr[4]/td[2]")
    print "Market: " + market.text.strip()
    ws1.row(rowNum).write(colNum, market.text.strip())

    submarket = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td[1]/table[1]/tbody/tr[5]/td[2]")
    print "Submarket: " + submarket.text.strip()
    ws1.row(rowNum).write(colNum+1, submarket.text.strip())

    channelBlock = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td[1]/table[1]/tbody/tr[4]/td[4]")
    print "Channelblock: " + channelBlock.text.strip()
    ws1.row(rowNum).write(colNum+2, channelBlock.text.strip())

    associatedFreq = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td[1]/table[1]/tbody/tr[5]/td[4]")
    print "Associated Frequency: " + associatedFreq.text.strip()
    ws1.row(rowNum).write(colNum+3, associatedFreq.text.strip())

    auction = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[3]/tbody/tr[2]/td[1]/table[1]/tbody/tr[6]/td[2]")

    print "Auction: " + auction.text.strip()
    ws1.row(rowNum).write(colNum+11, auction.text.strip())
