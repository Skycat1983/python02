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
