class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subfolders = {}

    def add_file(self, filename):
        self.files.append(filename)

    def add_subfolder(self, folder_name):
        if folder_name not in self.subfolders:
            self.subfolders[folder_name] = Folder(folder_name)
        else:
            print("Folder already exists!")

    def select_folder(self, folder_name):
        if folder_name in self.subfolders:
            return self.subfolders[folder_name]
        else:
            print("Folder not found!")
            return self

    def __count_files(self):
        count = len(self.files)
        for subfolder in self.subfolders.values():
            count += subfolder.__count_files()
        return count

    def __len__(self):
        return self.__count_files()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return False

    def __str__(self, level=0):
        result = "  " * level + f"--Folder: {self.name}\n"
        for file in self.files:
            result += "  " * (level + 1) + f"File: {file}\n"
        for subfolder in self.subfolders.values():
            result += subfolder.__str__(level + 1)
        return result


def folder_menu():
    root = Folder("Start Folder")
    current_folder = root

    while True:
        print("\n=== Menu ===")
        print(f"== Current Folder: {current_folder.name} ==")
        print("1) Add File")
        print("2) Add Folder")
        print("3) Select Folder")
        print("4) Print Folder")
        print("5) Exit")
        choice = input(">> Input: ")

        if choice == "1":
            filename = input("Enter file name: ")
            current_folder.add_file(filename)
        elif choice == "2":
            folder_name = input("Enter folder name: ")
            current_folder.add_subfolder(folder_name)
        elif choice == "3":
            folder_name = input("Enter folder name to select: ")
            selected_folder = current_folder.select_folder(folder_name)
            if selected_folder != current_folder:
                current_folder = selected_folder
        elif choice == "4":
            print(current_folder)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    folder_menu()
