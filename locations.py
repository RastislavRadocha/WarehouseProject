class Location:
    def __init__(self, name: str, limit: int):
        self.name = name
        self.limit = limit

    def load_pallet(self, num_pallets):
        self.limit -= num_pallets
        print(f"{num_pallets} pallets loaded into {self.name}")
        if self.limit == 0:
            print(f"Cannot load more pallets. Current limit {self.limit} for {self.name}")

    def unload_pallet(self, num_pallets):
        self.limit += num_pallets

    def get_limit(self):
        return self.limit

    def get_name(self):
        return self.name
