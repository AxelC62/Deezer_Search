import os
import requests
from colorama import Fore
from treelib import Tree
from pystyle import Colorate, Colors
from pycenter import center

# Partie utilisateur faites :)
# Partie artist faites :)

"""

Parti User

Categories :

- Information - Faits 
- Url - Faits
- Playlists - Faits

"""
class find_id:
    def __init__(self):
        self.name = input(Colorate.Color(Colors.pink, "\nName -> "))
        try:
            self.request_get_user = requests.get(f"http://api.deezer.com/search/user/?q={self.name}")
            self.data = self.request_get_user.json()
            print(f"\nUser id : {self.data['data'][0]['id']}")

            self.request_get_artist = requests.get(f"http://api.deezer.com/search/artist/?q={self.name}")
            self.data = self.request_get_artist.json()
            print(f"Artist id : {self.data['data'][0]['id']}\n")
        except:
            print("\nThis pseudonym is unavailable\n")

class deezer_user_id:
    def __init__(self):
        os.system("cls")
        self.title = """

                 ,----.     ,----.               ,----.               
  _,..---._   ,-.--` , \ ,-.--` , \ ,--,----. ,-.--` , \  .-.,.---.   
/==/,   -  \ |==|-  _.-`|==|-  _.-`/==/` - ./|==|-  _.-` /==/  `   \  
|==|   _   _\|==|   `.-.|==|   `.-.`--`=/. / |==|   `.-.|==|-, .=., | 
|==|  .=.   /==/_ ,    /==/_ ,    / /==/- / /==/_ ,    /|==|   '='  / 
|==|,|   | -|==|    .-'|==|    .-' /==/- /-.|==|    .-' |==|- ,   .'  
|==|  '='   /==|_  ,`-.|==|_  ,`-./==/, `--`\==|_  ,`-._|==|_  . ,'.  
|==|-,   _`//==/ ,     /==/ ,     |==\-  -, /==/ ,     //==/  /\ ,  ) 
`-.`.____.' `--`-----```--`-----`` `--`.-.--`--`-----`` `--`-`--`--'   


        """

        print(Colorate.Horizontal(Colors.blue_to_red, center(self.title)))
        self.id = input(Colorate.Color(Colors.pink, "User ID -> "))
        self.request_get = requests.get(f"https://api.deezer.com/user/{self.id}")
        self.data = self.request_get.json()

        self.tree = Tree()
        self.tree_info = Tree()
        self.tree_url = Tree()
        self.tree_playlists = Tree()

        self.request_get_playlists = None
        self.data_playlists = None
        self.r = None

    def results_data(self):
        self.tree.create_node(Colorate.Color(Colors.blue, f"\n{self.data['name']}"), 1)

        # Categories information

        self.tree_info.create_node(Colorate.Horizontal(Colors.blue_to_red, "Informations"), 2)
        self.tree_info.create_node(f"Id : {self.data['id']}", parent=2)
        self.tree_info.create_node(f"Name : {self.data['name']}", parent=2)
        self.tree_info.create_node(f"Country : {self.data['country']}", parent=2)
        self.tree_info.create_node(f"Type : {self.data['type']}", parent=2)

        # Categories url

        self.tree_url.create_node(Colorate.Horizontal(Colors.blue_to_red, "Url"), 3)
        self.tree_url.create_node(f"Link deezer : {self.data['link']}", parent=3)
        self.tree_url.create_node(f"Link picture : {self.data['picture']}", parent=3)
        self.tree_url.create_node(f"Link picture small : {self.data['picture_small']}", parent=3)
        self.tree_url.create_node(f"Link picture medium : {self.data['picture_medium']}", parent=3)
        self.tree_url.create_node(f"Link picture big : {self.data['picture_big']}", parent=3)
        self.tree_url.create_node(f"Link picture xl : {self.data['picture_xl']}", parent=3)
        self.tree_url.create_node(f"Link tracklist : {self.data['tracklist']}", parent=3)

        # Categories playlists

        self.request_get_playlists = requests.get(f"https://api.deezer.com/user/{self.id}/playlists")
        self.data_playlists = self.request_get_playlists.json()

        self.tree_playlists.create_node(Colorate.Horizontal(Colors.blue_to_red, "Playlists"), 5)
        for self.r in self.data_playlists['data']:
            self.tree_playlists.create_node(
                f"Title : {self.r['title']} | Id : {self.r['id']} | MD5 image : {self.r['md5_image']}", parent=5)

        self.tree.paste(1, self.tree_url)
        self.tree.paste(1, self.tree_info)
        self.tree.paste(1, self.tree_playlists)
        self.tree.show()

        returnMain = input(f"{Colorate.Color(Colors.pink, 'Replay (Y or N) -> ')}")

        if returnMain.lower()[0:1] == 'n':
            exit()
        if returnMain.lower()[0:1] == 'y':
            deezer()


