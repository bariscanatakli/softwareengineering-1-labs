

class Car():
    def __init__(self, max_velocity, current_velocity):
        super().__init__()
        self.max_velocity = max_velocity
        self.current_velocity = current_velocity
    def accelerate(self):
        if self.max_velocity > self.current_velocity:
            self.current_velocity += 10
        else:
            print("You are reached the max velocity.")
    def decelerate(self):
        if self.max_velocity >= 10:
            self.current_velocity -= 10
        else:
            print("You stopped")

    def showVelocity(self):
        print(self.current_velocity)


ferrari = Car(200,0)

for decelareteRange in range(18):
    ferrari.accelerate()


ferrari.showVelocity()