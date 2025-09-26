import math

def do_circles_intersect(c1_position_x, c1_position_y, c1_diameter,
                         c2_position_x, c2_position_y, c2_diameter):
    """
    Check if two circles intersect.

    Two circles intersect if the distance between their centers is less than or equal to the sum of their radii.

    Args:
        c1_position_x: A number. The x-coordinate of the center of the first circle.
        c1_position_y: A number. The y-coordinate of the center of the first circle.
        c1_diameter: A number. The diameter of the first circle.

        c2_position_x: A number. The x-coordinate of the center of the second circle.
        c2_position_y: A number. The y-coordinate of the center of the second circle.
        c2_diameter: A number. The diameter of the second circle.

    Returns:
        True if the circles intersect, False otherwise.
    """

    # use distance formula:
    # https://en.wikipedia.org/wiki/Distance
    dx = c1_position_x - c2_position_x
    dy = c1_position_y - c2_position_y
    distance_between_circle_centers = math.sqrt(dx * dx + dy * dy)

    sum_of_radius = (c1_diameter / 2) + (c2_diameter / 2)

    if distance_between_circle_centers <= sum_of_radius:
        return True
    else:
        return False
