# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    backup.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 15:32:42 by helaouta          #+#    #+#              #
#    Updated: 2026/03/13 11:17:21 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class WaterTank:
    def __init__(self, water_level: int) -> None:
        self._water_level = water_level

    @property
    def water_level(self) -> int:
        return self._water_level

    def add_water(self, water_added: int) -> None:
        self._water_level += water_added

    def use_water(self)->None:
        if self.water_level == 0:
            raise ValueError("Not enough water in tank")
        else:
            self._water_level = (self._water_level - 1)



class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun

    @property
    def status(self)->list[int, int]:
        return list[self.water, self.sun]


class GardenManager:
    def __init__(self) -> None:
        self._water_tank = WaterTank(0)
        self._plants: dict[int, Plant] = {}
        self._next_plant_id = 1

    @property
    def water_tank(self)->WaterTank:
        return (self._water_tank)

    def add_plant(self, name: str, water: int, sun: int) -> None:
        self.validate_str(name)
        self.validate_int("Water level", water, 10, 1)
        self.validate_int("Sunlight hours", sun, 12, 2)
        plant = Plant(name, water, sun)
        plant_id = self._next_plant_id
        self._plants[plant_id] = plant
        self._next_plant_id += 1
        print(f"Added {name} successfully")

    def water_plant(self, plant: Plant)->None:
        plant.water = plant.water + 1

    def water_plants(self)->None:
        print("Opening Watering system")
        try:
            plants = self._plants.items()
            for [_, plant] in plants:
                self.water_tank.use_water()
                self.water_plant(plant)
                print(f"Watering {plant.name} - success")
        except ValueError as e:
            raise ValueError(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant:Plant)->None:
        [water, sun] = plant.status
        try:
            self.validate_int("water", water, 10, 1)
            self.validate_int("sun", sun, 12, 2)
            print(f"")
        except ValueError as e:
            raise ValueError(f"Error checking {plant.name}: {e}")


    def check_plants_health(self)->None:
        try:
            plants = self._plants.items()
            for [_, plant] in plants:
                plant.status()
        except ValueError as e:
            raise ValueError(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def validate_str(name: str) -> None:
        if len(name) == 0:
            raise ValueError("Error: Name cannot be empty")

    @staticmethod
    def validate_int(label: str, value: int, high: int, low: int) -> None:
        if value > high:
            raise ValueError(f"Error: {label} {value} is too high (max {high})")
        if value < low:
            raise ValueError(f"Error: {label} {value} is too low (min {low})")


def test_garden_management() -> None:
    manager = GardenManager()

    print("Adding plants to garden...")

    try:
        manager.add_plant("tomato", 5, 8)
    except ValueError as e:
        print(e)

    try:
        manager.add_plant("lettuce", 4, 6)
    except ValueError as e:
        print(e)

    try:
        manager.add_plant("", 3, 7)
    except ValueError as e:
        print(e)

    print("Watering plants...")
    try:
        manager.water_plants()
    except ValueError as e:
        print(e)

    print("Checking plant health...")
    try:
        manager.check_plants_health()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()