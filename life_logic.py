import game_of_life

def is_cell_alive_next_gen(is_currently_alive, num_alive_neighbors):
    """
    For a single cell, determine if it will be alive in the next generation.

    Args:
        is_currently_alive: A boolean. Whether the cell is currently alive in this generation.
        num_alive_neighbors: A number. Indicates how many alive neighbors the cell has this generation.

    Returns:
        True if the cell will be alive in the next generation, False otherwise.

    Old Rules: (What the code currently does)
        Any live cell stays alive.
        Any dead cell becomes alive if any of its neighbors are alive.

    New Rules: (What you should make the code do)
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
        return True
    else:
        if num_alive_neighbors > 0:
            return True
        else:
            return False

if __name__ == '__main__':
    game_of_life.main()
