#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2019
# This file is the "Space Aliens" game
#   for CircuitPython

import ugame
import stage


def game_scene():
    # this function is the game scene

    # create a list fo rall the sprites to be held in
    sprites = []

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("./space_aliens.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # the ship sprite(the 5th image, starting to count at 0) 
    #   will show up at location (72,56), which places it in middle of screen
    ship = stage.Sprite(image_bank_1, 5, 72, 56)
    # add the ship sprite to the sprite list
    sprites.append(ship)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order, sprites and background behind
    game.layers = sprites + [background]
    # render the background and inital location of sprites list
    # most likely you will only render background once per scene
    # it is slow to draw
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprites list
        game.render_sprites(sprites)
        game.tick() # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()
