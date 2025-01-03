user_name=input("Enter your username: ")

valid_user="False"
if 5<len(user_name)<=15:
    if user_name[0].isalpha():
        for i in user_name:
            if i.isalnum():
                valid_user="True"
                continue
            else:
                valid_user="False"
                break

if(valid_user=="True"):
     print("The user is valid")
else:
    print("Invalid user")



