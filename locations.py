class Location:
    def __init__(self, name: str, limit: int):
        self.name = name
        self.limit = limit
        self.pallets = []
        self.excess_pallets = []  # pallets exceeding the limit
        self.pallets_for_relocation = []

    def load_pallet(self, pallets: list, max_allowed: int) -> list:
        """Loads pallets into the location, respecting the limit and returning unloaded pallets.

            Args:
                pallets: A list of pallet objects to be loaded.
                max_allowed: The maximum number of pallets allowed in the location (including any already loaded).

            Returns:
                A list of pallets that could not be loaded due to exceeding the limit.
            """
        available_space = max_allowed - len(self.pallets)
        pallets_to_load = min(available_space, len(pallets))

        self.pallets.extend(pallets[:pallets_to_load])
        unloaded_pallets = pallets[pallets_to_load:]

        print(f"{str(pallets_to_load)} pallets loaded onto {self.name}")
        if unloaded_pallets:
            print(f"{len(unloaded_pallets)} pallets not loaded due to space limitations.")

        return pallets_to_load, unloaded_pallets

    def relocate_pallet(self, target_location):
        print(f"Source location: {self.name}, Capacity: {self.limit}, Pallets: {len(self.pallets)}")
        print(f"Target location: {target_location.name}, Capacity: {target_location.limit},"
              f" Pallets: {len(target_location.pallets)}")
        unloaded_pallets = []
        available_space = target_location.limit - len(target_location.pallets)
        pallets_to_move = self.pallets[:available_space]

        target_location.pallets.extend(pallets_to_move)
        self.pallets = self.pallets[available_space:]

        print(f"Source location after relocation: {self.name}, Capacity: {self.limit}, Pallets: {len(self.pallets)}")
        print(f"Target location after relocation: {target_location.name}, Capacity: {target_location.limit},"
              f" Pallets: {len(target_location.pallets)}")
        return unloaded_pallets

    def get_limit(self):
        return self.limit

    def get_name(self):
        return self.name
