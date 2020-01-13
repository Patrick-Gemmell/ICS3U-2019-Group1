#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: January 2019
# This file is the "Space Aliens" game
#   for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random

import constants

def blank_white_reset_scene():
    # this function is the splash scene game loop
    # do house keeping to ensure everythng is setup
    # set up the NeoPixels
    # pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    # pixels.deinit() # and turn them all off
    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # Wait for 1/2 seconds
        time.sleep(0.5)
        splash_scene()
        # redraw sprite list

def splash_scene():
    # this function is the MT splash scene
    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white
    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white
    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white
    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # Wait for 1/2 seconds
        time.sleep(1.0)
        menu_scene()
        # redraw sprite list

def menu_scene():
    # this function is the splash scene game loop

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.0)
        menu_scene()

        # redraw sprite list

def menu_scene():
    # this function is the menu scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("menu.bmp")
    image_bank_3 = stage.Bank.from_bmp16("Menu2.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 4, 13)  # blank white
    background.tile(1, 2, 0)
    background.tile(0, 3, 0)
    background.tile(1, 3, 0)
    background.tile(0, 4, 0)
    background.tile(1, 4, 0)  # blank white
    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 0)
    background.tile(3, 5, 0)
    background.tile(3, 6, 0)
    background.tile(2, 6, 0)
    background.tile(2, 7, 0)  # blank white
    background.tile(1, 7, 0)  # blank white
    background.tile(0, 8, 0)
    background.tile(1, 8, 0)
    background.tile(5, 4, 0)
    background.tile(6, 4, 0)
    background.tile(7, 4, 0)  # blank white
    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 0)
    background.tile(5, 5, 0)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    sprite = []

    sprite_one = stage.Sprite(image_bank_2, 1, 144, 32)
    sprite.append(sprite_one)
    sprite_two = stage.Sprite(image_bank_2, 2, 128, 32)
    sprite.append(sprite_two)
    sprite_three = stage.Sprite(image_bank_2, 3, 112, 32)
    sprite.append(sprite_three)
    sprite_four = stage.Sprite(image_bank_2, 5, 96, 32)
    sprite.append(sprite_four)
    sprite_five = stage.Sprite(image_bank_2, 7, 80, 32)
    sprite.append(sprite_five)
    sprite_six = stage.Sprite(image_bank_2, 9, 64, 32)
    sprite.append(sprite_six)
    sprite_seven = stage.Sprite(image_bank_2, 4, 112, 48)
    sprite.append(sprite_seven)
    sprite_eight = stage.Sprite(image_bank_2, 6, 96, 48)
    sprite.append(sprite_eight)
    sprite_nine = stage.Sprite(image_bank_2, 8, 80, 48)
    sprite.append(sprite_nine)
    sprite_ten = stage.Sprite(image_bank_2, 10, 64, 48)
    sprite.append(sprite_ten)
    sprite_eleven = stage.Sprite(image_bank_2, 11, 48, 32)
    sprite.append(sprite_eleven)
    sprite_twelve = stage.Sprite(image_bank_2, 12, 48, 48)
    sprite.append(sprite_twelve)
    sprite_thirteen = stage.Sprite(image_bank_2, 13, 32, 48)
    sprite.append(sprite_thirteen)
    sprite_fourteen = stage.Sprite(image_bank_2, 14, 16, 48)
    sprite.append(sprite_fourteen)

    sprite_one = stage.Sprite(image_bank_3, 1, 144, 80)
    sprite.append(sprite_one)
    sprite_two = stage.Sprite(image_bank_3, 2, 128, 80)
    sprite.append(sprite_two)
    sprite_three = stage.Sprite(image_bank_3, 3, 112, 80)
    sprite.append(sprite_three)
    sprite_four = stage.Sprite(image_bank_3, 4, 96, 80)
    sprite.append(sprite_four)
    sprite_five = stage.Sprite(image_bank_3, 5, 80, 80)
    sprite.append(sprite_five)
    sprite_six = stage.Sprite(image_bank_3, 6, 64, 80)
    sprite.append(sprite_six)
    sprite_seven = stage.Sprite(image_bank_3, 7, 48, 80)
    sprite.append(sprite_seven)
    sprite_eight = stage.Sprite(image_bank_3, 8, 112, 64)
    sprite.append(sprite_eight)
    sprite_nine = stage.Sprite(image_bank_3, 9, 96, 64)
    sprite.append(sprite_nine)
    sprite_ten = stage.Sprite(image_bank_3, 10, 80, 64)
    sprite.append(sprite_ten)
    sprite_eleven = stage.Sprite(image_bank_3, 11, 64, 64)
    sprite.append(sprite_eleven)
    sprite_twelve = stage.Sprite(image_bank_3, 12, 48, 64)
    sprite.append(sprite_twelve)
    sprite_thirteen = stage.Sprite(image_bank_3, 13, 32, 64)
    sprite.append(sprite_thirteen)
    sprite_fourteen = stage.Sprite(image_bank_3, 14, 16, 64)
    sprite.append(sprite_fourteen)


    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Shooter Shootout")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("PRESS START")
    text.append(text2)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text+ sprite + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_START != 0:  # Start button
            game_scene()
            #break

        # redraw sprite list

