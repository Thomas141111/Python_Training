import pytest

def email_check(name):
    end=["gmail.com","yahoo.com","yash.com"]
    first=name.split("@")[0]
    second=name.split("@")[1]
    if first.isalnum():
        if second in end:
            print("valid mail")
            return True
        else:
            print("use correct domain")
    else:
        print("Enter valid mail")

def test_email():
    name="ww@yash.com"
    assert  email_check(name)

