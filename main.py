#!/usr/bin/env python3

from twisted.internet import wxreactor

wxreactor.install()
from twisted.internet import reactor
import wx
import wxscrab

# from twisted.internet.defer import setDebugging
# setDebugging(True)

app = wxscrab.App()
reactor.registerWxApp(app)
reactor.run()
