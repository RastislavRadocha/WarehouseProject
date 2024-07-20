import random
import string
import time
import datetime
from locations import Location


def generate_custom_id():
    # Get the current date
    timestamp = datetime.date.today()

    # Generate a random string of 10 characters using lowercase letters and digits
    # Instead of creating a random string of 10 characters, we are using 6 letters and 4 digits
    random_letters = random.choices(string.ascii_lowercase, k=6)
    random_digits = random.choices(string.digits, k=4)

    random_chars = ''.join(random_letters + random_digits)

    # Combine the random characters and timestamp to create a custom ID
    return f"ID:{random_chars}, Pallet created:{timestamp}"


custom_id = generate_custom_id()

print(custom_id)


def generate_pallets(pallets):
    """
    Generates a list of pallets with a given number of pallets.

    Args:
        pallets (int): The number of pallets to generate.

    Returns:
        list: A list of pallets.
    """

    # Initialize an empty list to store the generated pallets
    generated_pallets = []

    # Generate the specified number of pallets
    for _ in range(pallets):
        # Generate a custom ID for each pallet
        pallet = generate_custom_id()

        # Append the generated pallet to the list of pallets
        generated_pallets.append(pallet)

    # Return the list of generated pallets
    return generated_pallets


def main():
    # Ask the user for the number of pallets to generate and convert it to an integer
    num_pallets: int = int(input("How many pallets you want to generate?: "))

    # Generate pallets based on the user's input
    generated_pallets = generate_pallets(num_pallets)

    # Iterate through the generated pallets and display them with an index starting from 1
    for idx, pallet in enumerate(generated_pallets):
        print(f"{idx + 1}: {pallet}")

    loading_input: int = int(input("How many pallets would you like to load?: "))
    loaded_pallets = generated_pallets[:loading_input]


    # The last argument `location=generated_pallets` is used to pass the generated pallets to the `Location` class
    # as an initial value for the `location` attribute. This allows the `Location` class to have access to the
    # generated pallets when it is initialized.
    temporary_location: Location = Location('Temporary Location 1', 250, location=generated_pallets)

    overflow1: Location = Location('Overflow1', 50, location=generated_pallets)

    remaining_pallets = overflow1.load_pallet(pallets=loaded_pallets, limit_over=overflow1.limit)

    temporary_location.load_pallet(pallets=remaining_pallets, limit_over=temporary_location.limit)

    print(f"Temporary Location Pallets: {len(remaining_pallets)}")
    print(f"Overflow1 Pallets: {len(overflow1.pallets)}")



if __name__ == '__main__':
    main()
