# -*- coding: utf-8 -*-
#Reglage encoding
import wx
import wx.adv
from multiprocessing import Process

def _play(m):
   out = open("/dev/dsp", "wb")
   out.write(m)
   out.close()

class son :
    def __init__(self) :
        self.sons = {
            'debut':self.read_wav("sound/debut.raw"),
            'fin_tour': self.read_wav("sound/fin_tour.raw"),
            'valid': self.read_wav("sound/valid.raw")
        }

    def play(self, m):
        p = Process(target=_play, args=(m,))
        p.start()

    def play_debut(self, m) :
        self.play(self.sons['debut'])
        return m

    def play_valid(self, m) :
        self.play(self.sons['valid'])
        return m

    def play_fin_tour(self, m) :
        self.play(self.sons['fin_tour'])
        return m

    def read_wav(self, name):
        f = open(name, "rb")
        ret = f.read()
        f.close()
        return ret

if __name__ == '__main__':
    s = son()
