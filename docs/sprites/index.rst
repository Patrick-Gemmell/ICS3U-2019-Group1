
Sprites
=======

Now that we have the background, lets place a single sprite on the screen. Sprites are handled differently than the background, they can be placed anywhere we want on the sceen, not just tiled. We will create a varaible that holds a specific image from the image bank. We will also create a **list** that will hold all the sprites we want to paint onto the screen. We will take our ship variable and add it to this list. 

Painting the entire screen each frame is not practical. The refresh rate just is not fast enough. Instead when the scene loads we will paint the background and then all the sprites on top of it. After that, each frame we will just redraw the sprites in the sprites list. This will let us have a much faster refesh rate. To accomplish this after we first paint the entire screen, we will create a loop, usually known as a gaming loop, that will keep running the code to update our sprites. 

.. literalinclude:: ./code/code.py
   :language: python
   :caption: code.py
   :linenos:
   :emphasize-lines: 15,16,24-28,33,34,40-48

.. note::

   Full code and assets that can be copied onto PyBadge for this step can be found `here <https://github.com/MotherTeresaHS/ICS3U-2019-Group0/tree/master/docs/sprites/code>`_.
