class AutonomousCar:
    def __init__(self, model, speed=0):
        self.model = model
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"The car accelerates to {self.speed} km/h.")

    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"The car slows down to {self.speed} km/h.")

    def get_speed(self):
        return self.speed

    def get_model(self):
        return self.model