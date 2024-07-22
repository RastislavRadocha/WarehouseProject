import pandas as pd


class Pallet:
    def __init__(self, pallet_id):
        self.id = pallet_id

    def storing_pallet(self, file_path, pallets):  # Method for creating Excel file for storing data(pallets)
        pallet_ids = [pallet.id for pallet in pallets]
        data = {'Pallet ID': pallet_ids}
        df = pd.DataFrame(data, index=range(1, len(pallets) + 1))

        with pd.ExcelWriter('C:/Users/skill/PycharmProjects/WarehouseProject/generated_pallets.xlsx') as writer:
            df.to_excel(writer, sheet_name="Testing_pallets", index=False, header=True)
