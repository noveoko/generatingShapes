from bs4 import BeautifulSoup as bs
import random, os
from cairosvg import svg2png
import imagedif
import shutil

#SETS UP YOUR CONSTANTS----------------------------
constants = [a.replace("\n", "") for a in open('constants.txt').readlines()]

nmax = int(constants[0].split(",")[-1])
startShape = constants[1].split(",")[-1]
generatedShape = constants[2].split(",")[-1]
targetShape = constants[3].split(",")[-1]
#End of constants set up --------------------------

#generates a single random SVG image by manipulating vertice values
def createPNG(fname=generatedShape+".png"):
    file = open(startShape).read()
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

    save_this = str(soup)
    #update the SVG file with new images
    fileName = f"genimages/x.svg"
    try:
        svg2png(bytestring=save_this,write_to=fileName)
    except Exception as ee:
        print(ee)

count = 0
best_result = []
closest_score = 28563242999.0
while count < nmax:
    createPNG()
    save_path = f"genimages/x.svg"
    try:
        result = imagedif.main(f"x.png", save_path)
        mn_dist = float(result[0])
        count+=1
        if mn_dist < closest_score :
            closest_score = mn_dist
            best_result = [mn_dist, save_path]
            print(count, nmax-count, closest_score)
            try:
                shutil.move("genimages/x.png", "topimages/x.png")
            except Exception as ef:
                print(f"Tried to move file but: {ef}")
        else:
            continue
    except Exception as ee:
        print("Line 68", ee)

print(best_result)
