# SOTF-Trials
more or less private research on basic neural networks and how they work

> ######&copy; 2016 - David Gnauck, Hans Wegener

This project was created under Python 3.5.2 and uses pygame for the displayed
window. There is NO IMPLEMENTATION of any neural network activity at the moment,
what makes this map generator a base for all upcoming ideas and other features.

So all you need (for now) to get it work are the modules:
- 'pygame'
- 'noise'
___

The application is started by clicking on main.py
You should then see a window with a procedural generated tiled map.
The controls are as follows:

- Use the arrow keys or drag the mouse while pressing the right mouse button to
	move the map around.
- Use the mouse wheel to zoom in and out
- Press F2 to generate another map
- Press F3 or F5 to turn off and on the rendering (maybe useful later on)
- Press F8 or F9 to save and load a specific map (only one map is stored at once)
- Press F11 to toggle between windowed and fullscreen mode
- Press F12 to take a screenshot with date and time imformation in 'app' folder
- Press Esc to exit

___

You can change the parameters for how the map is generated by opening the Params.py
and playing around. Adjusting these values should be easier in the future, but for
now it suffice.

___

That's it.
Not pretty much at all, but at least it's a base for what we want to achieve.

Have fun.
