import sys

from pallet import Pallet
import datetime
from locations import Location
from pallet import Pallet


def create_location_dictionary(locations_data):
    location_dict = {}
    for location_data in locations_data:
        location = Location(location_data['name'], location_data['capacity'])
        location_dict[location.name] = location
    return location_dict


location_data = [
    {'name': 'Overflow1', 'capacity': 50},
    {'name': 'Overflow2', 'capacity': 50},
    {'name': 'Temporary Location 1', 'capacity': 250},
    {'name': 'Temporary Location 2', 'capacity': 250},
]

locations_data = create_location_dictionary(location_data)


class SystemMenu(Pallet):
    def __init__(self, user: str, pallet_id):
        super().__init__(pallet_id)
        self.user = user

    def _show_instructions(self):
        print(f'Welcome to Warehouse management system {self.user}!')
        print('Commands: ')
        print('1 - Generate pallets')
        print('2 - Load pallets')  # load them to specific locations
        print('3 - Relocate pallets')
        print('4 - Display excess pallets')
        print('5 - Show locations')
        print('6 - Show location status')  # How many pallets we have and where they are, ask which location
        print('7 - Exit')

    def _exit_system(self):
        print(f'See you next time {self.user}')
        sys.exit()

    def run(self) -> None:
        self._show_instructions()
        while True:
            user_input: str = input('Please choose an option: ')

            if user_input not in ('1', '2', '3', '4', '5', '6'):
                print('Invalid input. Enter a valid choice')
                continue

            if user_input == '1':
                num_pallets_to_generate = int(input('How many pallets would you like to generate?: '))
                print(f'Generating {num_pallets_to_generate} pallets')
                gen_pallet = Pallet.generating_pallets(self, num_pallets_to_generate)
                print(f'{[p for p in gen_pallet]}')

            if user_input == '2':
                print('Available locations:')
                for location_name, location in locations_data.items():
                    print(f'- {location_name}')

                num_pallets_to_load = int(input('How many pallets to load?: '))
                if num_pallets_to_load > len(gen_pallet):
                    print('Not enough pallets to load')
                    continue
                load_pallets = gen_pallet[:num_pallets_to_load]
                excess_pallets = gen_pallet[num_pallets_to_load:]

                choose_location = input('Where to load?: ')
                if choose_location in locations_data:
                    location = locations_data[choose_location]
                    loaded_count, remaining_pallets = location.load_pallet(load_pallets, location.limit)
                    excess_pallets.extend(remaining_pallets)

                    print(f"Loading {loaded_count} pallets to {choose_location}")
                    print(f"{len(remaining_pallets)} pallets could not be loaded")
                    print(f'{[p for p in load_pallets[:loaded_count]]}')
                else:
                    print(f"Location '{choose_location}' not found.")

            if user_input == '3':
                source_relocation_name = input('From which location you want to relocate pallets?: ')
                target_relocation_name = input('Where you want to relocate pallets?: ')
                if source_relocation_name not in locations_data or target_relocation_name not in locations_data:
                    print('Invalid location')
                    return

                source_location = locations_data[source_relocation_name]
                target_location = locations_data[target_relocation_name]

                print(f'Relocating pallets from {source_relocation_name} to {target_relocation_name}')
                source_location.relocate_pallet(target_location)




            if user_input == '4':
                print(f'Excess pallets: {[p for p in excess_pallets]}')

            if user_input == '6':
                self._exit_system()


def main():
    user = input('Enter your name: ')
    system = SystemMenu(user, pallet_id=1)
    system.run()


if __name__ == '__main__':
    main()
