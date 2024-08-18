def build_specific_tower(n_floors, block_size):
    tower = []
    for i in range(n_floors):
        if i % block_size[1] == 0:
            stars = '*' * block_size[0]
            tower.append(' ' * ((n_floors - i - 1) * block_size[0]) + stars + ' ' * ((n_floors - i - 1) * block_size[0]))
        else:
            tower.append(' ' * ((n_floors - i - 1) * block_size[0]))

    return tower


if __name__ == '__main__':
    print(build_specific_tower(3, (4,2)))
