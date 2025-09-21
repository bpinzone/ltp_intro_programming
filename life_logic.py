def is_alive_next_gen(is_currently_alive, num_alive_neighbors):
    if is_currently_alive:
        if num_alive_neighbors < 2:
            return False
        if num_alive_neighbors > 3:
            return False
        return True
    else:
        return num_alive_neighbors == 3