def game_scene():
    # this function is the game scene

    # game score
    score = 0

    # tank direction
    tank_direction = None

    def show_alien():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an alien show up on screen in the x-axis
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0: # meaning it is off the screen, so available to move on the screen
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew2.wav", 'rb')  # to change the wav volume: https://audioalter.com/volume/
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    image_bank_2 = stage.Bank.from_bmp16("sprites.bmp")
    # a list of sprites that will be updated every frame
    sprites = []

    # create lasers for when we shoot
    lasers = []
    lasers_direction = []
    for laser_number in range(constants.TOTAL_ATTACKS):
        a_single_laser = stage.Sprite(image_bank_2, 2, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        lasers_direction.append("None")
        lasers.append(a_single_laser)

    # set up the NeoPixels to match the # of lasers fired
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    for pixel_number in range(0, 5):
        pixels[pixel_number] = (0, 10, 0)
    pixels.show()

    # create aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_2, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        aliens.append(a_single_alien)

    # current number of aliens that should be moving down screen, start with just 1
    alien_count = 1
    show_alien()

    # add text at top of screen for score
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    tank = stage.Sprite(image_bank_2, 4, int(constants.SCREEN_X / 2), constants.SCREEN_Y - constants.SPRITE_SIZE)
    sprites.append(tank) # insert at the top of sprite list

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 0)
            background.tile(x_location, y_location, tile_picked)


    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + lasers + aliens + [score_text] + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_X != 0:  # A button
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # update game logic

        # if right D-Pad is pressed

        if keys & ugame.K_RIGHT != 0:
            # if tank moves off right screen, move it back
            if tank.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                tank.x = constants.SCREEN_X - constants.SPRITE_SIZE
            # else move tank right
            else:
                tank.move(tank.x + constants.BALL_SPEED, tank.y)
                tank.set_frame(frame=None,rotation=1)
                tank_direction = "right"

        # if left D-Pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if tank moves off left screen, move it back
            if tank.x < 0:
                tank.x = 0
            # else move tank left
            else:
                tank.move(tank.x - constants.BALL_SPEED, tank.y)
                tank.set_frame(frame=None,rotation=3)
                tank_direction = "left"

        if keys & ugame.K_UP != 0:
            # if tank moves off up screen, move it back
            if tank.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
                tank.y = constants.SCREEN_Y - constants.SPRITE_SIZE
            # else move tank up
            else:
                tank.move(tank.x, tank.y - 1)
                tank.set_frame(frame=None,rotation=0)
                tank_direction = "up"

        # if left D-Pad is pressed
        if keys & ugame.K_DOWN != 0:
            # if tank moves off down screen, move it back
            if tank.y < 0:
                tank.y = 0
            # else move tank down
            else:
                tank.move(tank.x, tank.y + 1)
                tank.set_frame(frame=None,rotation=2)
                tank_direction = "down"


        # if A Button (fire) is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser, if we have enough power (meaning we have not used up all the lasers)
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(tank.x, tank.y)
                    lasers_direction[laser_number] = tank_direction
                    sound.stop()
                    sound.play(pew_sound)
                    break

        # each frame move the lasers, that have been fired, up

        # first make all the neopixels yellow, then make them green if it is moving up
        lasers_moving_counter = -1
        for pixel_number in range(0, 5):
            pixels[pixel_number] = (0, 10, 0)

        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0 :
                laser_move_direction = None
                if lasers_direction[laser_number] == "down":
                    lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y + constants.ATTACK_SPEED)
                elif lasers_direction[laser_number] == "up":
                    lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.ATTACK_SPEED)
                elif lasers_direction[laser_number] == "left":
                    lasers[laser_number].move(lasers[laser_number].x - constants.ATTACK_SPEED, lasers[laser_number].y)
                elif lasers_direction[laser_number] == "right":
                    lasers[laser_number].move(lasers[laser_number].x + constants.ATTACK_SPEED, lasers[laser_number].y)


                lasers_moving_counter = lasers_moving_counter + 1
                pixels[lasers_moving_counter] = (10, 10 - (2 * lasers_moving_counter + 2), 0)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if lasers[laser_number].y > 128:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if lasers[laser_number].x > 160:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if lasers[laser_number].y < 1:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        if lasers_moving_counter == 4:
            for pixel_number in range(0, 5):
                pixels[pixel_number] = (10, 0, 0)
        pixels.show()


        # each frame move the aliens down the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0: # meaning it is on the screen
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien() # make it randomly show up at top again

        # each frame check if any of the lasers are touching any of the aliens
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0 :
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        # https://circuitpython-stage.readthedocs.io/en/latest/#stage.collide
                        # and https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other

                        # the first 4 numbers are the coordinates of A box
                        # since the laser is thin, it made it thinner and slightly smaller
                        #
                        # the second 4 numbers are the alien, it is more of a box so I just made it slightly smaller
                        #
                        # if you slow down the FPS, then you can see the interaction more easily to alter these numbers
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         aliens[alien_number].x + 1, aliens[alien_number].y,
                                         aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            # add 1 to the score
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            # this will freeze the screen for a split second, but we have no option
                            game.render_block()
                            # play sound effect
                            sound.stop()
                            # sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            alien_count = alien_count + 1

        # each frame check if any of the aliens are touching the tank
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                # https://circuitpython-stage.readthedocs.io/en/latest/#stage.collide
                # and https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                 tank.x, tank.y,
                                 tank.x + 15, tank.y + 15):
                    # alien hit the tank
                    sound.stop()
                    # sound.play(crash_sound)
                    for pixel_number in range(0, 5):
                        pixels[pixel_number] = (25, 0, 25)
                    pixels.show()
                    # Wait for 1 seconds
                    time.sleep(4.0)
                    # need to release the NeoPixels
                    pixels.deinit()
                    sound.stop()
                    game_over_scene(score)

        # redraw sprite list
        game.render_sprites(sprites + lasers + aliens)
        game.tick() # wait until refresh rate finishes

def game_over_scene(final_score):
    # this function is the game over scene
    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text0 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text0.move(22, 20)
    text0.text("Final Score: {:0>2d}".format(final_score))
    text.append(text0)

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(43, 60)
    text1.text("GAME OVER")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(32, 110)
    text2.text("PRESS SELECT")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_SELECT != 0:  # Start button
            keys = 0
            menu_scene()
            #break

        # redraw sprite list

if __name__ == "__main__":
    blank_white_reset_scene()