class Location:
    def __init__(self, name: str, limit: int, location: list = []):
        self.name = name
        self.limit = limit
        self.pallets = []
        self.remaining_pallets = []
        self.pallets_to_relocate = []

    def load_pallet(self, pallets, limit_over):
        self.limit - len(pallets)
        if len(pallets) >= limit_over:
            self.pallets.extend(pallets[:limit_over])
            self.remaining_pallets = pallets[limit_over:]
            print(f"{len(self.pallets)} pallets loaded onto {self.name}")
            print(f"{len(self.remaining_pallets)} not loaded onto {self.name}")
        elif len(pallets) < limit_over:
            self.pallets.extend(pallets)
            print(f"{len(self.pallets)} pallets loaded onto {self.name}")

            print(f"Maximum capacity is {limit_over}")
        return self.remaining_pallets

    def relocate_pallet(self, next_location):

        next_location.load_pallet(pallets=self.pallets_to_relocate, limit_over=next_location.limit)
        print(f"{len(self.pallets_to_relocate)} pallets relocated from {self.name} to {next_location.name}")

    def get_limit(self):
        return self.limit

    def get_name(self):
        return self.name
