import random
class FootballPlayer:
    def __init__(self,name,power,position,nationality,club) -> None:
        self.name=name
        self.power=power
        self.position=position
        self.nationality=nationality
        self.club=club
        
    def kick(self):
        print(self.name,"kick the ball",self.power*0.7,"meter")
        
    def tackle(self,target):
        print(self.name,"tackling",target.name,end=" ")
        realpower=self.power+random.randint(-5,5)
        realtpower=target.power+random.randint(-5,5)
        if (realpower>=realtpower):
            print("successfully and take the ball")
            return True
        else:
            print("but failed")
            return False
    def getball(self):
        print(self.name,"get the ball")
    def goal(self):
        print("gooooooooooooaaaaaallll!!!!!!!",self.name,"he scored the goal","1 point for",self.club)
        
class Keeper(FootballPlayer):
    def __init__(self, name, power, position, nationality, club) -> None:
        super().__init__(name, power, position, nationality, club)
    def catchball(self):
        success=random.randint(0,100)
        success+=self.power/10
        if(success>50):
            print(self.name,"successfully catch the ball")
            return True
        else:
            print(self.name,"failed to catch the ball")
            return False