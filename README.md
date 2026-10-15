This is a heavily sub-optimal way of generating a letter pair for edges and corners of the 3x3 Rubik's Cube.

The cube_attributes file houses the corner and edge letter memo identifiers. The default here follows the Speffz lettering scheme, though this has not been tested with other letter schemes.
The issue here is hard-coded letter tracings and swaps.
This works by mapping all 24 edge and corner pieces to a list, then reordering the list based on how any individual move affects the order.
We then go through checks to see which pieces are already solved (i.e. can be skipped) and then apply a loop to show how each piece maps from buffer -> helper -> target
There is also a a final handling of swapping buffer if parity exists for edge swaps

The edge buffer is set at DF (letter U in Speffz) and the corner buffer is UFR (letter C in Speffz).

The tracing_attributes file houses the order for edge and corner tracing. Again, this has not been tested with different orders.

The generate_scramble file houses the instantiation of a new scramble, and the corresponding letter pairs. This runs once per file execution and fully wipes the console per session each time the script is executed.

Please feel free to take any inspiration from this simple script for own personal use! 
