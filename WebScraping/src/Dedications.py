'''
Created on 17 Nov 2017

@author: alethea
'''
from xlrd import open_workbook
import xlrd

done = False
def create(data):
    global done
    dict = {}
    
    for sheet in data.sheets(): # year by year

        numRows = sheet.nrows # number of rows in each sheet
        
        for row in range(0, numRows): # skip header row
            for col in range(2): 
                if col == 0: # parent company col
                    person = sheet.cell(row,col).value
                    
                    if person == xlrd.empty_cell.value: 
                        done = True # done reading data in a sheet
                        break # breaks out of inner most loop
                     
                    person = str(person).strip()
                    if person not in dict: 
                        dict[person] = []

                if col == 1:     
                        message = str(sheet.cell(row,col).value).strip()
                        dict[person].append(message)
                     
            if done == True: 
                done = False
                break

    return dict
            
if __name__ == '__main__':
    data = open_workbook('/Users/alethea/Desktop/Dedications.xlsx')
#     for k,v in create(data).items():
#         print k,v
    print create(data)