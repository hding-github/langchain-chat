import requests
#pip install beautifulsoup4pip install beautifulsoup4
# from bs4 import BeautifulSoup
# import pandas as pd

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}




import pandas
strURL = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
strURL = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"


def get_table(strURL):
    #tables_on_page = pandas.read_html("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    tables_on_page = pandas.read_html(strURL, encoding='utf-8')

    table = tables_on_page[0]
    table.to_json("table.json", index=False, orient='table')
    tTable = table.values
    
    return tTable

def get_max(tStr,tMax):
    tInt = 0
    try:
        tInt = int(tStr)
    except ValueError:
        # Handle the exception
        print('Error: Unable to read x or y from the string.')

    if tInt>tMax:
            tMax = tInt
    return tMax

def get_dictionary(tTable):
    tMaxX = 0
    tMaxY = 0
    tD = {}
    tNumOfRows = len(tTable)
    tLargestNumOfRows = 0
    for i in range(1, tNumOfRows):
        tStrY = tTable[i][2]
        tStrX = tTable[i][0]
        tStrC = tTable[i][1]

        tMaxX = get_max(tStrX, tMaxX)
        tMaxY = get_max(tStrY, tMaxY)
        
        if tStrY not in tD:
            tD[tStrY] = {}
        if tStrX not in tD[tStrY]:
            tD[tStrY][tStrX] = tStrC
        else:
            print("Duplicated locations")
        tD["max_x"] = tMaxX
        tD["max_y"] = tMaxY
    return tD

def print_dictionary(tD):
    tMaxX=tD["max_x"]
    tMaxY=tD["max_y"]

    for i in range(tMaxY+1):
        intY = tMaxY-i
        tStrRow = ""
        for j in range(tMaxX+1):
            tChar = " "
            strX = str(j)
            strY = str(intY)
            if strY in tD:
                if strX in tD[strY]:
                    tChar = tD[strY][strX]
            tStrRow = tStrRow + tChar
        print(tStrRow)

def print_secrets(strURL):
    tTable = get_table(strURL)
    tD = get_dictionary(tTable)
    print_dictionary(tD)

print_secrets(strURL)
print("Completed")