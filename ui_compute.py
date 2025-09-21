from geometry import Rectangle

def get_subsection_for_child(parent_screen_section: Rectangle, child_intraParentPosition: Rectangle, parent_units_width: int, parent_units_height: int):
    """ The parent renders itself inside parent_screen_section.
    This function produces the subsection that the child should render itself in.
    child_intraParentPosition specifies the child's position and size in the parent's coordinate system.
    parent_units_width and parent_units_height specify how many units the parent is divided into. child_intraParentPosition should be specified in terms of these units."""

    pixels_per_parent_unit_width = parent_screen_section.width // parent_units_width
    pixels_per_parent_unit_height = parent_screen_section.height // parent_units_height

    child_screen_rect_left = parent_screen_section.left + child_intraParentPosition.left * pixels_per_parent_unit_width
    child_screen_rect_top = parent_screen_section.top + child_intraParentPosition.top * pixels_per_parent_unit_height
    child_screen_rect_width = child_intraParentPosition.width * pixels_per_parent_unit_width
    child_screen_rect_height = child_intraParentPosition.height * pixels_per_parent_unit_height
    return Rectangle(child_screen_rect_left, child_screen_rect_top, child_screen_rect_width, child_screen_rect_height)

