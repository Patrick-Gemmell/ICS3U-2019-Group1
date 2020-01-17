.. _space_ship:

Tank
==========

In this project we used a series of 16 pixels by 16 pixels picture to act as our characters, enemies and such. All we did was make a 16x256 file and inserted the  sprites along the picture and then uploaded to the pybadge.

.. figure:: https://raw.githubusercontent.com/Patrick-Gemmell/ICS3U-2019-Group1/master/docs/image_bank/sprites.bmp
    :height: 256 px
    :align: center
    :alt: Image Bank for Shooter Shootout

Next we continued to use the sprite and find a way to move it around, and this was how we did it.

.. code-block:: python
	:linenos:
        
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
X
