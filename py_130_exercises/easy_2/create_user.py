"""

Create a function create_user that takes a username and requires keyword-only arguments for email and age.

"""


def create_user(name,*,email, age):
    user = {"username":name, "email": email, "age": age}
    return user


print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
print(create_user("Srdjan", "srdjan@example.com", age=39))
# Raises an exception