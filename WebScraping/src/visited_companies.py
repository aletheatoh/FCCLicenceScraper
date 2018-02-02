'''
Created on 6 Nov 2017

@author: alethea
'''

from xlrd import open_workbook
import xlrd

visited_companies = set()  # set of subsidiaries

def visited(data):

    sheet_num = 1
    for sheet in data.sheets():  # year by year
        
        numRows = sheet.nrows  # number of rows in each sheet
   
        for row in range(1, numRows):  # skip header row
            col = 0
            if sheet_num == 2: col = 1
            company = sheet.cell(row, col).value
            if company == xlrd.empty_cell.value: 
                # done reading data in a sheet
                break 
        
            visited_companies.add(str(company).strip())
        
        sheet_num += 1
    return visited_companies
      
if __name__ == '__main__':
    data = open_workbook('Results_So_Far.xlsx')
    print visited(data)
    print len(visited(data))

