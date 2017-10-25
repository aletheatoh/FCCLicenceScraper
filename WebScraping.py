'''
Created on 24 Oct 2017

@author: alethea
'''
from xlrd import open_workbook
import xlrd

totalDict = {} # dictionary: keys = years 1999-2016, values = dictionaries mapping subsidiaries to parent companies

class yearEntry(object):
    
    # constructor to create each year and its value (dict of subsidiaries mapped to parent company) as an object
    def __init__(self, numYear, subToPar):
            self.numYear = numYear
            self.subToPar = subToPar

data = open_workbook('web-scraping.xlsx')

for sheet in data.sheets(): # year by year
    subToPar = {} # dictionary mapping subsidiaries (including parent company) to parent companies
    numRows = sheet.nrows # number of rows in each sheet
    for row in range(1, numRows): # skip header row
        parent = "" 
        for col in range(2): 
            if col == 0: # parent company col
                parent = sheet.cell(row,col).value
                if parent != xlrd.empty_cell.value: # so that we don't add empty cells to the dict
                    parent = str(parent)
                    if parent not in subToPar: # parent company not yet intialized in subToPar
                        subToPar[parent] = []
                        subToPar[parent].append(parent) # include parent company as subsidiary
            if col == 1: # subsidiary col
                if parent != xlrd.empty_cell.value: # so that we don't add empty cells to the dict
                    parent = str(parent)
                    subToPar[parent].append(sheet.cell(row,col).value) # add subsidiary to list
                    
    item = yearEntry(int(sheet.name), subToPar)
    totalDict[item.numYear] = item.subToPar # map subToPar dictionary to year
        
for line in totalDict.iteritems():
    print line

        