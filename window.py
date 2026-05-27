import os
# Environment variables for rendering the screen 
os.environ["SDL_VIDEO_CENTERED"] = "1"

import pygame
import random 
from generate import generate_valid_sudoku

FPS = 60
WIDTH = 1280
HEIGHT = 720
CENTER = (WIDTH / 2, HEIGHT / 2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 48)

running = True


grid = generate_valid_sudoku()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.display.set_caption("Sudoku Solver")

    # LOGIC HERE 

    


    # First edge 
    line_start = (CENTER[0] - 300, CENTER[1] - 300)
    
    # Lines for the sudoku 
    thick_line_offset = 200
    thin_line_offset = thick_line_offset / 3
    x,y = line_start    
    
    for i in range(4): 
        # Thick vertical lines 
        pygame.draw.line(screen, "black", (x + i * thick_line_offset, y), (x + i * thick_line_offset, y + 600), 5)
        
        # Thick horizontal lines 
        pygame.draw.line(screen, "black", (x, y + i * thick_line_offset), (x + 600, y + i * thick_line_offset), 5)
        
    for i in range(9): 
        # Thin vertical lines 
        pygame.draw.line(screen, "black", (x + i * thin_line_offset, y), (x + i * thin_line_offset, y + 600), 1)
        
        # Thin horizontal lines 
        pygame.draw.line(screen, "black", (x, y + i * thin_line_offset), (x + 600, y + i * thin_line_offset), 1)
    
    number_offset = thin_line_offset / 2
    
    # Adding numbers for testing 
    for row in range(9):
        for col in range(9):
            number = grid[row][col]
            number_center = (
                x + col * thin_line_offset + number_offset,
                y + row * thin_line_offset + number_offset
            )
            text_surface = font.render(str(number), True, "black")
            text_rect = text_surface.get_rect(center=number_center)
            screen.blit(text_surface, text_rect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # set FPS 
    clock.tick(FPS)

pygame.quit()