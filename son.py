# -*- coding: utf-8 -*-
# Reglage encoding
import wx
import wx.adv


class son:
    def __init__(self):
        self.sons = {
            "debut": wx.adv.Sound("sound/debut.wav"),
            "fin_tour": wx.adv.Sound("sound/fin_tour.wav"),
            "valid": wx.adv.Sound("sound/valid.wav"),
        }

    def play_debut(self, m):
        self.sons["debut"].Play(wx.adv.SOUND_ASYNC)
        return m

    def play_valid(self, m):
        self.sons["valid"].Play(wx.adv.SOUND_ASYNC)
        return m

    def play_fin_tour(self, m):
        self.sons["fin_tour"].Play(wx.adv.SOUND_ASYNC)
        return m


if __name__ == "__main__":
    s = son()
