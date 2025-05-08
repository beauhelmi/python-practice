import math


"""
Prompts the user for a weight on Earth
Prompts the user for choices of Planet
Prints out user weight on their chosen Planet
"""

MERCURY_FORMULA = 0.376
VENUS_FORMULA = 0.889
MARS_FORMULA = 0.378
JUPITER_FORMULA = 2.36
SATURN_FORMULA = 1.081
URANUS_FORMULA = 0.815
NEPTUNE_FORMULA = 1.14

def main():

    # Ask the user to enter their weight on Earth
    weight_on_earth = float(input("Please enter your weight on Earth: "))

    # Ask user to enter their PLanet
    # strip and capitalize is use to format user input
    planet = input("Enter a planet:").strip().capitalize()

    # Use if/elif for different planet formula
    # Depends on user input
    if planet == "Mercury":
        gravity_constant = MERCURY_FORMULA
    elif planet == "Venus":
        gravity_constant = VENUS_FORMULA
    elif planet == "Mars":
        gravity_constant = MARS_FORMULA
    elif planet == "Jupiter":
        gravity_constant = JUPITER_FORMULA
    elif planet == "Saturn":
        gravity_constant = SATURN_FORMULA
    elif planet == "Uranus":
        gravity_constant = URANUS_FORMULA
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_FORMULA
    else:
        print("Invalid planet name.")
        return

    planet_weight = weight_on_earth * gravity_constant

    rounded_planet_weight = round(planet_weight, 2)

    print(f"The equivalent weight on {planet}: {rounded_planet_weight}")

if __name__ == "__main__":
    main()
