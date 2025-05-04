print(f"Hello, welcome to the chatbot :) \nWhat's your mood today?")
mood = input().strip().lower()
if mood == "good": 
    print("Great!")
elif mood == "bad": 
    print("Well that sucks")
else:
    print("Ohhhh k then...")
name = input("What's your name?")
print(f"Well bye then {name}!!!")