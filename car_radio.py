class CarRadio:
    def __init__(self):
        self.volume = 50  # Default volume level
        self.station = "101.1 FM"  # Default radio station

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"Volume set to {self.volume}")
        else:
            print("Volume must be between 0 and 100")

    def change_station(self, station):
        self.station = station
        print(f"Station changed to {self.station}")

    def get_status(self):
        return f"Current station: {self.station}, Volume: {self.volume}"