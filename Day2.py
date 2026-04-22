def greet(name):
    return(f"Hello, {name}! Welcome to the system")

print(greet("Darshan"))

def welcome(name , city):
    return(f"Hello , {name} from {city} !Welcome to the location")

print(welcome("Drashan", "Lonavala"))

def check_age(age):
    if age >=18:
        return("You are eligible to vote")
    else:
        return("You are not eligible to vote")

print(check_age(100))


def display_user(user):
    print(f"Hello {user['name']} from {user['city']}, age {user['age']}")

def age_category(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 60:
        return "Adult"
    else:
        return "Senior"
    
user = crr()
display_user(user)

age_category = 25