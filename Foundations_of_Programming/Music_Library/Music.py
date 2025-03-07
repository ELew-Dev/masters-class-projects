class User:
    def __init__(self, name):
        self.name = name
        self.music_collection = {}  # Dictionary to store songs as {title: artist}
    
    def add_song(self, title, artist):
        self.music_collection[title] = artist
        print(f"Song '{title}' by {artist} added to {self.name}'s collection.")
    
    def retrieve_song(self, title):
        return self.music_collection.get(title, "Song not found.")
    
    def update_song(self, title, new_artist):
        if title in self.music_collection:
            self.music_collection[title] = new_artist
            print(f"Song '{title}' updated to artist {new_artist}.")
        else:
            print("Song not found.")
    
    def delete_song(self, title):
        if title in self.music_collection:
            del self.music_collection[title]
            print(f"Song '{title}' removed from collection.")
        else:
            print("Song not found.")
    
    def display_songs(self):
        if not self.music_collection:
            print("No songs in collection.")
        else:
            print(f"{self.name}'s Music Collection:")
            for title, artist in self.music_collection.items():
                print(f"{title} - {artist}")

class MusicOrganizer:
    def __init__(self):
        self.users = {}  # Dictionary to store users as {username: User object}
        self.current_user = None
    
    def add_user(self, name):
        if name in self.users:
            print("User already exists.")
        else:
            self.users[name] = User(name)
            self.current_user = self.users[name]
            print(f"User '{name}' added and set as current user.")
    
    def change_user(self, name):
        if name in self.users:
            self.current_user = self.users[name]
            print(f"Switched to user '{name}'.")
        else:
            print("User not found.")
    
    def menu(self):
        while True:
            print("=== Menu ===")
            if self.current_user:
                print(f"== User {self.current_user.name} ==")
            print("1) Add user")
            if self.users:
                print("2) Change user")
            if self.current_user:
                print("3) Add a song")
                print("4) Retrieve song details")
                print("5) Update song details")
                print("6) Delete a song")
                print("7) Display all songs")
                print("8) Exit")
            choice = input(">> input: ")
            
            if choice == "1":
                name = input(">> input UserName: ")
                self.add_user(name)
            elif choice == "2" and self.users:
                print("Select User:")
                for i, user in enumerate(self.users, 1):
                    print(f"{i}) {user}")
                user_choice = int(input(">> input: ")) - 1
                if 0 <= user_choice < len(self.users):
                    self.change_user(list(self.users.keys())[user_choice])
                else:
                    print("Invalid selection.")
            elif choice == "3" and self.current_user:
                title = input(">> input song title: ")
                artist = input(">> input song artist: ")
                self.current_user.add_song(title, artist)
            elif choice == "4" and self.current_user:
                title = input(">> input song title: ")
                print(f"Artist: {self.current_user.retrieve_song(title)}")
            elif choice == "5" and self.current_user:
                title = input(">> input song title: ")
                new_artist = input(">> input new artist: ")
                self.current_user.update_song(title, new_artist)
            elif choice == "6" and self.current_user:
                title = input(">> input song title: ")
                self.current_user.delete_song(title)
            elif choice == "7" and self.current_user:
                self.current_user.display_songs()
            elif choice == "8":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = MusicOrganizer()
    app.menu()
