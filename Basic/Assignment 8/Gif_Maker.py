import os
import imageio

def Gif_Maker() :
    File_List = sorted(os.listdir("Pylearn7\Assignment 8\Images"))

    IMAGES = []
    for file_name in File_List:
        File_Path = "Pylearn7/Assignment 8/Images/" + file_name
        Image = imageio.v2.imread(File_Path)
        IMAGES.append(Image)

    imageio.mimsave("Pylearn7\Assignment 8\TheEarth.gif", IMAGES)

Gif_Maker()