##### MohammadAli Mirzaei #####


from media import *  # Import all classes and functions from the media module
import actor  # Import the actor module
import clip  # Import the clip module
import documentary  # Import the documentary module
import film  # Import the film module
import series  # Import the series module

class Database:
    
    def read(self):
        # Open the database file in read mode
        data = open("Store-Class\database.txt", "r")
        # Iterate through each line in the file
        for line in data:
            # Split the line into individual details using comma as delimiter
            detail = line.split(",")
            # Create a new Media object using the details read from the file
            my_obj = Media(
                detail[0],
                detail[1],
                detail[2],
                detail[3],
                detail[4],
                detail[5],
                detail[6],
            )
            # Append the newly created Media object to the MEDIA list
            MEDIA.append(my_obj)
        # Close the file
        data.close()

    def write(self):
        # Open the database file in write mode
        data = open("Pylearn7\Assignment 12\database.txt", "w")
        # Iterate through each object in the MEDIA list
        for obj in MEDIA:
            # Format the object details into a string
            result = f"{obj.type},{obj.name},{obj.director},{obj.imdb_score},{obj.url},{obj.duration},{obj.casts}"
            # Write the formatted string to the file
            data.write(result)

class Store:

    @staticmethod
    def show_menu():
        # Display the store menu options
        print("1- Add")
        print("2- Edit")
        print("3- Remove")
        print("4- Search")
        print("5- Show List")
        print("6- Show Info")
        print("7- Download")
        print("8- Exit")

    @staticmethod
    def add():
        # Get input from user to add a new media
        type = input("Enter media type: ")
        name = input("Enter media name: ")
        director = input("Enter director name: ")
        imdb_score = input("Enter imdb score: ")
        url = input("Enter url address: ")
        duration = input("Enter duration time: ")
        casts = input("Enter casts list: ")
        # Create a new Media object with user input
        new_media = Media(type, name, director, imdb_score, url, duration, casts)
        # Append the new Media object to the MEDIA list
        MEDIA.append(new_media)
        print("New media add to list successfully")

    def edit(self, old_name, new_name):
        # Edit the name of a media
        for obj in MEDIA:
            if obj.name == old_name:
                obj.name = new_name
                print('Media edited successfully') 
                break   
        else:
            print('Media Not found...!')    

    def remove(self, media_name):
        # Remove a media from the list
        i = 0
        for obj in MEDIA:
            if obj.name == media_name:
                MEDIA.pop(i)
                print("Media Remove successfully")
                break
            else:
                i += 1
        else:
            print("Media not found...!")

    def search(self, media_name):
        # Search for a media in the list
        for obj in MEDIA:
            if media_name in obj.name:
                # Print details of the found media
                print(
                    f"type: {obj.type}\nname: {obj.name}\nDirector: {obj.director}\nImdb_score: {obj.imdb_score}\nUrl: {obj.url}\nDuration: {obj.duration}\ncasts: {obj.casts}\n=======================\n"
                )
                break
        else:
            print("Media not found...!")

    @staticmethod
    def show_list():
        # Display the list of all media
        for obj in MEDIA:
            print(
                f"type: {obj.type}\nname: {obj.name}\nDirector: {obj.director}\nImdb_score: {obj.imdb_score}\nUrl: {obj.url}\nDuration: {obj.duration}\ncasts: {obj.casts}\n=======================\n"
            )


# Start Program
print("🎉 Welcome To My Store 🎉")
print("⏳ Loading")
db = Database()
db.read()
store = Store()

while True:
    print("============================")
    Store.show_menu()
    user_select = int(input("Enter Your Choice: "))  # Corrected spelling of "Choice"
    print("============================")
    
    match user_select:
        case 1:
            Store.add()

        case 2:
            old_name = input("Enter movie name: ")
            new_name = input("Enter movie new name: ")
            store.edit(old_name, new_name)

        case 3:
            media_name = input("Enter Movie name you want to remove: ")
            store.remove(media_name)

        case 4:
            media_name = input("Enter Movie name you want to find: ")
            store.search(media_name)

        case 5:
            Store.show_list()

        case 6:
            media_name = input("Enter Movie name you want to find: ")
            Media.show_info(media_name)

        case 7:
            media_name = input("Enter movie name you want to download: ")
            Media.download(media_name)

        case 8:
            db.write()
            exit(0)

