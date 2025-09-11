print("Welcome to Manga Reader of Temperature !")
print("Answer a few questions to get started!\n")

genre = input("What genre are you interested in? (action, romance, horror): ").lower()
duration = input("How long should a manga volume be? (long, medium, short): ").lower()
time = input("Which decade do you prefer? (2000s, 2010s): ").lower()

print("\n--- Your Manga Recommendations ---")

if genre == "action":
    if duration == "long":
        if time == "2000s":
            print("The available mangas are: Naruto, Bleach, and One Piece.")
        elif time == "2010s":
            print("The available mangas are: Attack on Titan, My Hero Academia, and Black Clover.")
    elif duration == "medium":
        if time == "2000s":
            print("The available mangas are: Fullmetal Alchemist and Gantz.")
        elif time == "2010s":
            print("The available mangas are: Demon Slayer, Fire Force, and Blue Exorcist.")
    elif duration == "short":
        if time == "2000s":
            print("The available mangas are: Samurai Champloo and Trigun.")
        elif time == "2010s":
            print("The available mangas are: Akame ga Kill! and Tokyo ESP.")

elif genre == "romance":
    if duration == "long":
        if time == "2000s":
            print("The available mangas are: Boys Be, Peach Girl, and Kare Kano.")
        elif time == "2010s":
            print("The available mangas are: Ao Haru Ride, Kimi ni Todoke, and Say I Love You.")
    elif duration == "medium":
        if time == "2000s":
            print("The available mangas are: Lovely★Complex and Fruits Basket.")
        elif time == "2010s":
            print("The available mangas are: Your Lie in April, Horimiya, and Orange.")
    elif duration == "short":
        if time == "2000s":
            print("The available mangas are: Honey and Clover and Paradise Kiss.")
        elif time == "2010s":
            print("The available mangas are: A Silent Voice and Wolf Girl & Black Prince.")

elif genre == "horror":
    if duration == "long":
        if time == "2000s":
            print("The available mangas are: Hellsing and Battle Royale.")
        elif time == "2010s":
            print("The available mangas are: Ajin: Demi-Human and Parasyte Rebirth.")
    elif duration == "medium":
        if time == "2000s":
            print("The available mangas are: Elfen Lied and Gantz (horror elements).")
        elif time == "2010s":
            print("The available mangas are: Tokyo Ghoul and The Promised Neverland.")
    elif duration == "short":
        if time == "2000s":
            print("The available mangas are: Uzumaki and Tomie by Junji Ito.")
        elif time == "2010s":
            print("The available mangas are: I Am a Hero and Franken Fran.")

else:
    print("Sorry, the genre you entered is not available. Please restart and try again.")

print("\nThank you for using Manga Reader of Temperature! Enjoy your reading adventure!")