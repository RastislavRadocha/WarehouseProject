location_1 = []
location_2 = []

numbers = list(range(1, 51))

num_of_pallets_to_move = 20

pallets_to_move = numbers[:num_of_pallets_to_move]
location_1.extend(pallets_to_move)
del numbers[:num_of_pallets_to_move]

pallets_to_relocate = location_1[:num_of_pallets_to_move]
location_2.extend(pallets_to_relocate)
del location_1[:num_of_pallets_to_move]

if __name__ == '__main__':
    print(location_1)
    print(location_2)
    print(numbers)
