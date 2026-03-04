"""
Create a generator function that yields user input strings until the word "stop" is entered.
"""

def user_input_generator():
    user_input = input("Write a word: ")
    
    while user_input != "stop":
        yield user_input
        user_input = input("Write a word: ")
    print("You entered 'stop'. Generator will now stop.") 


for word in user_input_generator():
    print(f"You entered: {word}")