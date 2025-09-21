#! /usr/bin/python3
# EVERYTHING is Top Left = 0, 0

# dream and nightmare board display is pretty much done. A bit buggy, sometimes blocks are one cell too high.

import os
from time import sleep
import time

from life_logic import is_cell_alive_next_gen
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
import sys
from enum import Enum, auto
from dataclasses import dataclass
from geometry import Rectangle
from color_grid import ColorGrid 
from collections.abc import Callable
from colors import *

from ui_buttons import BoolButton, Button, LabelledIntegerControl
from ui_render_primitives import draw_rectangle_outline, draw_rectangle, draw_juicy_rectangle, draw_text
from ui_compute import get_subsection_for_child

# Initialize Pygame
pygame.init()

# Get the screen info
screen_info = pygame.display.Info()
WINDOW_WIDTH = screen_info.current_w / 2
WINDOW_HEIGHT = screen_info.current_h / 2

# Set up the display with resizable flag
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game of Life")

class GridCell:
    def __init__(self):

        # todo these should be static
        # todo: why can't it find these properly via import?
        GREEN = (0, 255, 0)
        WHITE = (255, 255, 255)
        self.alive_color = GREEN
        self.dead_color = WHITE


        self.__is_alive = False
        self.button = Button(None, None, self.dead_color, self.toggle_alive, False)
    
    def get_alive(self):
        return self.__is_alive

    def set_alive(self, is_alive):
        if is_alive:
            self.__is_alive = True
            self.button.button_color = self.alive_color
        else:
            self.__is_alive = False
            self.button.button_color = self.dead_color
    
    def toggle_alive(self):
        self.set_alive(not self.__is_alive)


# [row][col]. (0, 0) is top left.
class Grid:

    def __init__(self, width, height):
        self.cells = [ [GridCell() for _ in range(0, width)] for _ in range(0, height)]
        self.width = width
        self.height = height
    
    def tick(self):

        # borders are always dead. Implemented by setting all to False here and not touching them.
        self.alive_next_gen = [ [False for _ in range(0, self.width)] for _ in range(0, self.height)]

        for row in range(1, self.height - 1):
            for col in range(1, self.width - 1):

                # count how many neighbors are alive.
                alive_neighbors = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if(self.cells[row + dy][col + dx].get_alive()):
                            alive_neighbors += 1

                # TODO: replace witih actual function
                # self.alive_next_gen[row][col] = self.cells[row][col - 1].get_alive()
                self.alive_next_gen[row][col] = is_cell_alive_next_gen(self.cells[row][col].get_alive(), alive_neighbors)

        for row in range(0, self.height):
            for col in range(0, self.width):
                self.cells[row][col].set_alive(self.alive_next_gen[row][col])
        
    def draw(self, surface: pygame.Surface, screen_section: Rectangle):

        for row in range(0, self.height):
            for col in range(0, self.width):
                cell_pos = Rectangle(col, row, 1, 1)
                cell_subsection = get_subsection_for_child(screen_section, cell_pos, self.width, self.height)

                self.cells[row][col].button.draw_andSaveScreenSection(surface, cell_subsection)


class State:
    def __init__(self, is_paused, speed, grid_units):

        # self
        self.is_paused = is_paused
        self.speed = speed
        self.grid_units = grid_units
        self.grid = Grid(self.grid_units, self.grid_units)

        # control
        self.size_control = LabelledIntegerControl("size", 20, 4, 1000)
        self.pause_control = BoolButton(True, "Pause", "Play")
        self.speed_control = LabelledIntegerControl("speed", 5, 1, 15)

        # about user hardware
        self.is_mouse_pressed = False
        self.last_mouse_event_instant = time.time()
    
    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.is_mouse_pressed = True
            self.last_mouse_event_instant = time.time()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_mouse_pressed = False
            self.last_mouse_event_instant = time.time()


    def fwd_control_to_self(self):
        
        if self.grid_units != self.size_control.get_val():
            self.grid_units = self.size_control.get_val()
            self.grid = Grid(self.grid_units, self.grid_units)
        
        if self.is_paused != self.pause_control.val:
            self.is_paused = self.pause_control.val
        
        if self.speed != self.speed_control.get_val():
            self.speed = self.speed_control.get_val()
    
    def get_sim_tick_period(self):
        sim_tick_period_step = 0.1
        return sim_tick_period_step * (self.speed_control.int_control_buttons.max - self.speed)

state = State(True, 1, 10)


def main():
    global screen
    current_w = WINDOW_WIDTH
    current_h = WINDOW_HEIGHT

    global state

    last_sim_tick_instant = time.time()
    
    while True:

        this_frame_instant = time.time()
        
        # simulate
        if not state.is_paused:
            time_since_last_sim_tick = this_frame_instant - last_sim_tick_instant
            if time_since_last_sim_tick >= state.get_sim_tick_period():
                # simulate
                state.grid.tick()
                last_sim_tick_instant = this_frame_instant

        # render
        draw_screen(screen, Rectangle(left=0, top=0, width=current_w, height=current_h))
        pygame.display.flip()

        # wait for events
        sleep(10 / 1000)

        # gather events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resize
                current_w, current_h = event.size
                screen = pygame.display.set_mode((current_w, current_h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Button.fwd_event_to_buttons(event)
                state.handle_mouse_event(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                state.handle_mouse_event(event)
        
        if state.is_mouse_pressed:
            Button.fwd_hover_to_buttons(state.last_mouse_event_instant)
        
        # forward any data changes from buttons to UI elements.
        state.fwd_control_to_self()



def draw_screen(surface: pygame.Surface, screen_section: Rectangle):
    surface.fill(BLACK)


    controls_width = screen_section.width * 0.2
    controls_height = screen_section.height

    remaining_width = screen_section.width - controls_width
    board_size = min(remaining_width, screen_section.height)


    board_pos = Rectangle(0, 0, board_size, board_size)
    controls_pos = Rectangle(board_pos.left + board_pos.width, 0, controls_width, controls_height)

    board_ss = get_subsection_for_child(screen_section, board_pos, screen_section.width, screen_section.height)
    draw_grid(surface, board_ss)

    controls_ss = get_subsection_for_child(screen_section, controls_pos, screen_section.width, screen_section.height)
    draw_controls(surface, controls_ss)



def draw_grid(surface: pygame.Surface, screen_section: Rectangle):
    global state
    state.grid.draw(surface, screen_section)

def draw_controls(surface: pygame.Surface, screen_section: Rectangle):
    ui_units_width = 1
    ui_units_height = 10

    global state

    pause_control_pos = Rectangle(0, 0, 1, 1)
    pause_control_ss = get_subsection_for_child(screen_section, pause_control_pos, ui_units_width, ui_units_height)
    state.pause_control.draw(surface, pause_control_ss)


    size_control_pos = Rectangle(0, 1, 1, 1)
    size_control_ss = get_subsection_for_child(screen_section, size_control_pos, ui_units_width, ui_units_height)
    state.size_control.draw(surface, size_control_ss)


    speed_control_pos = Rectangle(0, 2, 1, 1)
    speed_control_ss = get_subsection_for_child(screen_section, speed_control_pos, ui_units_width, ui_units_height)
    state.speed_control.draw(surface, speed_control_ss)


if __name__ == "__main__":
    main() 
