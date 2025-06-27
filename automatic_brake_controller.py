from openai import OpenAI


class AutomaticBrakeController:
    """
    This class uses an AI model to determine braking decisions
    based on speed, distance, and road conditions.
    """

    def __init__(self, speed_limit):
        self.speed_limit = speed_limit  # km/h
        self.client = OpenAI()  # You'd need your API key configured

    def decide_action(self, current_speed, distance_to_vehicle, road_condition):
        """
        Calls an AI model with a prompt describing the driving context
        and retrieves the recommended action.
        """
        prompt = (
            f"You are an autonomous vehicle control system.\n"
            f"Current speed: {current_speed} km/h\n"
            f"Distance to vehicle ahead: {distance_to_vehicle} meters\n"
            f"Road condition: {road_condition}\n"
            f"Speed limit: {self.speed_limit} km/h\n\n"
            "Decide the best action to maintain safety and comfort.\n"
            "Respond with one word: 'brake', 'maintain', or 'accelerate'."
        )

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a vehicle control AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        action = response.choices[0].message.content.strip().lower()
        return action

# Example usage:
# controller = AutomaticBrakeController(speed_limit=100)
# action = controller.decide_action(current_speed=90, distance_to_vehicle=5, road_condition="wet")
# print("AI recommends:", action)
