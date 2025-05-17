def chatbot():
    while True:
        print("\nHello, welcome to the interactive chatbot :)")
        mood = input("How are you feeling today? (good / bad / excited / tired / other): ").strip().lower()

        if mood == "good":
            print("That's awesome! Keep it up 😊")
        elif mood == "bad":
            print("Oh no! Hope things get better soon 😔")
        elif mood == "excited":
            print("Yay! What's got you excited? 🚀")
        elif mood == "tired":
            print("Maybe a nap or a snack would help 😴")
        else:
            print("Thanks for sharing. Emotions are complex, huh? 🤔")

        name = input("\nWhat's your name? ").strip().capitalize()
        print(f"Nice to meet you, {name}!")

        topic = input("Would you like to talk about (1) Hobbies, (2) School, or (3) Something random? ").strip()
        if topic == "1":
            hobby = input("What's your favorite hobby? ").strip()
            print(f"{hobby}? Sounds fun! I wish I could try it too.")
        elif topic == "2":
            subject = input("What's your favorite school subject? ").strip().lower()
            if subject in ["math", "science"]:
                print(f"{subject.capitalize()} is so interesting and useful!")
            else:
                print(f"{subject.capitalize()} must be really cool!")
        elif topic == "3":
            print("Did you know octopuses have three hearts? 🐙 Weird but true!")
        else:
            print("That's okay, we can chat about anything next time.")

        again = input("\nWould you like to talk again? (yes / no): ").strip().lower()
        if again != "yes":
            print(f"Goodbye, {name}! Take care 👋")
            break

chatbot()
