"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()

def personal_info_manager():
    # Create initial person tuple
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    
    person = (name, age, city, country)
    hobbies = []

    while True:
        print("\n--- Personal Info Manager ---")
        print("1. Display all information")
        print("2. Add a new hobby")
        print("3. Remove a hobby")
        print("4. Update age")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print(f"\nName: {person[0]}")
            print(f"Age: {person[1]}")
            print(f"City: {person[2]}")
            print(f"Country: {person[3]}")
            print(f"Hobbies: {hobbies if hobbies else 'None'}")
        elif choice == "2":
            hobby = input("Enter a new hobby: ")
            hobbies.append(hobby)
            print(f"'{hobby}' added.")
        elif choice == "3":
            hobby = input("Enter a hobby to remove: ")
            if hobby in hobbies:
                hobbies.remove(hobby)
                print(f"'{hobby}' removed.")
            else:
                print("Hobby not found.")
        elif choice == "4":
            new_age = int(input("Enter new age: "))
            person = (person[0], new_age, person[2], person[3])
            print("Age updated.")
        elif choice == "5":
            print("Exiting Personal Info Manager.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    personal_info_manager()
