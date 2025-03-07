class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species} and makes a {self.make_sound()} sound."

class Bear(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color
    
    def make_sound(self):
        return "roar"
    
    def info(self):
        return f"{self.name} is a {self.species} bear with {self.fur_color} fur and makes a {self.make_sound()} sound."

class Elephant(Animal):
    def __init__(self, name, species, weight):
        super().__init__(name, species)
        self.weight = weight
    
    def make_sound(self):
        return "trumpet"
    
    def info(self):
        return f"{self.name} is a {self.species} elephant weighing {self.weight} kg and makes a {self.make_sound()} sound."

class Penguin(Animal):
    def __init__(self, name, species, height):
        super().__init__(name, species)
        self.height = height
    
    def make_sound(self):
        return "squawk"
    
    def info(self):
        return f"{self.name} is a {self.species} penguin and stands at a height of {self.height} ft and makes a {self.make_sound()} sound."

def main():
    zoo = []
    while True:
        print("\n===Zoo Menu===")
        print("1) Add animals")
        print("2) Print all")
        print("3) Print specific")
        print("4) Exit")
        choice = input(">>input: ")

        if choice == "1":
            print("\n===Add Menu===")
            print("1) Add bear")
            print("2) Add elephant")
            print("3) Add penguin")
            add_choice = input(">>input: ")
            
            name = input("Enter name: ")
            species = input("Enter species: ")
            
            if add_choice == "1":
                fur_color = input("Enter fur color: ")
                zoo.append(Bear(name, species, fur_color))
            elif add_choice == "2":
                weight = float(input("Enter weight (kg): "))
                zoo.append(Elephant(name, species, weight))
            elif add_choice == "3":
                height = float(input("Enter height (ft): "))
                zoo.append(Penguin(name, species, height))
            
        elif choice == "2":
            print("\nAll Animals in the Zoo:")
            for animal in zoo:
                print(animal.info())
        
        elif choice == "3":
            print("\n===Print Menu===")
            print("1) Print bears")
            print("2) Print elephants")
            print("3) Print penguins")
            print("4) Go back")
            print_choice = input(">>input: ")
            
            if print_choice == "1":
                for animal in zoo:
                    if isinstance(animal, Bear):
                        print(animal.info())
            elif print_choice == "2":
                for animal in zoo:
                    if isinstance(animal, Elephant):
                        print(animal.info())
            elif print_choice == "3":
                for animal in zoo:
                    if isinstance(animal, Penguin):
                        print(animal.info())
        
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
