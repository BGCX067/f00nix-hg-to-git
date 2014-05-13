#!/usr/bin/env python

import os
import sys
import pyglet

def main():
	print('Working!!!')
	
	# create a window
	window = pyglet.window.Window()
	label = pyglet.text.Label('TestMode::war10ck_system', font_name = 'Courier New', font_size = 10, x = 10, y = 35)
	
	#music = pyglet.resource.media("test.mp3")
	#music.play()
	
	player = pyglet.media.Player()
	music = pyglet.media.load('test.mp3')
	player.queue(music)
	
	playDuration = pyglet.text.Label('Total Duration : ' + str(music.duration), font_name = 'Courier New', font_size = 10, x = 10, y = 20)
	player.play()
	playerTime = pyglet.text.Label('Playing Duration : ' + str(player.time), font_name = 'Courier New', font_size = 10, x = 10, y = 10)
	
	def on_update():
		print(player.time)
		print(music.duration)
	
	def update_play_time(inpPlayerTime):
		playerTime = pyglet.text.Label('Playing Duration : ' + str(inpPlayerTime), font_name = 'Courier New', font_size = 10, x = 10, y = 10)
		playerTime.draw()
	
	@window.event
	def on_draw():
		window.clear()
		label.draw()
		playDuration.draw()
		#playerTime.draw()
		on_update()
		update_play_time(player.time)

if __name__ == '__main__':
	main()
	pyglet.app.run()
