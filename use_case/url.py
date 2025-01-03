def login():
    print("This is login")
def logout():
    print("This is logout")

while True:
    url=input("Enter Url:")
    l=url.rsplit("/",1)
    if l[1]=="login":
        login()
        break
    if l[1]=="logout":
        logout()
        break




