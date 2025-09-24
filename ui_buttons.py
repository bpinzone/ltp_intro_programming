from collections.abc import Callable

from geometry import Rectangle
from ui_render_primitives import draw_juicy_rectangle, draw_text, draw_rectangle
from ui_compute import get_subsection_for_child
import pygame
from colors import *
import time

class LabelledIntegerControl():
    def __init__(self, label, init_val, min, max):
        self.label = label
        self.int_control_buttons = IntegerControlButtons(init_val, min, max)
    
    def get_val(self):
        return self.int_control_buttons.val
    
    def draw(self, surface: pygame.Surface, screen_section: Rectangle):
        ui_units_width = 6
        ui_units_height = 1

        label_pos = Rectangle(0, 0, 3, 1)
        control_pos = Rectangle(3, 0, 3, 1)

        label_ss = get_subsection_for_child(screen_section, label_pos, ui_units_width, ui_units_height)
        control_ss = get_subsection_for_child(screen_section, control_pos, ui_units_width, ui_units_height)

        draw_text(surface, label_ss, self.label, WHITE)

        self.int_control_buttons.draw(surface, control_ss)



class IntegerControlButtons:
    def __init__(self, init_val: int, min: int, max: int):
        self.val = init_val
        self.min = min
        self.max = max

        self.plus_button = Button(text="+", text_color=WHITE, button_color=RED, on_click=self.increase_val)
        self.minus_button = Button(text="-", text_color=WHITE, button_color=BLUE, on_click=self.decrease_val)
    
    def increase_val(self):
        self.val += 1
        if self.val > self.max:
            self.val = self.max
    
    def decrease_val(self):
        self.val -= 1
        if self.val < self.min:
            self.val = self.min

    # You should send a screensection that is ratio width = 3, height = 1
    def draw(self, surface: pygame.Surface, screen_section: Rectangle):

        ui_units_width = 3
        ui_units_height = 1

        minus_subsection = get_subsection_for_child(screen_section, Rectangle(left=0, top=0, width=1, height=1), ui_units_width, ui_units_height)

        val_subsection = get_subsection_for_child(screen_section, Rectangle(left=1, top=0, width=1, height=1), ui_units_width, ui_units_height)

        plus_subsection = get_subsection_for_child(screen_section, Rectangle(left=2, top=0, width=1, height=1), ui_units_width, ui_units_height)

        self.minus_button.draw_andSaveScreenSection(surface, minus_subsection)
        self.plus_button.draw_andSaveScreenSection(surface, plus_subsection)
        draw_text(surface, val_subsection, str(self.val), WHITE)

class BoolButton:
    def __init__(self, init_val: bool, true_str, false_str):
        self.val = init_val
        self.true_str = true_str
        self.false_str = false_str
        if self.val:
            text = self.false_str
        else:
            text = self.true_str
        self.button = Button(text=text, text_color=WHITE, button_color=GREEN, on_click=self.toggle)
    
    def toggle(self):
        if self.val:
            self.val = False
            self.button.text = self.true_str
        else:
            self.val = True
            self.button.text = self.false_str

    # You should send a screensection that is ratio width = 3, height = 1
    def draw(self, surface: pygame.Surface, screen_section: Rectangle):
        self.button.draw_andSaveScreenSection(surface, screen_section)



class Button:
    all_buttons = []
    def __init__(self,
        text: [None, str],
        text_color,
        button_color, on_click: Callable[[], None],
        single_click_only = True):

        self.screen_section = None

        self.text = text
        self.text_color = text_color

        self.button_color = button_color

        self.on_click : Callable[[], None] = on_click

        self.single_click_only = single_click_only

        self.last_on_click_instant = None

        Button.all_buttons.append(self)
    
    # single click only.
    @classmethod
    def fwd_event_to_buttons(cls, event):
        for button in cls.all_buttons:
            if button.single_click_only:
                button.possibly_handle_event(event)

    # hover buttons only
    @classmethod
    def fwd_hover_to_buttons(cls, last_mouse_event_instant):
        mouse_pos = pygame.mouse.get_pos()
        for button in cls.all_buttons:
            if not button.single_click_only:
                button.handle_hover(mouse_pos, last_mouse_event_instant)
    

    def draw_andSaveScreenSection(self, surface: pygame.Surface, screen_section : Rectangle):

        self.screen_section = screen_section
        self.py_rect = self.screen_section.as_pygame_rect()

        # background
        draw_juicy_rectangle(surface, self.screen_section, self.button_color)

        # text
        if self.text is not None:
            draw_text(surface, self.screen_section, self.text, self.text_color)
    
    # only call for Single Click buttons.
    def possibly_handle_event(self, event: pygame.event.Event):
        if self.screen_section is None:
            raise Exception("LOGIC ERROR: Buton is possibly handling event but has no screen section!")
        if not self.single_click_only:
            raise Exception("Logic error. Don't call this function for single click buttons.")

        assert event.type == pygame.MOUSEBUTTONDOWN

        if event.button == 1:  # Left click

            mouse_pos = pygame.mouse.get_pos()

            py_rect = self.screen_section.as_pygame_rect()
            if py_rect.collidepoint(mouse_pos):
                self.on_click()
                self.last_on_click_instant = time.time()
    
    def handle_hover(self, mouse_pos, last_mouse_event_instant):
        if self.py_rect.collidepoint(mouse_pos):
            if (self.last_on_click_instant is None) or last_mouse_event_instant > self.last_on_click_instant:
                self.on_click()
                self.last_on_click_instant = time.time()
