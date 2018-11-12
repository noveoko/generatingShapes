from bs4 import BeautifulSoup as bs
import random

file = open("startcircle.svg").read()
soup = bs(file, 'lxml')
dimensions = soup.find("path")
shape = dimensions['d']
list_of_dimensions = shape.split(",")
new_list_of_dimensions = []
#iterate through all of the `verticies` in the .svg file
for dim in list_of_dimensions:
    items = dim.split(" ")
    new_items = []
    for item in items:
        if item.isalpha():
            new_items.append(item)
        else:
            di = float(item)
            #changes the value of a single veritce at a time
            dinum = di+random.uniform(0, 10)/random.uniform(0,10)
            new_items.append(str(dinum))
    listofDIMS = " ".join(new_items)
    new_list_of_dimensions.append(listofDIMS)

reinsert = ",".join(new_list_of_dimensions)
dimensions['d'] = reinsert
