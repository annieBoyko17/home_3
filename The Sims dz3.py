import random
class Human:
    def __init__(self, name = "Human", home = None, study = None, lesson = None):
        self.name = name
        self.home = home
        self.study = study
        self.gladness = 50
        self.money = 300
        self.satiety = 50
        self.lesson = lesson

    def get_home(self):
        self.home = House()
    def get_study(self):
        self.study = Study
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 10
            self.home.food -= 5

    def chill(self):
        self.gladness += 10
        self.home.mess += 3

    def shopping(self, manage):
        if manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        print(f"Study - {self.lesson}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.study is None:
            self.get_study()
            print(f"I need to study. Let`s studing")
        self.days_indexes(day)
        dice = random.randint(1, 3)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\n So I will clean the house")
                self.cleaning()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
                print("Start study harder")
                self.study()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start study")
            self.study()
        elif dice == 3:
            print("Cleaning time!")
            self.cleaning()

    def cleaning(self):
        self.gladness -= 5
        self.home.mess = 0


class House:

    def shopping(self, manage, money, home):
        self.home = home
        self.money = 300
        if manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50

    def __init__(self):
        self.mess = 0
        self.food = 0

    def cleaning(self, gladness):
        self.gladness = 50
        self.gladness -= 5
        self.home.mess = 0

class Study:
    def study_money(self, money, lesson):
        self.money += 50
        self.lesson = print("Math, English, Informatics")

emily = Human(name="Emily", study=None)
for day in range(1,8):
    if emily.live(day) == False:
        break