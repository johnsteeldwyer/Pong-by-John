# Pong! by John
## Video Demo:
#### https://www.youtube.com/watch?v=7PVtS384PAo&ab_channel=RadChads
## Introduction
Hello, world! My name is John, and well, this is Pong! If that needs more explaining, perhaps you should get out from under that rock you've been hiding under since 1972!

With that said, I have no clue how they built pong in the 70's... one big takeaway I've had from this project is the extent to which I (and all the rest of us in the dark art of programming) stand on the shoulders of giants. 

## Turtle, Libraries, and OOP
Anyway, lets dive into how *I* did this! *Pong! by John* is built on Python, using the help the Turtle library. For the uninitiated, Turtle is a library that is included with Python and basically has a bunch of code that allows you to transfer what you write in Python into a graphical interface. I definitely spent a TON of time fidgeting and testing with Turtle, as prior to Cs50 I had no experience with it. Fortunately, Turtle is very well documented and I was able to rely almost exclusively on its official documentation to solve my bugs/woes.

One techinque that I had to rely on heavily for *Pong! by John* was Object-Oriented-Programming (OOP). Writing the game procedurally would have been beyond the scope of my ability, and quite possibly patience. While Cs50 did not explicitly cover OOP, I was able to piece together enough through Youtube tutorials to get the gist of it, and it ultimately made my life easier when it came to tweaking settings and debugging.

## Main.py, Scoreboard.py and Paddle.py
### Main.py
In main, the program initalizes all of the objects (Paddles, Ball & Scoreboard). There is a listener that checks for key presses (Up, Down, 'w' and 'd'). It also sets a while loop thats runs continuously, refreshing every 10 milliseconds (I found this to be the optimal framerate for smooth ball motion). With each frame, main.py checks if the ball is out of bounds (thus giving a point), if the ball hits the floor/ceiling, and if the ball is hit by a paddle. On each event, a method is called - either telling the ball to do something, or to update the scoreboard.
### Scoreboard.py
The Scoreboard object class is straightforward: it takes as an input what side it should be on, and depending on whether is is 'l' or 'r' is initialized on the appropriate side of the court. When the scoreboard.score() method is called, it updates, giving itself a point. Pretty straightforward from a design perspective
### Paddle.py
Implementing the paddle was tricker than the scoreboard, but still fairly straightforward. It has two methods, paddle.up() and paddle.down(), and I hope their functions speak for themselves.
## Ball.py - *The Strugglebus*
That pesky ball was easily the trickest part of the project to implement!

I could write a novel detailling ill-conceived design decisions, movement dynamics, reviewing middle-school geometry, and endless debugging, but I will spare you. Ultimately, I'm very happy with how it turned out - but please, test it because I'm sure there are still bugs hidden somewhere in that accursed file!
## Thank You and Enjoy Playing!

