def cause_value_error() -> None:
    int("1o")


def cause_zero_division() -> None:
    10 / 0


def cause_file_not_found() -> None:
    file = open("missing.txt")
    file.close()


def cause_key_error() -> None:
    plants = {"tomato": 5}
    print(plants["lettuce"])


def garden_operations(operation) -> None:
    operation()


def test_error_types() -> None:
    tests = {
        "ValueError": cause_value_error,
        "ZeroDivisionError": cause_zero_division,
        "FileNotFoundError": cause_file_not_found,
        "KeyError": cause_key_error,
    }

    for name, func in tests.items():
        print(f"Testing {name}...")
        try:
            garden_operations(func)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except KeyError as e:
            print(f"Caught KeyError: {e}")
        print()

    print("Testing multiple errors together...")
    try:
        garden_operations(cause_value_error)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    