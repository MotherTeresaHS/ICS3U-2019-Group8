#!/usr/bin/env python3

# Created by: Mariam
# Created on: 2020
# This file is the "pong" game
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
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    pixels.deinit() # and turn them all off

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
        mt_splash_scene()

        # redraw sprite list

def mt_splash_scene():
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

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
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

        # Wait for 1 seconds
        time.sleep(1.0)
        game_splash_scene()

        # redraw sprite list

def game_splash_scene():
    # this function is the game scene

    # repeat forever, game loop
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(60, 10)
    text1.text("Pong")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("Mariam Hemdan")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.0)
        main_menu_scene()

        # redraw sprite list

    pass # just a placeholder until you write the code


def main_menu_scene():
    # this function is the game scene

    # repeat forever, game loop
    # repeat forever, game loop
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(60, 10)
    text1.text("Pong")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 110)
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
    while True:
        # get user input

        # update game logic
        keys = ugame.buttons.get_pressed()
        # Wait for 1 seconds
        if keys & ugame.K_SELECT!= 0:
            key = 0
            game_scene()


        # redraw sprite list

        pass # just a placeholder until you write the code


def game_scene():
    # this function is the game scene
    # repeat forever, game loop
    bank = stage.Bank.from_bmp16("ball.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(bank, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # sprites
    sprites = []
    computer_paddle = []
    user_paddle = []
    velocity = [1, 1]

    ball = stage.Sprite(bank, 1, 80, 64)
    sprites.append(ball)

    paddle = stage.Bank.from_bmp16("paddle.bmp")
    paddle_a = stage.Sprite(paddle, 10, 8, 60)
    computer_paddle.append(paddle_a)
    paddle_b = stage.Sprite(paddle, 10, 8, 70)
    computer_paddle.append(paddle_b)
    paddle_c = stage.Sprite(paddle, 10, 8, 80)
    computer_paddle.append(paddle_c)

    paddle_d = stage.Sprite(paddle, 144, 136, 60)
    user_paddle.append(paddle_d)
    paddle_e = stage.Sprite(paddle, 144, 136, 70)
    user_paddle.append(paddle_e)
    paddle_f = stage.Sprite(paddle, 144, 136, 80)
    user_paddle.append(paddle_f)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = computer_paddle + user_paddle + sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)
        if keys & ugame.K_UP:
            # move the user paddle up
            for a_single_paddle_piece in user_paddle:
                a_single_paddle_piece.move(a_single_paddle_piece.x, a_single_paddle_piece.y - 1)
            # check if top paddle peice off top of screen
            if user_paddle[0].y < 0:
                # move all the paddle peices back up
                for a_single_paddle_piece in user_paddle:
                    a_single_paddle_piece.move(a_single_paddle_piece.x, a_single_paddle_piece.y + 1)
        if keys & ugame.K_DOWN:
            # move the user paddle up
            for a_single_paddle_piece in user_paddle:
                a_single_paddle_piece.move(a_single_paddle_piece.x, a_single_paddle_piece.y + 1)
            # check if bottom paddle peice off bottom of screen
            if user_paddle[2].y > 112 :
                # move all the paddle peices back up
                for a_single_paddle_piece in user_paddle:
                    a_single_paddle_piece.move(a_single_paddle_piece.x, a_single_paddle_piece.y - 1)

        # move the ball
        ball.move(ball.x + velocity[0], ball.y + velocity[1])
        # see the ball bounce
        if not 0 < ball.x < 144:
            velocity[0]= -velocity[0]
        if not 0 < ball.y < 110:
            velocity[1] = -velocity[1]

        # move computer paddle
        # move the 3 parts to be in the y value of the ball
        computer_paddle[0].move(computer_paddle[1].x, ball.y-10)
        computer_paddle[1].move(computer_paddle[1].x, ball.y)
        computer_paddle[2].move(computer_paddle[1].x, ball.y+10)


        # make the ball bounce if touch the paddles
        if (ball.x > 120 and ball.x < 142 and ball.y < paddle_d.y + 20 and ball.y > paddle_d.y - 20):
            velocity[0]= -velocity[0]
        if (ball.x > 120 and ball.x < 142 and ball.y < paddle_e.y + 20 and ball.y > paddle_e.y - 20):
            velocity[0]= -velocity[0]
        if (ball.x > 120 and ball.x < 142 and ball.y < paddle_f.y + 20 and ball.y > paddle_f.y - 20):
            velocity[0]= -velocity[0]
        # bouncing the ball in computer paddle
        if (ball.x > 15 and ball.x < 20 and ball.y < paddle_a.y + 20 and ball.y > paddle_a.y - 20):
            velocity[0]= -velocity[0]
        if (ball.x > 15 and ball.x < 20 and ball.y < paddle_b.y + 20 and ball.y > paddle_b.y - 20):
            velocity[0]= -velocity[0]
        if (ball.x > 15 and ball.x < 20 and ball.y < paddle_c.y + 20 and ball.y > paddle_c.y - 20):
            velocity[0]= -velocity[0]
        if computer_paddle == ball:
            coin_sound = open("coin.wav", 'rb')
            sound = ugame.audio
            sound.stop()
            sound.mute(False)
            sound.play(coin_sound)
        if user_paddle == ball:
            coin_sound = open("coin.wav", 'rb')
            sound = ugame.audio
            sound.stop()
            sound.mute(False)
            sound.play(coin_sound)
        # redraw sprite list
        game.render_sprites(computer_paddle + user_paddle + sprites)
        game.tick()  # wait until refresh rate finishes

def game_over_scene():
    # this function is the game over scene

    # repeat forever, game loop
    while True:
        text = []
        text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
        text1.move(60, 10)
        text1.text("GAME OVER")
        text.append(text1)

        # update game logic
        keys = ugame.buttons.get_pressed()
        # Wait for 1 seconds
        if keys & ugame.K_SELECT!= 0:
            key = 0
            mt_splash_scene()

        # redraw sprite list
        pass # just a placeholder until you write the code


if __name__ == "__main__":

    blank_white_reset_scene()