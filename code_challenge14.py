
anime_list = []

print("Welcome to the Anime List Creator!")
print("Enter the title of an anime (or type 'exit' to finish).")

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ").strip()

    if anime.lower() == 'exit':
        print("\nYou have exited the anime entry program.")
        break

    elif anime == "":
        print("You did not enter any title. Please type an anime name or 'exit'.")
        continue

    anime_list.append(anime)
    print(f"'{anime}' has been added to your anime list.\n")

print("\nYour anime list includes:")
if len(anime_list) == 0:
    print("No anime were added.")
else:
    for title in anime_list:
        print(f"- {title}")

print("\nThank you for using the Anime List Creator!")
