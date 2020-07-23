class Profile:
    def __init__(self, name, email, age, password):
        self.name = name
        self.email = email
        self.age = age
        self.password = password

user1 = Profile("Matt", "matthewrgunn@upperline.com", 43, "Chewie")
user2 = Profile("Chewie", "chewie@upperline.com", 2, "_M@tt!_")
user3 = Profile("Maddie", "maddie@gmail.com", 10, "Dadisthebest")

print(user1.email)
