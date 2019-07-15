#!/usr/bin/env python2
# -*- coding: UTF8 -*-

from twisted.internet import wxreactor
wxreactor.install()
from twisted.internet import reactor
import wx
import wxscrab

app = wxscrab.App()
reactor.registerWxApp(app)
reactor.run()
