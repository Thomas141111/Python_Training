# def decor(f1):
#     def inner(name):
#         if name=="Tom":
#             print("#"*20)
#             print("HEllo",name)
#         else:
#             f1(name)
#             print("Heeello",name)
#     return inner
#
# @decor
# def wish(name):
#     print("Hello", name,"GOod")
#
# wish("Tom")
# wish("Gags")

authorized=True
def login_required(func):
    def inner(*args,**kwargs):
        if authorized:
            print("hello")
            return func("hbjb")
        else:
            print("Please login")
            return False
    return inner

@login_required
def withdraw(str):
    print(str)

def logout():
    global authorized
    authorized=False
    print(authorized)
    print("loggged out")


# while True:
#     choice = int(input("1.Login\n2.Logout\n"))
#     if choice == 1:
#         withdraw("Hello")
#     if choice == 2:
#         logout()
#     print(authorized)
withdraw()
logout()
print(authorized)
withdraw()
