def classify_age(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teen"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"

user_age = int(input("Enter your age: "))
print(classify_age(user_age))