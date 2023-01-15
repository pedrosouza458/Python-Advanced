class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "Lab", name = "Sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)