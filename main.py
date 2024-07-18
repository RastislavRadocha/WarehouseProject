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


def generate_pallets(num_pallets):
    """
    Generates a list of pallets with a given number of pallets.

    Args:
        num_pallets (int): The number of pallets to generate.

    Returns:
        list: A list of pallets.
    """

    # Initialize an empty list to store the generated pallets
    pallets = []

    # Generate the specified number of pallets
    for _ in range(num_pallets):
        # Generate a custom ID for each pallet
        pallet = generate_custom_id()

        # Append the generated pallet to the list of pallets
        pallets.append(pallet)

    # Return the list of generated pallets
    return pallets


def main():
    # Ask the user for the number of pallets to generate and convert it to an integer
    num_pallets: int = int(input("How many pallets you want to generate?: "))

    # Generate pallets based on the user's input
    generated_pallets = generate_pallets(num_pallets)

    # Iterate through the generated pallets and display them with an index starting from 1
    for idx, pallet in enumerate(generated_pallets):
        print(f"{idx + 1}: {pallet}")

    overflow1: Location = Location('Overflow1', 50)
    overflow1.load_pallet(num_pallets)
    overflow1_limit = overflow1.get_limit()
    print(f"Current limit: {overflow1_limit}")




if __name__ == '__main__':
    while True:
        main()
