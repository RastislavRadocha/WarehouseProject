import pandas as pd
import os
import openpyxl


class Pallet:
    def __init__(self, pallet_id):
        self.id = pallet_id

    def storing_pallet(self, file_path: str, pallets: list) -> None:
        """
        Store the pallet IDs in a pandas DataFrame and write it to an Excel file.

        Args:
            file_path (str): The path to the Excel file.
            pallets (list): A list of Pallet objects.

        Returns:
            None
        """
        # Extract the pallet IDs from the pallets list
        pallet_ids = [pallet.id for pallet in pallets]

        # Create a dictionary with the pallet IDs as values
        new_data = {'Pallet ID': pallet_ids}

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
        with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='replace') as writer:
            combined_df.to_excel(writer, sheet_name="Testing_sheet", index=False, header=True)
