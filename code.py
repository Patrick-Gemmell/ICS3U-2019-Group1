#!/usr/bin/env python3

# Created by: Patrick
# Created on: January 2019
# Makes a game on circuit python

import ugame
import stage
import time
import random
import neopixel
import board

import constants


def splash_scene():
    # this function is the splash scene game loop

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

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
    # this function is a scene

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

    # a list of sprites
    sprites = []

    # add text objects
    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("BALL BREAKER!")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + sprites + [background]
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

def game_scene():

    image_bank_1 = stage.Bank.from_bmp16("ball.bmp")
    sprites = []
    image_bank_2 = stage.Bank.from_bmp16("space_aliens.bmp")
    sprites = []

    attack = []
    for attack_number in range(constants.TOTAL_ATTACKS):
        a_single_attack = stage.Sprite(image_bank_1, 2, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        attack.append(a_single_attack)

    enemy = []
    for enemy_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_enemy = stage.Sprite(image_bank_2, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        enemy.append(a_single_enemy)

    def show_enemy():
        for enemy_number in range(len(enemy)):
            if enemy[enemy_number].x < 20:
                enemy[enemy_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    enemy_count = 10
    show_enemy()

    score = 0
    text = []
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))
    text.append(score_text)
    
    # this sets the background
    a_button = constants.button_state["button_up"]

    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    boom_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    for pixel_number in range(0, 5):
        pixels[pixel_number] = (0, 10, 0)
    pixels.show()

    # this is the background
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1,3)
            background.tile(x_location, y_location, tile_picked)

    # create a sprite
    # parameters (image_bank_1, image # in bank, x, y)
    ball_one = stage.Sprite(image_bank_1, 3, 64, 56)
    sprites.append(ball_one)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = sprites + attack + enemy + text + [background]

    game.render_block()

    while True:
        # get user inputs
        keys = ugame.buttons.get_pressed()
        # print(keys)
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_UP != 0:
            if ball_one.y < 0:
                ball_one.move(ball_one.x, 0)
            else:
                ball_one.move(ball_one.x, ball_one.y -
                              constants.SPRITE_MOVEMENT_SPEED)
            pass
        if keys & ugame.K_DOWN != 0:
            if ball_one.y > constants.SCREEN_Y - constants.SCREEN_GRID_Y:
                ball_one.move(ball_one.x, constants.SCREEN_Y -
                              constants.SPRITE_SIZE)
            else:
                ball_one.move(ball_one.x, ball_one.y +
                              constants.SPRITE_MOVEMENT_SPEED)
            pass
        if keys & ugame.K_LEFT != 0:
            if ball_one.x < 0:
                ball_one.move(0, ball_one.y)
            else:
                ball_one.move(ball_one.x - constants.SPRITE_MOVEMENT_SPEED,
                              ball_one.y)
            pass
        if keys & ugame.K_RIGHT != 0:
            if ball_one.x > constants.SCREEN_X - constants.SCREEN_GRID_X:
                ball_one.move(constants.SCREEN_X - constants.SPRITE_SIZE,
                              ball_one.y)
            else:
                ball_one.move(ball_one.x + constants.SPRITE_MOVEMENT_SPEED,
                              ball_one.y)
            pass
        # update game logic
        if a_button == constants.button_state["button_just_pressed"]:
            for attack_number in range(len(attack)):
                if attack[attack_number].x < 0:
                    attack[attack_number].move(ball_one.x, ball_one.y)
                    sound.play(pew_sound)
                    break
        for attack_number in range(len(attack)):
            if attack[attack_number].x > 0:
                attack[attack_number].move(attack[attack_number].x,
                                           attack[attack_number].y -
                                           constants.ATTACK_SPEED)
                if attack[attack_number].y < constants.OFF_TOP_SCREEN:
                   attack[attack_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
        for enemy_number in range (len(enemy)):
            if enemy[enemy_number].x > 0:
                enemy[enemy_number].move(enemy[enemy_number].x,
                                           enemy[enemy_number].y +
                                           constants.ALIEN_SPEED)
                if enemy[enemy_number].y > constants.SCREEN_Y:
                    enemy[enemy_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_enemy()

        for attack_number in range(len(attack)):
            if attack[attack_number].x > 0 :
                for enemy_number in range(len(enemy)):
                    if enemy[enemy_number].x > 0:
                        if stage.collide(enemy[enemy_number].x + 1,
                                         enemy[enemy_number].y,
                                         enemy[enemy_number].x + 15,
                                         enemy[enemy_number].y + 15,
                                         attack[attack_number].x + 6,
                                         attack[attack_number].y + 2,
                                         attack[attack_number].x + 11,
                                         attack[attack_number].y + 12):
                            # when you hit an alien
                            enemy[enemy_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            attack[attack_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            game.render_block()
                            
                            sound.stop()
                            sound.play(boom_sound)
                            show_enemy()
                            show_enemy()
                            enemy_count = enemy_count + 1

        for enemy_number in range(len(enemy)):
            if enemy[enemy_number].x > 0:
                # https://circuitpython-stage.readthedocs.io/en/latest/#stage.collide
                # and https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
                if stage.collide(enemy[enemy_number].x + 1, enemy[enemy_number].y,
                                 enemy[enemy_number].x + 15, enemy[enemy_number].y + 15,
                                 ball_one.x, ball_one.y,
                                 ball_one.x + 15, ball_one.y + 15):
                    # alien hit the ship
                    sound.stop()
                    sound.play(coin_sound)
                    for pixel_number in range(0, 5):
                        pixels[pixel_number] = (25, 0, 25)
                    pixels.show()
                    # Wait for 1 seconds
                    time.sleep(1.0)
                    # need to release the NeoPixels
                    pixels.deinit()
                    sound.stop()
                    game_over_scene(score)

        # redraw sprite list
        game.render_sprites(sprites + attack + enemy)
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


if __name__ == "__main__":
    splash_scene()