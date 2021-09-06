import csv
import os
from pandas_ods_reader import read_ods as reader
from PIL import Image

questions = reader("/home/abdullah/Desktop/image_generation/Paper_Meta_data.ods")
database = reader("/home/abdullah/Desktop/image_generation/MD_Ready.ods")
images = os.listdir("/home/abdullah/Desktop/image_generation/dataset/")





for image in images:
    im = Image.open("/home/abdullah/Desktop/image_generation/dataset/" + image)
    im.show()

    features = []
    file = open('s.csv', 'a',encoding='UTF8')
    writer = csv.writer(file)
    features.append(image)
    for question in questions.columns:
        print("What is the [" + question + "] as shown in the image? \n ")
        print("answer must be one of the following:\n")
        print(questions[question].all())
        answer = input("--->")
        features.append(answer)
        print("---------------------------\n\n\n\n\n")
    writer.writerow(features)
    file.close()
    im.save("/home/abdullah/Desktop/image_generation/labeled_data/"+image)
    os.system("rm "+"/home/abdullah/Desktop/image_generation/dataset/" + image)
    break


