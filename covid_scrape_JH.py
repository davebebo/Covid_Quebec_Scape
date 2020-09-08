##############################################################################################
#
#  Author  : Dave Bourbeau
#  Program : covid_scrape.py
#  Python  : Python3
#  Description : This program scrapes the Quebec government Website for the current case
#                of covid cases in each region display and stores it in a text file daily
##############################################################################################
import requests
import datetime
from bs4 import BeautifulSoup

# Global local variables
first_table_elem = 0
i=0
table = []

#Create a Request object of the website
#URL = 'https://www.quebec.ca/en/health/health-issues/a-z/2019-coronavirus/'
URL = 'https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6'
page = requests.get(URL)

#Get current date, and create text file with date appended
today = datetime.datetime.now()
filename = "data_JH/Covid_data_QC_" + today.strftime("%Y") + "_" + today.strftime("%m") + "_" + today.strftime("%d")
file = open(filename, "w+")

#Create beautiful soup object from the page request for easy filtering of HTML
soup = BeautifulSoup(page.content, 'html.parser')

#Gather all text in the Table field of the website and enter into a list
results = soup.findAll("div", {"class": "overflow-hidden text-ellipsis padding-left-quarter avenir-bold"})

print(results)
for p in results:
    table.append(p.text)

table_len = len(table)

#Filter trough elements of table and output everything after Mauricie, formated to text file
while i < table_len - 1:
#	if "Mauricie" in table[i]:
	if "01 - " in table[i]:
		first_table_elem = 1
	if first_table_elem == 1:
		print("[",table[i],"] ","[", table[i+1],"] ")
		text = "[" +table[i]+ "] " + "[" + table[i+1] + "] " + "\n"
		file.write(text)
		i = i+2
	else:
		i = i+1
