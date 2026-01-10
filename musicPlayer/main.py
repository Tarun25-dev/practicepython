import os
#actually when we import pygame it shows a welcome message that was
#pygame 2.6.1 (SDL 2.28.4, Python 3.11.6)
#Hello from the pygame community. https://www.pygame.org/contribute.html. whenever we run this code this prints in console but you dont need this we need to remove.
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide" # this line hides the above two comment lines.
import pygame # this library is used for playing sounds and music and handling keyboard,mouse,joystick input.but main purpose is for creaing a 2d games and game windows.

def play_music(folder,song_name):
    file_path=os.path.join(folder,song_name)

    if not os.path.exists(file_path):
        print("File not found!")
        return
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print(f"\nNow Playing: {song_name}")
    print("commands: [P]-pause, [R]-resume, [S]-stop")

    while True:
        command=input("> ").upper()
        if command=='P':
            pygame.mixer.music.pause()
            print("Paused")
        elif command == 'R':
            pygame.mixer.music.unpause()
            print("Resumed")
        elif command == 'S':
            pygame.mixer.music.stop()
            print("Stoped")
            return # which exits from loop beacuse user want to stop the song not pause
        else:
            print("Invalid command")

def main():
    try:
        pygame.mixer.init() # is used for loading and playing the sounds 
        # mixer.init() initialize the sound system in pygame without this we can get errors.imagine just like engine on button when we on then we control and manage sound system.
    except pygame.error as e: # it happens when any error occurs with the pygame
        print("Auido initialization failed!",e)
        return
    folder="music" # which is already i named "music" and keep all mp3 files inside.


    if not os.path.isdir(folder): # if the folder is not there then prints this and exit
        print(f"Folder '{folder}' not found")
        return
    mp3_files=[file for file in os.listdir(folder) if file.endswith(".mp3")] # list comprehension
    # first for loop takes one by one files in the folder dir and returns it in list beacuse we write listdir(folder) and that file needs to check the if condition if it is mp3 file then add it. 
    if not mp3_files: # if list is empty then there is no such mp3 files in directory, so we need to print
        print("No .mp3 files found!")
    # main loop 
    while True:
        print("******* Music Player *******")
        print("▶ My Songs List:")
        for index,song in enumerate(mp3_files,start=1): # enumerate is a function if handles data with index values actually deafault value is 0 but we want from 1 so thats why start = 1 we keep it.
            print(f"{index}. {song}")
        choice_input=input("\nEnter the song # to play (or 'Q' to quit): ")

        if choice_input.upper()=='Q':
            print("Bye!")
            return
        if not choice_input.isdigit():
            print("Not a valid choice!")
            continue #which skips the current iteration when if statement true
        choice=int(choice_input)-1 # why beacuse list has index from 0 so we need to minus one
        
        if choice>=0 and choice<=len(mp3_files):
            play_music(folder,mp3_files[choice])
        else:
            print("Invalid choice")
            



if __name__=="__main__":
    main()