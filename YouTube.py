from xmlrpc.server import list_public_methods
from pytube import YouTube
import os
import time



end_stage = False

commends = ["s","list_start","list_end","link","location"]
default_location = 'G:/'
def download(link):
    if link:
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        yd.download(default_location)
        
    else:
        pass
    
def clear_terminal():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

while not end_stage:
    print(f"now your default save location is {default_location}")
    print(
        """
        if want to stop, 's' \n
        if want a list start, 'list_start' \n
        if want a list end, 'list_end' \n
        if want to download from link, 'link' \n
        if wanna change location, 'location'\n
        """
    )
    list_end = True
    input_commend = input("enter input :")
    if input_commend in commends:
        if input_commend == "s" :
            end_stage = True
        if input_commend == "list_start":
            link_list = []
            list_end = False
            print("""
                  list is start now! enter your links! \n
                  if want a list end, 'list_end' 
                  """)
            while not list_end:
                list_input = input("enter input :")
                if list_input == "list_end":
                    list_end = True
                else:
                    link_list.append(list_input)
                    print(link_list)
            if len(link_list) != 0:
                for link in link_list:
                    print(f"start download video from '{link}'")
                    download(link)
                    print(f"download finish from '{link}'")
            
            
        if input_commend == "list_end":
            print( "list is not start yet, please start list first")
        if input_commend == "link":
            link = input("enter url here :")
            print(f"start download video from '{link}'")
            download(link)
            print(f"download finish from '{link}'")
        if input_commend == "location":
            location = input("enter your location here :")
            default_location =  location
            print(default_location)
        clear_terminal()
    
        

    
        