import pygame

def load_sprite(image_path):
    return pygame.image.load(image_path)

playerImg = load_sprite('player.png')
enemyImg = load_sprite('enemy.png')
bulletImg = load_sprite('bullet.png')

textImg = load_sprite('text.png')

sprite_loaded = True