# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/09 14:35:22 by helaouta          #+#    #+#              #
#    Updated: 2026/03/09 14:36:49 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



# Write a function garden_operations() that demonstrates these common errors:
# • ValueError - when someone gives bad data (like "abc" instead of a number)
# • ZeroDivisionError - when you try to divide by zero
# • FileNotFoundError - when you try to open a file that doesn’t exist
# • KeyError - when you look for something that isn’t in a dictionary

# Create a test_error_types() function that:
# • Shows each type of error happening
# • Catches each error and explains what went wrong
# • Demonstrates that your program continues running after each error
# • Shows how to catch multiple error types with one except block

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