##############################################################################################
#
#  Author  : Dave Bourbeau
#  Program : covid_scrape.py
#  Python  : Python3
#  Description : Gather Data from all files inside the data directory and
#                Plot onto a graph
##############################################################################################
import matplotlib.pyplot as plt
import os

path = "data/"
files = []

regions = ["Bas-Saint-Laurent"    , ""                     , "Capitale Nationale"     , "Mauricie - Centre du Québec", 
           "Estrie"               , "Montreal"             , "Outaouais"              , "                           ",
           ""                     , "Nord-du-Québec"       , ""                       , "Chaudiere-Appalaches"       ,
           "Laval"                , "Lanaudière"           , "Laurentides"            , "Montérégie"                 ,
           "Qebec Province"]

print("")
print("Which region of Quebec would you like to plot?")
print("")
print("   [01 - Bas-Saint-Laurent]")
print("   [03 - Capitale Nationale]")
print("   [04 - Mauricie - Centre du Québec]")
print("   [05 - Estrie]")
print("   [06 - Montréal]")
print("   [07 - Outaouais]")
print("   [10 - Nord-du-Québec]")
print("   [12 - Chaudière-Appalaches]")
print("   [13 - Laval]")
print("   [14 - Lanaudière]")
print("   [15 - Laurentides]")
print("   [16 - Montérégie]")
print("   [17 - Quebec Province]")
print("")

user_input = int(input('Select a number between 1 and 17 : '))

if (1 <= user_input <= 17):
	print("")
	print("You selected " + regions[user_input - 1])






# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
    	files.append(os.path.join(r, file))    # prints data/filename
#    	files.append(os.path.join(file))	   # prints filename

# List all files in the directory Data
for f in files:
    print(f)

# x = [1, 2, 3, 4, 5 , 6  , 7, 8, 9 ,10]
# y1 = [1, 2, 4, 8, 16, 32, 64, 128, 256,512]
# y2 = x = [1, 2, 3, 4, 5 , 6  , 7, 8, 9 ,10]
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.ylabel('some numbers')
# plt.show()

