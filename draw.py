from bs4 import BeautifulSoup as bs
import random, os
from cairosvg import svg2png
import imagedif
import shutil

def createPNG(name):
    file = open('startcircle.svg').read()

    soup = bs(file, 'xml')

    dimensions = soup.find("path")
    shape = dimensions['d']
    list_of_dimensions = shape.split(",")
    new_list_of_dimensions = []

    for dim in list_of_dimensions:
        items = dim.split(" ")
        new_items = []
        for item in items:
            if item.isalpha():
                new_items.append(item)
            else:
                di = float(item)
                dinum = di+random.uniform(0, 10)/random.uniform(0,10)
                new_items.append(str(dinum))
        listofDIMS = " ".join(new_items)
        new_list_of_dimensions.append(listofDIMS)

    reinsert = ",".join(new_list_of_dimensions)
    dimensions['d'] = reinsert

    save_this = str(soup)
    svg2png(bytestring=save_this,write_to=f"genimages/{name}.png")

max = 10000
count = 0
best_result = []
closest_score = 28563242999.0
while count < max:
    createPNG("X")
    save_path = f"genimages/X.png"
    try:
        result = imagedif.main("heart.png", save_path)
        mn_dist = float(result[0])
        count+=1
        if mn_dist < closest_score :
            closest_score = mn_dist
            best_result = [mn_dist, save_path]
            print(count, max-count, closest_score)
            try:
                shutil.move("genimages/X.png", "topimages/X.png")
            except Exception as ef:
                print(f"Tried to move file but: {ef}")
        else:
            continue
    except Exception as ee:
        print(ee)

print(best_result)


#SAVE SVG FILE
# with open('brand_new_image.svg','w') as outfile:
#     outfile.write(str(soup))



#USE PHASH TO DISCARD ANY IMAGES THAT ARE NOT CLOSER TO TARGET IMAGE THAN PREVIOUS ATTEMPTS



# digest1 = pHash.image_digest( 'file.1.jpg', 1.0, 1.0, 180 )
# digest2 = pHash.image_digest( 'file.2.jpg', 1.0, 1.0, 180 )
# print 'Cross-correelation: %d' % ( pHash.crosscorr( digest1, digest2 ) )