"""

Parti Artist

Categories :

- Albums - Faits
- Information - Faits 
- Url - Faits
- Playlists - Faits

"""


class deezer_artist_id:
    def __init__(self):
        os.system("cls")
        self.title = """

                 ,----.     ,----.               ,----.               
  _,..---._   ,-.--` , \ ,-.--` , \ ,--,----. ,-.--` , \  .-.,.---.   
/==/,   -  \ |==|-  _.-`|==|-  _.-`/==/` - ./|==|-  _.-` /==/  `   \  
|==|   _   _\|==|   `.-.|==|   `.-.`--`=/. / |==|   `.-.|==|-, .=., | 
|==|  .=.   /==/_ ,    /==/_ ,    / /==/- / /==/_ ,    /|==|   '='  / 
|==|,|   | -|==|    .-'|==|    .-' /==/- /-.|==|    .-' |==|- ,   .'  
|==|  '='   /==|_  ,`-.|==|_  ,`-./==/, `--`\==|_  ,`-._|==|_  . ,'.  
|==|-,   _`//==/ ,     /==/ ,     |==\-  -, /==/ ,     //==/  /\ ,  ) 
`-.`.____.' `--`-----```--`-----`` `--`.-.--`--`-----`` `--`-`--`--'   


        """

        print(Colorate.Horizontal(Colors.blue_to_red, center(self.title)))

        self.id = input(Colorate.Color(Colors.pink, "Artist ID -> "))
        self.request_get = requests.get(f"https://api.deezer.com/artist/{self.id}")
        self.data = self.request_get.json()

        self.tree = Tree()
        self.tree_info = Tree()
        self.tree_url = Tree()
        self.tree_albums = Tree()
        self.tree_playlists = Tree()

        self.request_get_albums = None
        self.data_albums = None
        self.r = None
        self.request_get_playlists = None
        self.data_playlists = None

    def results_data(self):
        self.tree.create_node(Colorate.Color(Colors.blue, f"\n{self.data['name']}"), 1)

        # Categories information

        self.tree_info.create_node(Colorate.Horizontal(Colors.blue_to_red, "Informations"), 2)
        self.tree_info.create_node(f"Id : {self.data['id']}", parent=2)
        self.tree_info.create_node(f"Name : {self.data['name']}", parent=2)
        self.tree_info.create_node(f"Number of albums : {self.data['nb_album']}", parent=2)
        self.tree_info.create_node(f"Number of fan : {self.data['nb_fan']}", parent=2)
        self.tree_info.create_node(f"Radio : {self.data['radio']}", parent=2)
        self.tree_info.create_node(f"Type : {self.data['type']}", parent=2)

        # Categories url

        self.tree_url.create_node(Colorate.Horizontal(Colors.blue_to_red, "Url"), 3)
        self.tree_url.create_node(f"Link deezer : {self.data['link']}", parent=3)
        self.tree_url.create_node(f"Link share : {self.data['share']}", parent=3)
        self.tree_url.create_node(f"Link picture : {self.data['picture']}", parent=3)
        self.tree_url.create_node(f"Link picture small : {self.data['picture_small']}", parent=3)
        self.tree_url.create_node(f"Link picture medium : {self.data['picture_medium']}", parent=3)
        self.tree_url.create_node(f"Link picture big : {self.data['picture_big']}", parent=3)
        self.tree_url.create_node(f"Link picture xl : {self.data['picture_xl']}", parent=3)
        self.tree_url.create_node(f"Link tracklist : {self.data['tracklist']}", parent=3)

        # Categories albums

        self.request_get_albums = requests.get(f"https://api.deezer.com/artist/{self.id}/albums")
        self.data_albums = self.request_get_albums.json()

        self.tree_albums.create_node(Colorate.Horizontal(Colors.blue_to_red, "Albums"), 4)
        for self.r in self.data_albums['data']:
            self.tree_albums.create_node(
                f"Title : {self.r['title']} | Release date : {self.r['release_date']} | Id : {self.r['id']} | MD5 image : {self.r['md5_image']}",
                parent=4)

        # Categories playlists

        self.request_get_playlists = requests.get(f"https://api.deezer.com/artist/{self.id}/playlists")
        self.data_playlists = self.request_get_playlists.json()

        self.tree_playlists.create_node(Colorate.Horizontal(Colors.blue_to_red, "Playlists"), 5)
        for self.r in self.data_playlists['data']:
            self.tree_playlists.create_node(
                f"Title : {self.r['title']} | Id : {self.r['id']} | MD5 image : {self.r['md5_image']}", parent=5)

        self.tree.paste(1, self.tree_url)
        self.tree.paste(1, self.tree_albums)
        self.tree.paste(1, self.tree_playlists)
        self.tree.paste(1, self.tree_info)
        self.tree.show()

        returnMain = input(f"{Colorate.Color(Colors.pink, 'Replay (Y or N) -> ')}")

        if returnMain.lower()[0:1] == 'n':
            exit()
        if returnMain.lower()[0:1] == 'y':
            deezer()


