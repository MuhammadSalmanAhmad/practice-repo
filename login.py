name=input("enter your username")
password=input("enter your password")

def login():
    x=input("enter your name again")
    y=input("enter your password again")
    if (x==name and y==password):
        print("login successful")
