from src.utils.prompt_executer import PromptExecuter


class SpeedChanger:
    def __init__(self, speed=1.0):
        self.speed = speed
        prompt = (
            "You are controlling an autonomous vehicle driving on a multi-lane road. Continuously monitor the vehicle’s current speed, the posted speed limit, the distance to the vehicle ahead, and road conditions (wet, dry, icy). Adjust the throttle and brakes to maintain a safe following distance and comply with the speed limit.\n"
            "Rules:\n"
            "If the car is within 5 meters of the vehicle ahead, gradually decelerate to increase the gap.\n"
            "Never exceed the posted speed limit.\n"
            "If road conditions are wet or icy, reduce speed by 20%.\n"
            "Aim for smooth acceleration and braking to ensure passenger comfort.\n"
            "Output:\n"
            "Provide the recommended target speed in km/h and indicate whether to accelerate, maintain, or decelerate."
        )
        self.prompt_executer = PromptExecuter(prompt)

    def change_speed(self, new_speed):
        self.prompt_executer.execute()

        if new_speed <= 0:
            raise ValueError("Speed must be greater than 0")
        self.speed = new_speed

    def get_speed(self):
        return self.speed

    def apply_speed(self, value):
        return value * self.speed