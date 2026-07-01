#MeltFocus (Python Logic)

import random
import time
from dataclasses import dataclass, field

# Helper
def clamp(value, minimum=0.0, maximum=1.0):
    return max(minimum, min(maximum, value))

# Melting Objects
class Candle:
    def __init__(self):
        self.max_height = 180
        self.height = self.max_height
        self.flame_size = 1.0
        self.wax_puddle = 0.0
        self.drips = 0

    def update(self, progress):
        progress = clamp(progress)

        self.height = self.max_height * (1 - progress)
        self.flame_size = max(0.0, 1 - progress * 0.8)
        self.wax_puddle = progress

        if random.random() < 0.03:
            self.drips += 1


class IceCube:
    def __init__(self):
        self.size = 1.0
        self.opacity = 1.0
        self.roundness = 0.0
        self.water_puddle = 0.0
        self.droplets = 0

    def update(self, progress):
        progress = clamp(progress)

        self.size = 1 - progress
        self.opacity = max(0.2, 1 - progress * 0.8)
        self.roundness = progress
        self.water_puddle = progress

        if random.random() < 0.03:
            self.droplets += 1

# Hidden Timer
class HiddenTimer:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.duration = random.randint(minimum, maximum)
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start_time

    @property
    def progress(self):
        return clamp(self.elapsed / self.duration)

    @property
    def finished(self):
        return self.progress >= 1

# Statistics
@dataclass
class Statistics:
    sessions: int = 0
    total_minutes: float = 0
    longest_session: float = 0
    streak: int = 0
    history: list = field(default_factory=list)

    def add(self, minutes):
        self.sessions += 1
        self.total_minutes += minutes
        self.longest_session = max(self.longest_session, minutes)
        self.streak += 1

        self.history.append(minutes)

        if len(self.history) > 7:
            self.history.pop(0)

    @property
    def average(self):
        if self.sessions == 0:
            return 0
        return self.total_minutes / self.sessions

# Main Application
class MeltFocus:

    def __init__(self):

        self.statistics = Statistics()

        self.mode = None
        self.object = None
        self.timer = None

    def choose(self, mode):

        mode = mode.lower()

        if mode == "candle":
            self.object = Candle()

        elif mode == "ice":
            self.object = IceCube()

        else:
            raise ValueError("Choose 'candle' or 'ice'.")

        self.mode = mode

    def start(self, minimum_minutes, maximum_minutes):

        self.timer = HiddenTimer(
            minimum_minutes * 60,
            maximum_minutes * 60
        )

        self.timer.start()

        print("\nStudy session started.")
        print("The duration has been hidden.")
        print("Watch the melting object instead of a timer.\n")

    def update(self):

        p = self.timer.progress

        self.object.update(p)

        return p

    def finish(self):

        minutes = self.timer.duration / 60

        self.statistics.add(minutes)

        print("\nSession Complete!")
        print(f"Hidden Duration : {minutes:.1f} minutes")

        print("\nStatistics")
        print("----------------------")
        print("Sessions :", self.statistics.sessions)
        print("Total    :", round(self.statistics.total_minutes, 1), "minutes")
        print("Average  :", round(self.statistics.average, 1), "minutes")
        print("Longest  :", round(self.statistics.longest_session, 1), "minutes")
        print("Streak   :", self.statistics.streak)

# Demonstration
if __name__ == "__main__":

    app = MeltFocus()

    choice = input("Choose object (candle/ice): ").strip().lower()

    minimum = int(input("Minimum study time (minutes): "))
    maximum = int(input("Maximum study time (minutes): "))

    app.choose(choice)
    app.start(minimum, maximum)

    while not app.timer.finished:

        progress = app.update()

        if choice == "candle":
            print(
                f"\rCandle | "
                f"Height: {app.object.height:6.1f} "
                f"| Wax: {app.object.wax_puddle:.0%}",
                end=""
            )

        else:
            print(
                f"\rIce | "
                f"Size: {app.object.size:.0%} "
                f"| Water: {app.object.water_puddle:.0%}",
                end=""
            )

        time.sleep(0.2)

    app.finish()