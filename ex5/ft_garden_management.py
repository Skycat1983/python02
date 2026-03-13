# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 15:32:42 by helaouta          #+#    #+#              #
#    Updated: 2026/03/13 12:02:24 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun

    @property
    def status(self) -> tuple[int, int]:
        return (self.water, self.sun)


class GardenManager:
    def __init__(self, water: int) -> None:
        self._water = water
        self._next_plant_id = 1
        self._plants: dict[int, Plant] = {}

    @property
    def water(self) -> int:
        return self._water

    def add_plant(self, name: str, water: int, sun: int) -> None:
        self.validate_str(name)
        self.validate_int("Water level", water, 10, 1)
        self.validate_int("Sunlight hours", sun, 12, 2)

        plant = Plant(name, water, sun)
        plant_id = self._next_plant_id
        self._plants[plant_id] = plant
        self._next_plant_id += 1
        print(f"Added {name} successfully")

    def water_plant(self, plant: Plant) -> None:
        plant.water += 1
        self._water -= 1

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for _, plant in self._plants.items():
                if self.water == 0:
                    raise WaterError("Not enough water in tank")
                self.water_plant(plant)
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> None:
        water, sun = plant.status
        self.validate_int("Water level", water, 10, 1)
        self.validate_int("Sunlight hours", sun, 12, 2)
        print(f"{plant.name}: healthy (water: {water}, sun: {sun})")

    def check_plants_health(self) -> None:
        for _, plant in self._plants.items():
            try:
                self.check_plant_health(plant)
            except PlantError as e:
                print(f"Error checking {plant.name}: {e}")

    @staticmethod
    def validate_str(name: str) -> None:
        if len(name) == 0:
            raise PlantError("Plant name cannot be empty!")

    @staticmethod
    def validate_int(label: str, value: int, high: int, low: int) -> None:
        if value > high:
            raise PlantError(f"{label} {value} is too high (max {high})")
        if value < low:
            raise PlantError(f"{label} {value} is too low (min {low})")


def test_garden_management() -> None:
    manager = GardenManager(5)

    print("Adding plants to garden...")

    try:
        manager.add_plant("tomato", 5, 8)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("lettuce", 4, 6)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("", 3, 7)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nChecking plant health...")
    try:
        manager.check_plants_health()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()