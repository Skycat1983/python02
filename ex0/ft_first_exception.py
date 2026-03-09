

def check_temperature(temp_str: str) -> int:
    print("Testing temperature:", temp_str)
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
            return None

        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
            return None

        print(f"Temperature: {temp}°C is is perfect for plants!\n")
        return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input()->None:
    goodInput = '25'
    badInput = 'abc'
    extremeValues = ['100', '-50']
    tests = [goodInput, badInput, extremeValues]
    for test in tests:
        if len(test) > 1:
            arr = test
            for val in arr:
                check_temperature(val)
        else:
            check_temperature(test)

    # while


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    # temp = str(input("enter temp:"))

