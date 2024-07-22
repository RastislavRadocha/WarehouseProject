class Location:
    def __init__(self, name: str, limit: int, location: list = []) -> None:
        self.name = name
        self.limit = limit
        self.pallets = []
        self.remaining_pallets = []

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

    def offload_pallet(self, pallets, next_location):
        self.limit += len(pallets)

    def get_limit(self):
        return self.limit

    def get_name(self):
        return self.name
