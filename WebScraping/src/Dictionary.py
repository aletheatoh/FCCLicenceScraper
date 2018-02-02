'''
Created on 6 Nov 2017

@author: alethea
'''
import xlrd
from xlrd import open_workbook
import xlwt # to output data on excel spreadsheet 

wb = xlwt.Workbook(encoding="utf-8")
ws1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)  # sheet 1 contains all the webscraped data
from DictObject import yearEntry

totalDict = {} # dictionary: keys = all 18 years 1999-2016, values = dictionaries mapping subsidiaries to parent companies
subSet = set() # set of subsidiaries

done = False

def createDict(data):
    global done
    
    for sheet in data.sheets(): # year by year

        subToPar = {} # dictionary mapping subsidiaries (including parent company) to parent companies
        numRows = sheet.nrows # number of rows in each sheet
        
        for row in range(1, numRows): # skip header row
            parent = "" 
            for col in range(2): 
                if col == 0: # parent company col
                    parent = sheet.cell(row,col).value
                     
                    if parent == xlrd.empty_cell.value: 
                        done = True # done reading data in a sheet
                        break # breaks out of inner most loop
                     
                    parent = str(parent).strip()
                    if parent not in subToPar: # parent company not yet intialized in subToPar
                        subToPar[parent] = []
                        subToPar[parent].append(parent) # include parent company as subsidiary
                if col == 1: # subsidiary col      
                        # don't add subsidiary companies that have non-ascii characters   
                        try:
                            subToPar[parent].append(str(sheet.cell(row,col).value).strip()) # add subsidiary to list
                        except:
                            pass
                            
            if done == True: 
                done = False
                break
                         
        item = yearEntry(int(sheet.name), subToPar)

        totalDict[item.numYear] = item.subToPar # map subToPar dictionary to year

    for year, dict in totalDict.items():
        for k,v in dict.items():
            for sub in v:
                subSet.add(sub)
    return subSet
        
if __name__ == '__main__':
    data = open_workbook('data.xlsx')
    
    print createDict(data)
    print len(createDict(data))

    


