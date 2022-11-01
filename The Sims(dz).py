import random
class Girl:
    def __init__(self, name = "Girl", chores = None, home = None, job = None):
        self.name = name
        self.money = 300
        self.gladness = 50
        self.satiety = 50
        self.chores = chores
        self.home = home
        self.job = job
    def get_home(self):
        self.home = Chores()
    def get_job(self):
        self.job = Girl()
    def eat(self):
        print("Need to eat")
        self.satiety += 9
    def bath(self):
        print("Need to take a shower")
        self.gladness += 3
    def chill(self):
        print("Whhhh. Need to chill")
        self.gladness += 9

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
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
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\n So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
                print("Start working")
                self.work()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")


class Chores:
    def __init__(self, home = None, car = None):
        self.money = 300
        self.home = home
        self.car = car
        self.clean = 70
    def cleaning(self):
        print("The house is dirty. Let`s clean")
        self.clean += 15
    def to_repair(self):
        self.car.strength += 100
        self.money -= 60
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50

    def brand(self):
        brand = brands_of_car


    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)


job_list = {
 "Web designer":
 {"salary":70, "gladness_less": 3 },
 "Сonfectioner":
 {"salary":45, "gladness_less":8 },
 "Beautician":
 {"salary":65, "gladness_less": 10 },
 "Volonteer":
 {"salary":40, "gladness_less": 1 },
 }
brands_of_car = {
 "BMW":{"fuel":100, "strength":100,
 "consumption": 6},
 "Lada":{"fuel":50, "strength":40,
 "consumption": 10},
 "Volvo":{"fuel":70, "strength":150,
 "consumption": 8},
 "Ferrari":{"fuel":80, "strength":120,
 "consumption": 14},
 }
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
alice = Girl(name="Alice")
for day in range(1,8):
    if alice.live(day) == False:
        break




, Literature, Sport, Informatics, English, Biology, Geography, Physics
print("Math", randint(1,12))
    print("Literature", randint(1, 12))
    print("Sport", randint(1, 12))
    print("Informatics", randint(1, 12))
    print("English", randint(1, 12))
    print("Biology", randint(1, 12))
    print("Geography", randint(1, 12))
    print("Physics", randint(1, 12))