from Pet import Pet  # Import the Pet class from pet.py

if __name__ == "__main__":
    my_pet = Pet("Max")
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.train("roll over")
    my_pet.train("play dead")
    my_pet.get_status()