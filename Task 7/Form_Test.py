print("==========================================")
print("        PERSONAL PROFILE")
print("==========================================\n")

name = input("First name: ")
surname = input("Last name: ")
age = input("Age: ")
city = input("City: ")
country = input("Country: ")
study = input("School / Job: ")
course = input("Course or grade (if any): ")
hobby = input("Hobby: ")
skills = input("Main skills or interests: ")
music = input("Favorite music genre: ")
game = input("Favorite game: ")
movie = input("Favorite movie or TV show: ")
food = input("Favorite food: ")
dream = input("Biggest dream: ")
goal = input("Goal for the next year: ")

print("\n==========================================")
print("        SHORT STORY ABOUT ME")
print("==========================================\n")

print(
    f"Hi! My name is {name} {surname}. "
    f"I am {age} years old and I live in {city}, {country}. "
    f"Currently, I study or work at {study}."
)

if course.strip() != "":
    print(f"At the moment, I am studying in {course}.")

print(
    f"In my free time, I enjoy {hobby}. "
    f"My main skills and interests include {skills}. "
    f"I mostly listen to {music} music."
)

print(
    f"My favorite game is {game}, "
    f"and my favorite movie or TV show is {movie}. "
    f"My favorite food is {food}."
)

print(
    f"My biggest dream is {dream}. "
    f"My main goal for the next year is {goal}."
)

print("\n==========================================")
print("Thank you for filling out the form!")
print("Have a great day and good luck with your studies!")