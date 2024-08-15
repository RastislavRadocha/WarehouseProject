import pandas as pd
import os
import openpyxl
import string
import random


class Pallet:
    def __init__(self, pallet_id):
        self.id = pallet_id

    def storing_pallet(self, file_path: str, pallets: list, timestamp) -> None:
        """
        Store the pallet IDs in a pandas DataFrame and write it to an Excel file.

        Args:
            file_path (str): The path to the Excel file.
            pallets (list): A list of Pallet objects.

        Returns:
            None
            :param file_path:
            :param pallets:
            :param timestamp:
        """
        # Extract the pallet IDs from the pallets list
        pallet_ids = [pallet.id for pallet in pallets]

        # Create a dictionary with the pallet IDs as values
        new_data = {'Pallet ID': pallet_ids, 'Date': [timestamp] * len(pallet_ids)}

        # Create a pandas DataFrame with the pallet IDs and an index
        new_df = pd.DataFrame(new_data, index=range(1, len(pallets) + 1))
        if os.path.exists(file_path):
            try:
                existing_df = pd.read_excel(file_path, sheet_name='Testing_sheet')
                combined_df = pd.concat([new_df, existing_df], ignore_index=True)
            except ValueError:
                combined_df = new_df
        else:
            combined_df = new_df

        # Write the DataFrame to an Excel file
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='r+', if_sheet_exists='replace') as writer:
            combined_df.to_excel(writer, sheet_name="Testing_sheet", index=False, header=True)

    def generate_custom_id(self):
        # Generate a random string of 10 characters using lowercase letters and digits
        # Instead of creating a random string of 10 characters, we are using 6 letters and 4 digits
        random_letters = random.choices(string.ascii_lowercase, k=6)
        random_digits = random.choices(string.digits, k=4)

        random_chars = ''.join(random_letters + random_digits)

        return f"ID:{random_chars}"

    def generating_pallets(self, pallets_id):
        generated_pallets = []

        for _ in range(pallets_id):
            id_value = self.generate_custom_id()
            pallet_id = f"Pallet ID: {id_value}"
            generated_pallets.append(pallet_id)

        return generated_pallets