class deezer:
    def __init__(self):
        os.system("cls")
        self.title = """

                 ,----.     ,----.               ,----.               
  _,..---._   ,-.--` , \ ,-.--` , \ ,--,----. ,-.--` , \  .-.,.---.   
/==/,   -  \ |==|-  _.-`|==|-  _.-`/==/` - ./|==|-  _.-` /==/  `   \  
|==|   _   _\|==|   `.-.|==|   `.-.`--`=/. / |==|   `.-.|==|-, .=., | 
|==|  .=.   /==/_ ,    /==/_ ,    / /==/- / /==/_ ,    /|==|   '='  / 
|==|,|   | -|==|    .-'|==|    .-' /==/- /-.|==|    .-' |==|- ,   .'  
|==|  '='   /==|_  ,`-.|==|_  ,`-./==/, `--`\==|_  ,`-._|==|_  . ,'.  
|==|-,   _`//==/ ,     /==/ ,     |==\-  -, /==/ ,     //==/  /\ ,  ) 
`-.`.____.' `--`-----```--`-----`` `--`.-.--`--`-----`` `--`-`--`--'   
                        
                        By Kijusu and Prasax-Dev
                          By Maxence and Axel
"""

        textingBox = f"""
                                                (+)══════════════════════════════════════════════════════════════════════(+)
                                                 ║                                                                        ║
                                                 ║   {Fore.WHITE}[{Fore.MAGENTA}01{Fore.WHITE}] Search User with Id, {Fore.WHITE}[{Fore.MAGENTA}02{Fore.WHITE}] Search Artist with Id, {Fore.WHITE}[{Fore.MAGENTA}03{Fore.WHITE}] Find ID   ║
                                                 ║                                                                        ║
                                                (+)══════════════════════════════════════════════════════════════════════(+)
        """

        print(Colorate.Horizontal(Colors.blue_to_red, center(self.title)))
        print(center(textingBox))

        while True:
            choice = input("Deezer Search -> ")
            if choice == '01':
                deezer_user_id().results_data()
            if choice == '02':
                deezer_artist_id().results_data()
            if choice == '03':
                find_id()
            else:
                pass


deezer()
