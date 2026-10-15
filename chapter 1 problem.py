print('''
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are ''')
#question 2
import pyttsx3
engine = pyttsx3.init()
engine.say("BTS paved the way")
engine.runAndWait()
#problem 4
import os

# Specify the directory path ('.' represents the current directory)
directory_path = 'c:\\'

try:
    # os.listdir() returns a list containing the names of the entries in the directory
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{os.path.abspath(directory_path)}':\n")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")