class Robot:
    def __init__(self, name):
        self.name = name      

    def introduce(self):    
        print("Hello! I am a robot")
        print("My name is:", self.name)
        
if __name__ == "__main__":
    r1 = Robot("Robo")
    r1.introduce()
