#!/usr/bin/env python3
# coding: utf8
import pyxel
class App:
    def __init__(self):
        pyxel.init(96, 54, caption="Sound API")
        self.__set_sound()
        self.__play()
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.is_play: self.__stop()
            else: self.__play()
    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, 'Please SPACE key: ' + ('PLAY' if self.is_play else 'STOP'), 7)
    def __play(self):
        pyxel.play(self.ch1, [self.sound00], loop=True)
        self.is_play = True
    def __stop(self):
        pyxel.stop()
        self.is_play = False
    def __set_sound(self):
        self.ch1 = 0
        self.sound00 = 0
        self.notes = "c2d2e2f2g2a2b2c3"
        self.tones = "p"
        self.volumes = "6"
        self.effects = "n"
        self.speed = 30
        pyxel.sound(self.sound00).set(
            self.notes,
            self.tones,
            self.volumes ,
            self.effects ,
            self.speed,
        )
App()
