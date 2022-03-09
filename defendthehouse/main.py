import pyglet
import pyglet.gl
from pyglet.gl import *
from game import Mainscreen, Levels, Game
from constants import icon

def main():
	screen = Game(1063, 592, "Defend The House")
	screen.set_icon(icon)
	screen.set_vsync(True)
	pyglet.clock.schedule_interval(screen.update, screen.frame_rate)
	pyglet.app.run()

if __name__ == "__main__":
	main() 