class Location:
    def __init__(self, name: str, limit: int):
        self.name = name
        self.limit = limit
        self.pallets = []
        self.excess_pallets = [] # pallets exceeding the limit
        self.pallets_for_relocation = []

    def load_pallet(self, pallets:list , max_allowed: int) -> list:
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

        return unloaded_pallets

    def relocate_pallet(self, next_location):
        try:
            unloaded_pallets = next_location.load_pallet(self.pallets_for_relocation, next_location.limit)
            if unloaded_pallets:
                print(f"Warning: {len(unloaded_pallets)} pallets could not be relocated to {next_location.name}"
                      f" due to space limitations.")
            else:
                print(f"{len(self.pallets_for_relocation)} pallets relocated from {self.name} to {next_location.name}")
                self.pallets_for_relocation = []  # Clear the list after successful relocation

        except Exception as e:
            print(f"Error relocating pallets: {e}")



    def get_limit(self):
        return self.limit

    def get_name(self):
        return self.name
