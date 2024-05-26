#### MohammadAli Mirzaei ####

import os  # Importing the 'os' module to interact with the operating system
import imageio  # Importing the 'imageio' library for working with images and creating GIFs

def Gif_Maker():
    # Retrieving a sorted list of files in the specified directory
    File_List = sorted(os.listdir("Translator\Images"))

    IMAGES = []  # Initializing an empty list to store image data

    # Iterating through each file in the sorted list
    for file_name in File_List:
        # Constructing the full path of the image file
        File_Path = "Translator\Images" + file_name
        # Reading the image file and storing its data
        Image = imageio.v2.imread(File_Path)
        # Appending the image data to the list of images
        IMAGES.append(Image)

    # Saving the list of images as a GIF file
    imageio.mimsave("Translator\Images", IMAGES)

# Calling the Gif_Maker function to create the GIF
Gif_Maker()
