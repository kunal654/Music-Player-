import pygame
import os

def main():
    pygame.mixer.init()
    
    while True:
        print("\n1. Play music\n2. Stop music\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file = input("Enter the path to the music file: ")
            if os.path.exists(file):
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
            else:
                print("File not found.")
        elif choice == "2":
            pygame.mixer.music.stop()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
