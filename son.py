# -*- coding: utf-8 -*-
#Reglage encoding
import wx
import wx.adv
class son :
    def __init__(self) :
        self.sons = {
            'debut':self.read_wav("sound/debut.raw"),
            'fin_tour': self.read_wav("sound/fin_tour.raw"),
            'valid': self.read_wav("sound/valid.raw")
        }

    def play_debut(self, m) :
        self.play_dsp(self.sons['debut'])
        return m

    def play_valid(self, m) :
        self.play_dsp(self.sons['valid'])
        return m

    def play_fin_tour(self, m) :
        self.play_dsp(self.sons['fin_tour'])
        return m

    def play_dsp(self, data):
        out = open("/dev/dsp", "wb")
        out.write(data)
        out.close()

    def read_wav(self, name):
        f = open(name, "rb")
        ret = f.read()
        f.close()
        return ret

if __name__ == '__main__':
    s = son()
