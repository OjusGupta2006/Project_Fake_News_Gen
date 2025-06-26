# 1 Import random module
import random

# 2 Create lists for subjects, actions and places

Subjects = [
    "Akshay Kumar",
    "Prime Minister Modi",
    "Salman Khan",
    "A Delhi Boy",
    "A cute dog",
    "Birds",
    "New Mahindra Thar Roxx",
    "Monkey",
    "God",
    "The Visual Studio Code",
]

Actions = [
    "declares war on a country",
    "eats ice cream",
    "got a fire burn",
    "rides a buffalo",
    "gets caught",
    "races",
]

Places = [
    "at India Gate",
    "in Mc Donalds",
    "at F1 Racing Track",
    "inside Supreme Court",
    "in Kaala Paani Jail",
    "inside the Park",
    "at the Bar",
]

print("📢 Welcome to the Fake News Generator")


# while loop
while True:
    print("\nPlease choose an option to continue")
    print("\n1. Generate Random Fake News")
    print("\n2. Create your custom Fake News")
    print("\n3. Exit")

    choice = input("Enter your option (1,2 or 3): ").strip()

    if choice == "1":
        subjects = random.choice(Subjects)
        actions = random.choice(Actions)
        places = random.choice(Places)
        print("📢 Breaking News : " + "\n" + f"{subjects} {actions} {places}")

    elif choice == "2":
        print("📢 Create your own Fake News ")
        subjects = input("\nEnter a Subject: ").strip()
        actions = input("\nEnter an Action: ").strip()
        places = input("\nEnter a Place: ").strip()
        print("\n📢 Your Custom Breaking News : " +
              "\n" + f"{subjects} {actions} {places}")

    elif choice == "3":
        print("\nThank you for using the fake news generator")
        break

    else:
        print("Invalid Choice. Please choose from 1, 2 or 3")
