# mims-animation
 Jupyter notebook that animates a Python Turtle rainbow drawing. Created during MIMS bootcamp alongside 4 classmates. 
 
# Prerequisites
* Python3
* Pip3
* Jupyter Notebook (`pip3 install jupyter`)

# How It Works
This project uses Jupyter Notebook, web-based interactive computing platform, to run a series of Python commands. The majority of the work is done using Turtle, a Python drawing library. 

## parts.py

A module called `parts.py` contains the main program functions which draw a cloud, a rainbow, and then animate the rainbow across the Turtle screen. 

* `draw_cloud`: Relies on other shape-drawing functions like `draw_c1` to draw a cloud
* `drawRays`, `draw_circle`: Combined these two draw a sun
* `draw_rainbow`: Draws a rainbow by drawing 7 semi-circles
* `move_rainbow`: Loops the drawing of the rainbow, making it appears as if the rainbow is moving horizontally. As `start_x` is increased at a regular internal, animation begins.

Additionally, 2 commands (`no_delay` and `setup`)in [Chris Proctor's](https://github.com/cproctor) `helpers.py` are utilized.  

## rainbow.ipynb

This is the main Jupyter Notebook which launches Turtle and creates the animation. 

![unnamed](https://user-images.githubusercontent.com/54450015/184468146-e79cf230-f016-4e93-8981-c7058d520f5d.gif)

The animation starts with a cloudy sky. After each iteration of the loop, the background color turns into a lighter shade of blue until on the 4th the sun comes out. 
