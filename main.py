'''
Q1. Create a Book class with properties: title, author, genre, and pages.

Make methods to:
1. __str__() - Prints out all properties neatly.
2. read() - Prints "[title] is being read!"
3. describe() - Prints "[title] is a [genre] book written by [author]."

Create a Book object and test your class and all its methods.
'''
class Book:
    def  __init__(self,title,author,genre,pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def read(self):
        print(f"{self.title} is being read!")

    def __str__(self):
        print(f"{self.title} is a {self.genre} book written by {self.author}.")

    def describe(self):
            print(f"{self.title} is a {self.genre} book written by {self.author}.")



'''
Q2. Write a class called "Employee" that has the attributes:
name, job_title, and salary.

Make 1 method for this class.

Then, create an object of the Employee class for each of the following people:
Alex (Software Developer, $65000)
Jamie (Web Designer, $58000)
Taylor (Database Administrator, $70000)

Print each object. (You'll need the __str__() method.)
'''
class Employee:
    def __init__(self,name,job_title,salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def __str__(self):
        print(f"{self.name} is a {self.job_title} and thier salary is {self.salary}")

Alex = Employee("Alex","Software Designer", 65000)
Jamie = Employee("Jamie","Web Designer", 58000)
Taylor = Employee("Alex","Database Administrator", 70000)



'''
Q3. Create a GameCharacter class and initialize it with:
name, level, health, weapon, and speed.

Make methods to:
1. __str__() - Displays all information about the character.
2. levelUp() - Adds 1 to the character's level.
3. heal() - Adds 10 to the character's health.
4. takeDamage() - Subtracts 10 from the character's health.

Create a GameCharacter object and test the class and all its methods.
'''
class GameCharacter:
    def __init__(self,name,level,health,weapon,speed):
        self.name = name
        self.level = level
        self.health = health
        self.weapon = weapon
        self.speed = speed

    def __str__(self):
        print(f"{self.name}")
        print(f"Level : {self.level}")
        print(f"Health : {self.health}")
        print(f'Weapon : {self.weapon}')
        print(f"Speed : {self.speed}")

    def levelup(self):
        self.level += 1

    def heal(self):
        self.health += 10

    def takeDamage(self):
        self.health -= 10


Player1 = GameCharacter("Ivan", 100, 100, "Sword", "100 mph")


'''
Q4. Write a class called Song that has the attributes:
title, artist, and year.

Then, create a LIST of Song objects for the following songs:

"Blinding Lights" (The Weeknd, 2020)
"Anti-Hero" (Taylor Swift, 2022)
"Flowers" (Miley Cyrus, 2023)

Print the title and artist of each song using a for loop.
'''

# class Song:
#     def __init__(self,title,artist,year):
#         self.title = title
#         self.artist = artist 
#         self.year = year

#     def __str__(self):
#         return(f"The song {song.title} was made by {song.artist} in the year of {song.year} ")

# song1 = Song("Blinding Lights", "The Weekend", 2020)
# song2 = Song("Anti-Hero", "Taylor Swift", 2022)
# song3 = Song("Flowers", "Miley Cyrus", 2023)

# songs = [song1,song2,song3]

# for song in songs:
#     print(song)


'''
Q5. Write a class named BankAccount that has the following
data attributes:

account_holder
balance

The class should have an __init__ method that accepts the
account holder's name and starting balance.

The class should also have the following methods:

- deposit: Adds a given amount to the balance.
- withdraw: Subtracts a given amount from the balance.
- get_balance: Returns the current balance.

Next, create a BankAccount object with a starting balance
of $500.

Deposit $100 three times using a for loop.

After each deposit, display the current balance.

Then withdraw $50 two times and display the balance after
each withdrawal.
'''
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        print(f"{self.name}'s Account has a total of ${self.balance} in the account.")

    def deposit(self,amount):
        self.balance += amount


    def withdrawal(self,amount):
        self.balance -= amount


    def get_balance(self):
        return(f"${self.balance}")

    
checkings = BankAccount("Ivan's bank", 500)

for x in range(3):
    checkings.deposit(100)
    print(checkings.get_balance())