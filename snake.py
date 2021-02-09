import pygame
import sys
import random
pygame.init()
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
window_width = 600
window_height = 600
velocity = 10
snake_width = 15
snake_height = 5
apple_size = 20
small_font = pygame.font.sysFont('forte,25')
large_font = pygame.font.sysFont('showcardgothic', 30, True) 
medium_font = pygame.font.sysFont('chiller', 60, True, True)
canvas = pygame.display.set_mode(
    window_width,
    window_height
)
pygame.display.set_caption(
    'snake game'
)
apple_image = pygame.image.load('apple 1.png')
snake_image = pygame.image.load('snake 21.png')
def start_game(){
    canvas.fill(black)
    start_font(large_font.render)
    start_font1 = large_font.render("Welcome to snake game", True, GREEN)
    start_font2 = medium_font.render("Play Game", True, RED, YELLOW)
    start_font3 = medium_font.render("Instructions", True, RED, YELLOW)
    start_font4 = medium_font.render("Quit", True, RED, YELLOW)
    start_font5 = medium_font.render("Creator", True, RED, YELLOW)
}
    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()
    start_font5_rect = start_font5.get_rect()

    star_font1_rect.center = (the_window/2,window_height/2-2)
    star_font2_rect.center = (the_window/2+100,window_height/2+50)
    star_font3_rect.center = (the_window/2+100,window_height/2+100)
    star_font4_rect.center = (the_window/2+100,window_height/2+50)
    star_font5_rect.center = (the_window/2+100,window_height/2+200)

    canvas.bilt(star_font1,start_font1_rect)
    canvas.bilt(star_font2,start_font2_rect)
    canvas.bilt(star_font3,start_font3_rect)
    canvas.bilt(star_font4,start_font4_rect)
    canvas.bilt(star_font5,start_font5_rect)

    pygame.display.update()

def game_over(){
    font_game_over1 = large_font.render('game over', True, RED)
    font_game_over2 = large_font.render('play again', True, GREEN)
    font_game_over3 = large_font.render('quit', True, BLUE) 
    Font_game_over_rect1
    Font_game_over_rect2
    Font_game_over_rect3
    
}    