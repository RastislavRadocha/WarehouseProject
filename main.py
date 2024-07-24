import random
import string
import openpyxl
import pandas as pd
import time
import datetime
import customtkinter as ctk
from pallet import Pallet
from locations import Location

# Define and initialize a Pallet object with the name 'Testing_sheet'
# Call the storing_pallet method on the store_pallet object
# to store the pallet data in the Excel file 'generated_pallets.xlsx'
store_pallet: Pallet = Pallet('Testing_sheet')


def generate_custom_id():
    # Get the current date
    timestamp = datetime.date.today()

    # Generate a random string of 10 characters using lowercase letters and digits
    # Instead of creating a random string of 10 characters, we are using 6 letters and 4 digits
    random_letters = random.choices(string.ascii_lowercase, k=6)
    random_digits = random.choices(string.digits, k=4)

    random_chars = ''.join(random_letters + random_digits)

    return f"ID:{random_chars}"



def generate_pallets(pallets_id):
    """
    Generates a list of pallets with a given number of pallets.

    Args:
        pallets_id (int): The number of pallets to generate.

    Returns:
        list: A list of pallets.
        :param pallets_id:
    """

    # Initialize an empty list to store the generated pallets
    generated_pallets = []

    # Generate the specified number of pallets
    for _ in range(pallets_id):
        # Generate a custom ID for each pallet
        id_value = generate_custom_id()
        pallet_id = f"Pallet ID: {id_value}"
        pallet = Pallet(pallet_id)

        # Append the generated pallet to the list of pallets
        generated_pallets.append(pallet)

    # Return the list of generated pallets
    return generated_pallets


def main():
    # Ask the user for the number of pallets to generate and convert it to an integer
    num_pallets: int = int(input("How many pallets you want to generate?: "))

    # Generate pallets based on the user's input
    generated_pallets = generate_pallets(num_pallets)

    store_pallet.storing_pallet(file_path='C:/Users/skill/PycharmProjects/WarehouseProject/generated_pallets.xlsx',
                                pallets=generated_pallets, timestamp=datetime.datetime.now())

    # Iterate through the generated pallets and display them with an index starting from 1
    for idx, pallet in enumerate(generated_pallets):
        print(f"{idx + 1}: {pallet.id}")

    loading_input: int = int(input("How many pallets would you like to load?: "))
    loaded_pallets = generated_pallets[:loading_input]

    # The last argument `location=generated_pallets` is used to pass the generated pallets to the `Location` class
    # as an initial value for the `location` attribute. This allows the `Location` class to have access to the
    # generated pallets when it is initialized.
    temporary_location: Location = Location('Temporary Location 1', 250, location=generated_pallets)

    overflow1: Location = Location('Overflow1', 50, location=generated_pallets)

    over_pallets = overflow1.load_pallet(pallets=loaded_pallets, limit_over=overflow1.limit)
    remaining_pallets = generated_pallets[loading_input:]

    temporary_location.load_pallet(pallets=over_pallets, limit_over=temporary_location.limit)

    print(f"Temporary Location Pallets: {[p.id for p in temporary_location.pallets]}")
    print(f"Overflow1 Pallets: {[p.id for p in overflow1.pallets]}")
    print(f"Unloaded Pallets: {[p.id for p in remaining_pallets]}")


if __name__ == '__main__':
    main()
