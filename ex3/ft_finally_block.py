class Plant:
    def __init__(self, name: str) -> None:
        self.name = name

def water_plants(plant_list: list[Plant])->None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            name = plant.name
            if not isinstance(name, str):
                raise ValueError(f"Error: Cannot water {name} - invalid plant!")
            print(f"Watering {plant.name}")
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")

    tomato = Plant("tomato")
    lettuce = Plant("lettuce")
    carrots = Plant("carrots")
    invalid = Plant(None)

    print("Testing normal watering")
    plant_list = [tomato, lettuce, carrots]
    water_plants(plant_list)
    print("Watering completed successfully!")

    print("\nTesting with error")
    plant_list_invalid = [tomato, invalid, carrots]
    water_plants(plant_list_invalid)

    print("\nCleanup always happens, even with errors!")
    