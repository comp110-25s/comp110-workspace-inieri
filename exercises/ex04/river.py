"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        fish_temp: list[Fish] = self.fish.copy()
        bear_temp: list[Bear] = self.bears.copy()
        for fish in self.fish:
            if fish.age > 3:
                fish_temp.remove(fish)
        self.fish = fish_temp
        for bear in self.bears:
            if bear.age > 5:
                bear_temp.remove(bear)
        self.bears = bear_temp
        return None

    def bears_eating(self):
        while len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        bear_temp2: list[Bear] = self.bears.copy()
        for bear in bear_temp2:
            if bear.hunger_score < 0:
                bear_temp2.remove(bear)
        self.bears = bear_temp2
        return None

    def repopulate_fish(self):
        num_new_fish = (len(self.fish) // 2) * 4
        index = 0
        while index < num_new_fish:
            self.fish.append(Bear())
            count += 1
        return None

    def repopulate_bears(self):
        num_new_bears = len(self.bears) // 2
        index = 0
        while index < num_new_bears:
            self.bears.append(Bear())
            count += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        index: int = 0
        while index <= amount:
            self.fish.pop(0)
            index += 1
