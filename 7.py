class Robot:
    def introduce_self(self):
        print("my name is " + self.name)



r1 = Robot()
r1.name = 'tom'

r2 = Robot( )
r2.name = "Jerry"

r1.introduce_self()
r2.introduce_self()