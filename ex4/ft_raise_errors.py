# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_errors.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 14:02:40 by helaouta          #+#    #+#              #
#    Updated: 2026/03/12 14:30:31 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> str:

    if len(plant_name) == 0:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"



def test_plant_checks() -> None:

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 5, 8))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting water level minimum boundary...")
    try:
        print(check_plant_health("tomato", 1, 8))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting water level below minimum...")
    try:
        print(check_plant_health("tomato", 0, 8))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting water level maximum boundary...")
    try:
        print(check_plant_health("tomato", 10, 8))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting water level above maximum...")
    try:
        print(check_plant_health("tomato", 11, 8))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting sunlight minimum boundary...")
    try:
        print(check_plant_health("tomato", 5, 2))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting sunlight below minimum...")
    try:
        print(check_plant_health("tomato", 5, 1))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting sunlight maximum boundary...")
    try:
        print(check_plant_health("tomato", 5, 12))
    except ValueError as e:
        print("Error:", e)


    print("\nTesting sunlight above maximum...")
    try:
        print(check_plant_health("tomato", 5, 13))
    except ValueError as e:
        print("Error:", e)




if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()