print("This is CS50")
print("Hello,World!")

# removes whitespace then capitalize name and store it into variable.
username = input("Enter your name: ").strip().capitalize()
date = input("Enter date today: ")
[date,time] = date.split(" ")
print(date,time)
print(f"Hello {username}, welcome to CS50!")



