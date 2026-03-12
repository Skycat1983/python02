# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/09 15:26:06 by helaouta          #+#    #+#              #
#    Updated: 2026/03/09 15:39:51 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# Create these simple custom exception classes:
# • GardenError - A basic error for garden problems
# • PlantError - For problems with plants (inherits from GardenError)
# • WaterError - For problems with watering (inherits from GardenError)
# Each custom exception should:
# • Be a simple class that inherits from Exception (or GardenError)
# • Have a helpful error message
# • Be easy to catch and handle
# Create functions that:
# • Raise your custom errors in different situations
# • Show how to catch your specific error types
# • Demonstrate that catching GardenError catches all garden-related errors

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class WaterTank:
    def __init__(self, water_level: int) -> None:
        self.water_level = water_level

    def check_status(self) -> None:
        if self.water_level == 0:
            raise WaterError("Not enough water in the tank!")


class Plant:
    def __init__(self, dryness: int) -> None:
        self.dryness = dryness

    def check_status(self) -> None:
        if self.dryness == 0:
            raise PlantError("The tomato plant is wilting!")


class Garden:
    def __init__(self, water_tank: WaterTank, plant: Plant) -> None:
        self.water_tank = water_tank
        self.plant = plant

    def check_status(self) -> None:
        self.plant.check_status()
        self.water_tank.check_status()


def test_plant_error() -> None:
    print("Testing PlantError...")
    water_tank = WaterTank(5)
    plant = Plant(0)
    garden = Garden(water_tank, plant)

    try:
        garden.plant.check_status()
    except PlantError as error:
        print("Caught PlantError:", error)


def test_water_error() -> None:
    print("\nTesting WaterError...")
    water_tank = WaterTank(0)
    plant = Plant(5)
    garden = Garden(water_tank, plant)

    try:
        garden.water_tank.check_status()
    except WaterError as error:
        print("Caught WaterError:", error)


def test_garden_error() -> None:
    print("\nTesting catching all garden errors...")

    water_tank = WaterTank(0)
    plant = Plant(0)
    garden = Garden(water_tank, plant)

    try:
        garden.plant.check_status()
    except GardenError as error:
        print("Caught a garden error:", error)

    try:
        garden.water_tank.check_status()
    except GardenError as error:
        print("Caught a garden error:", error)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    test_water_error()
    test_garden_error()
    print("\nAll custom error types work correctly!")

    # temp = str(input("enter temp:"))


# $> python3 ft_custom_errors.py
# === Custom Garden Errors Demo ===
# Testing PlantError...
# Caught PlantError: The tomato plant is wilting!
# Testing WaterError...
# Caught WaterError: Not enough water in the tank!
# Testing catching all garden errors...
# Caught a garden error: The tomato plant is wilting!
# Caught a garden error: Not enough water in the tank!
# All custom error types work correctly!