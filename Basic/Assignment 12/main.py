##### Mohammad Ali Mirzaei #####


from media import *
import actor
import clip
import documentary
import film
import series


class Database:
    
    def read(self):
        data = open("Pylearn7\Assignment 12\database.txt", "r")
        for line in data:
            detail = line.split(",")
            my_obj = Media(
                detail[0],
                detail[1],
                detail[2],
                detail[3],
                detail[4],
                detail[5],
                detail[6],
            )
            MEDIA.append(my_obj)
        data.close()

    def write(self):
        data = open("Pylearn7\Assignment 12\database.txt", "w")
        for obj in MEDIA:
            result = f"{obj.type},{obj.name},{obj.director},{obj.imdb_score},{obj.url},{obj.duration},{obj.casts}"
            data.write(result)

class Store:

    @staticmethod
    def show_menu():
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
        type = input("Enter media type: ")
        name = input("Enter media name: ")
        director = input("Enter director name: ")
        imdb_score = input("Enter imdb score: ")
        url = input("Enter url address: ")
        duration = input("Enter duration time: ")
        casts = input("Enter casts list: ")
        new_media = Media(type, name, director, imdb_score, url, duration, casts)
        MEDIA.append(new_media)
        print("New media add to list successfully")

    def edit(self, old_name, new_name):
        for obj in MEDIA:
            if obj.name == old_name:
                obj.name = new_name
                print('Media edited successfully') 
                break   
        else:
            print('Media Not found...!')    


    def remove(self, media_name):
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
        for obj in MEDIA:
            if media_name in obj.name:
                print(
                    f"type: {obj.type}\nname: {obj.name}\nDirector: {obj.director}\nImdb_score: {obj.imdb_score}\nUrl: {obj.url}\nDuration: {obj.duration}\ncasts: {obj.casts}\n=======================\n"
                )
                break
        else:
            print("Media not found...!")

    @staticmethod
    def show_list():
        for obj in MEDIA:
            print(
                f"type: {obj.type}\nname: {obj.name}\nDirector: {obj.director}\nImdb_score: {obj.imdb_score}\nUrl: {obj.url}\nDuration: {obj.duration}\ncasts: {obj.casts}\n=======================\n"
            )


# Start Programm
print("🎉 Welcome To My Store 🎉")
print("⏳ Loading")
db = Database()
db.read()
store = Store()

while True:
    print("============================")
    Store.show_menu()
    user_select = int(input("Enter Your Choise: "))
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
