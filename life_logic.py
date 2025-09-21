def is_cell_alive_next_gen(is_currently_alive, num_alive_neighbors):
    """
    For a single cell, determine if it will be alive in the next generation.

    Args:
        is_currently_alive: Whether the cell is currently alive.
        num_alive_neighbors: The number of alive neighbors the cell has.

    Returns:
        True if the cell will be alive in the next generation, False otherwise.
    
    Rules:
        Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    assert num_alive_neighbors >= 0 and num_alive_neighbors <= 8

    # Exercise: Edit the code below:
    # Use comparison operators to make this code shorter.
    # See circle_intersection.py for an example of using comparison operators.
    if is_currently_alive:
        if num_alive_neighbors == 0:
            return False
        if num_alive_neighbors == 1:
            return False
        if num_alive_neighbors == 2:
            return True
        if num_alive_neighbors == 3:
            return True
        if num_alive_neighbors == 4:
            return False
        if num_alive_neighbors == 5:
            return False
        if num_alive_neighbors == 6:
            return False
        if num_alive_neighbors == 7:
            return False
        if num_alive_neighbors == 8:
            return False
    else:
        if num_alive_neighbors == 3:
            return True
        return False

