class Hero:
    def __init__(self, name, age, hero_type):
        self.name = name
        self.age = age
        self.hero_type = hero_type

    def attack(self):
        if self.hero_type == "mage":
            attack_description = "magic"
        elif self.hero_type == "warrior":
            attack_description = "sword"
        elif self.hero_type == "monk":
            attack_description = "martial arts"
        elif self.hero_type == "ninja":
            attack_description = "shuriken"
        else:
            attack_description = "unknown weapon"

        print(f"The {self.hero_type} attacked using {attack_description}.")


# Example usage:
hero1 = Hero("Aragon", 30, "warrior")
hero1.attack()

hero2 = Hero("Gandalf", 150, "mage")
hero2.attack()

hero3 = Hero("Liang", 25, "monk")
hero3.attack()

hero4 = Hero("Shadow", 28, "ninja")
hero4.attack()
