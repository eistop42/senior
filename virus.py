import pygame
from tkinter import *
from tkinter import messagebox
import time


pygame.init()
screen = pygame.display.set_mode((100, 850))

screen.fill('yellow')
icon = pygame.image.load('C:\\Users\\alex\\Downloads\\images (3).jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption("WARNING!")

font = pygame.font.SysFont("Lucida Console", 20)

label = font.render("YOU DOWNLOADED VIRUS", 1, (12, 140, 0, 1))
screen.blit(label, (50, 50))
screen.blit(label, (50, 100))
screen.blit(label, (250, 100))
pygame.display.update()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(1)
            pygame.quit()

            # screen = pygame.display.set_mode((850, 150))
            # screen.fill((0, 0, 0))
            
            # pygame.init()
            # font = pygame.font.SysFont("Lucida Console", 20)
            # label = font.render("asdfasfsadf", 1, (12, 140, 0, 1))
            # screen.blit(label, (50, 50))
            # pygame.display.update()
            # messagebox.showerror("LOL", "WE ARE ENCRYPTING OUR FILES")

