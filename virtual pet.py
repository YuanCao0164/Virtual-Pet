def print_cat_face():
    print(r"""
 /\_/\  
( o.o ) 
 > ^ <  
""")

def get_valid_name():
    while True:
        name = input("Please give your kitten a name! ")
        if name.isalpha() and len(name) <= 20:
            name = name[0].upper() + name[1:].lower()
            print(f'{name} loves the name you gave!')
            return name
        else:
            print("Invalid name, please re-enter")

class VirtualCat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50  
        self.energy = 50
        self.feed_count = 0
        self.interact_count = 0
        self.head_count = 0
        self.belly_count = 0
        self.toy_count = 0     

    def show_status(self):
        print(f"\n{self.name}'s status: happiness = {self.happiness}, energy = {self.energy}")
        if self.happiness < 50:
            print(f"{self.name} looks sad...")
            print_sad_cat_face()
        elif self.happiness <= 70:
            print(f"{self.name} looks fine.")
            print_cat_face()
        else:
            print(f"{self.name} is happily smiling at you!")
            print_happy_cat_face()
        if self.energy <= 40:
            print(f"{self.name} meows as if to say 'I'm hungry.'")
            print_sad_cat_face()

    def feed(self):
        if self.energy + 15 > 100:
            print(f"{self.name} is not hungry at this time, maybe play instead.")
        else:
            self.energy += 15
            self.feed_count += 1
            print(f"{self.name} eats happily, energy +15.")
            if self.energy > 100:
                self.energy = 100
        self.show_status()
        self.check_ending() 

    def interact(self):
        if self.energy <= 30:
            print(f"{self.name} is too hungry and tired to play. Please feed {self.name}.")
            return

        print("\nYou can choose: 1. Pat head 2. Pat belly 3. Play with toys")
        choice = input("Please enter option (1/2/3): ")
        
        if choice == "1":
            self.happiness += 10
            self.energy -= 5
            self.interact_count += 1
            self.head_count += 1
            print(f"You stroked {self.name}'s head. {self.name} purrs happily. happiness +10, energy -5")
        elif choice == "2":
            self.interact_count += 1
            self.belly_count += 1
            if self.happiness >= 80:
                self.happiness += 5
                print(f"{self.name} purrs softly. happiness +5")
            else:
                self.happiness -= 10
                self.energy -= 5
                print(f"{self.name} walks away unhappy. happiness -10, energy -5")
        elif choice == "3":
            self.happiness += 15
            self.energy -= 10
            self.interact_count += 1
            self.toy_count += 1
            print(f"You play with {self.name}. {self.name} has a lot of fun! happiness +15, energy -10")
        else:
            print("Invalid option, please select again.")
            return  # exit early to avoid showing status

        if self.happiness > 100:
            self.happiness = 100
        if self.energy > 100:
            self.energy = 100
        self.show_status()
        self.check_ending()

    def check_happy_ending(self):
        return self.happiness >= 90 and self.energy >= 90
    
    def check_ending(self):
        if self.happiness >= 90 and self.energy >= 90:
            print(f"\n{self.name} comes over to rub against you. {self.name} is very happy and truly loves you!")
            print_happy_cat_face()
            self.summary()
            print("Game Over!")
            exit()


    def summary(self):
        print("\n--- Interaction Summary ---")
        print(f"Total times fed: {self.feed_count}")
        print(f"Total interactions: {self.interact_count}")
        print(f"  - Pat head: {self.head_count}")
        print(f"  - Pat belly: {self.belly_count}")
        print(f"  - Play with toy: {self.toy_count}")
    


def print_happy_cat_face():
    print(r"""
 /\/\ 
(｡･ω･｡)
 /づ♡
""")

def print_sad_cat_face():
    print(r"""
 /\ /\  
(T . T)
 > ^ <  
""")

def main():
    print("Welcome to the virtual pet game!")
    cat_name = get_valid_name()
    cat = VirtualCat(cat_name)
    print(f"You adopted a kitten named {cat_name}. Let's see what they look like:")
    print_cat_face()

    while True:
        print("\nYou can choose from the following options:")
        print("1. Interact with your kitten")
        print("2. Feed your kitten")
        print("3. Check your kitten's status")
        print("4. End Game")
        action = input("Please enter your selection (1/2/3/4): ")

        if action == "1":
            cat.interact()
        elif action == "2":
            cat.feed()
        elif action == "3":
            cat.show_status()
        elif action == "4":
            h = cat.happiness
            e = cat.energy
            print()
            if h >= 90 and e >= 90:
                print(f"{cat.name} comes over to rub against you. {cat.name} is very happy and truly loves you!")
                print_happy_cat_face()
            elif h >= 90 and e < 90:
                print(f"{cat.name} really loves you, but {cat.name} seems hungry... Please take better care of the kitten next time.")
                print_sad_cat_face()
            elif h >= 50:
                print(f"{cat.name} feels fine about you, but you're not best friends yet. Keep trying!")
                print_cat_face()
            else:
                print(f"{cat.name} walks around... It seems {cat.name} doesn't like you very much.")
                print_sad_cat_face()
            cat.summary()
            print("Game Over!")
            break
        else:
            print("Enter a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
