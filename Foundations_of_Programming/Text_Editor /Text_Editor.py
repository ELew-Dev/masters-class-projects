import os
from collections import Counter

def readTextFile(filename):
    """Reads text from a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def saveTextFile(filename, text):
    """Saves text back to the file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def AllWordCount(text):
    """Counts word frequency and returns the top 5 most common words."""
    words = text.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(5)

def SingleWordCount(text, word):
    """Counts occurrences of a single word."""
    return text.lower().split().count(word.lower())

def ReplaceWord(text, target, replacement):
    """Replaces a word and counts occurrences replaced."""
    count = text.lower().split().count(target.lower())
    text = text.replace(target, replacement)
    return text, count

def AddText(text, new_text):
    """Appends new text."""
    return text + '\n' + new_text

def DeleteText(text, target):
    """Deletes the first occurrence of the target text."""
    return text.replace(target, '', 1)

def HighLight(text, word):
    """Highlights a word in text by surrounding it with **."""
    return text.replace(word, f'**{word}**')

def ReverseText(text):
    """Reverses the order of words."""
    return ' '.join(text.split()[::-1])

def menu(filename):
    """Menu system for user interaction."""
    text = readTextFile(filename)
    while True:
        print("\n===Edit Menu===")
        print("1: Top 5 most common words")
        print("2: Single Word Frequency")
        print("3: Replace a word")
        print("4: Add Text")
        print("5: Delete Text")
        print("6: Highlight Text")
        print("7: Reverse Text (Extra Credit)")
        print("8: Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            print(AllWordCount(text))
        elif choice == '2':
            word = input("Enter a word: ")
            print(f"{word} appears {SingleWordCount(text, word)} times.")
        elif choice == '3':
            target = input("Enter word to replace: ")
            replacement = input("Enter replacement: ")
            text, count = ReplaceWord(text, target, replacement)
            print(f"{count} words replaced.")
        elif choice == '4':
            new_text = input("Enter text to add: ")
            text = AddText(text, new_text)
        elif choice == '5':
            target = input("Enter text to delete: ")
            text = DeleteText(text, target)
        elif choice == '6':
            word = input("Enter word to highlight: ")
            print(HighLight(text, word))
        elif choice == '7':
            print(ReverseText(text))
        elif choice == '8':
            saveTextFile(filename, text)
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    filename = "sample.txt"  # Ensure this file is present
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("This is a sample text file for the text editor.")
    menu(filename)
