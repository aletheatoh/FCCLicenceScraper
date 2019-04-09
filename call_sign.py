'''
Created on 1 Feb 2018

@author: alethea

This is a helper function to scrape data for subsidiaries with only call signs


'''
def call_sign(driver, ws1, rowNum, colNum):
    print "call sign"
    print "im here 12"
    cs_or_lease = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]")
    print "CS or lease: " + cs_or_lease.text.strip()
    cs_or_lease_id = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]")
    ws1.row(rowNum).write(1, cs_or_lease.text.strip() + ": " + cs_or_lease_id.text.strip())
    print "CS or lease id: " + cs_or_lease_id.text.strip()
    # scrape market section
    # market = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[8]/td[2]")
    market = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]")
    print "Market: " + market.text.strip()
    ws1.row(rowNum).write(colNum, market.text.strip())
    # submarket = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[9]/td[2]")
    submarket = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[2]")
    print "Submarket: " + submarket.text.strip()
    ws1.row(rowNum).write(colNum+1, submarket.text.strip())
    # channelBlock = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[8]/td[4]")
    channelBlock = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[4]")
    print "Channelblock: " + channelBlock.text.strip()
    ws1.row(rowNum).write(colNum+2, channelBlock.text.strip())
    # associatedFreq = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[9]/td[4]")
    associatedFreq = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[4]")
    print "Associated Frequency: " + associatedFreq.text.strip()
    ws1.row(rowNum).write(colNum+3, associatedFreq.text.strip())

    # scrape dates section
    # grant = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]")
    grant = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[14]/td[2]")
    print "Grant: " + grant.text.strip()
    ws1.row(rowNum).write(colNum+4, grant.text.strip())
    # effective = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[2]")
    effective = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[2]")
    print "Effective: " + effective.text.strip()
    ws1.row(rowNum).write(colNum+5, effective.text.strip())
    # expiration = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[4]")
    expiration = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[14]/td[4]")
    print "Expiration: " + expiration.text.strip()
    ws1.row(rowNum).write(colNum+6, expiration.text.strip())
    # cancellation = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[12]/td[4]")
    cancellation = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[4]")
    print "Cancellation: " + cancellation.text.strip()
    ws1.row(rowNum).write(colNum+7, cancellation.text.strip())

    # scrape buildout deadlines
    # firstBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[2]")
    firstBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[18]/td[2]")
    print "First BD: " + firstBD.text.strip()
    ws1.row(rowNum).write(colNum+8, firstBD.text.strip())
    # secondBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[15]/td[4]")
    secondBD = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[18]/td[4]")
    print "Second BD: " + secondBD.text.strip()
    ws1.row(rowNum).write(colNum+9, secondBD.text.strip())

    # scrape licensee ID
    licenseeID = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[4]/td/table/tbody/tr[2]/td[2]")
    print "Licensee ID: " + licenseeID.text.strip()
    ws1.row(rowNum).write(colNum+10, licenseeID.text.strip())

    # click 'market' tab
    marketTab = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[1]/tbody/tr[2]/td/a[2]")
    marketTab.click()
    # NOTE: Market tab takes quite long to load

    # scrape auction data - just the text and not the link
    auction = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]")
    print "Auction: " + auction.text.strip()
    ws1.row(rowNum).write(colNum+11, auction.text.strip())
