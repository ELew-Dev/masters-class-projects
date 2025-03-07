class CreatureNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class CreatureFamilyTree:
    def __init__(self):
        self.root = None
    
    def add_root(self, name):
        if not self.root:
            self.root = CreatureNode(name)
            return f"{name} is the root creature!"
        else:
            return "Root already exists."
    
    def add_creature(self, parent_name, name, side):
        if not self.root:
            return "Root creature does not exist."
        
        parent = self.find_creature(self.root, parent_name)
        if not parent:
            return "Parent not found."
        
        side = side.strip().upper()  # Normalize input
        if side == 'L' and not parent.left:
            parent.left = CreatureNode(name)
            return f"{name} added as left child of {parent_name}."
        elif side == 'R' and not parent.right:
            parent.right = CreatureNode(name)
            return f"{name} added as right child of {parent_name}."
        else:
            return "That position is already occupied or invalid input."
    
    def find_creature(self, node, name):
        if not node:
            return None
        if node.name == name:
            return node
        
        left_search = self.find_creature(node.left, name)
        if left_search:
            return left_search
        return self.find_creature(node.right, name)
    
    def print_tree(self, node, level=0, prefix="Root: "):
        if node:
            print("    " * level + prefix + node.name)
            if node.left:
                self.print_tree(node.left, level + 1, "L--> ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--> ")
    
    def find_ancestors(self, name):
        ancestors = []
        if not self.find_ancestor_helper(self.root, name, ancestors):
            return "Creature not found."
        return " -> ".join(ancestors[::-1]) if ancestors else "No ancestors found."
    
    def find_ancestor_helper(self, node, name, ancestors):
        if not node:
            return False
        if node.name == name:
            return True
        
        if self.find_ancestor_helper(node.left, name, ancestors) or self.find_ancestor_helper(node.right, name, ancestors):
            ancestors.append(node.name)
            return True
        return False

# Main program loop
def main():
    tree = CreatureFamilyTree()
    
    while True:
        print("\n=== Menu ===")
        print("0) Add Root Creature")
        print("1) Add Creature")
        print("2) Print All")
        print("3) Print Ancestors")
        print("4) Exit")
        choice = input("============= \n>> Input: ")
        
        if choice == '0':
            name = input(">> Input Name: ")
            print(tree.add_root(name))
        
        elif choice == '1':
            parent_name = input(">> Input Parent Name: ")
            side = input(">> Input 'L' or 'R' for child: ")
            name = input(">> Input Name: ")
            print(tree.add_creature(parent_name, name, side))
        
        elif choice == '2':
            if tree.root:
                print("=== Creatures ===")
                tree.print_tree(tree.root)
            else:
                print("The tree is empty. Add a root first.")
        
        elif choice == '3':
            name = input(">> Input Node Name: ")
            print(tree.find_ancestors(name))
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
