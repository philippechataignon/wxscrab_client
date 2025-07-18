#!/usr/bin/env python3
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Dialog Test", size=(500, 400))
        self.panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.log = wx.TextCtrl(
            self.panel,
            wx.ID_ANY,
            size=(400, 300),
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL,
        )
        self.button = wx.Button(self.panel, label="Click me")
        sizer.Add(self.log, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.button, 0, wx.EXPAND | wx.ALL, 10)
        self.panel.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        dlg = GetData(parent=self.panel)
        dlg.ShowModal()
        if dlg.result_name:
            self.log.AppendText("Name: " + dlg.result_name + "\n")
            self.log.AppendText("Surname: " + dlg.result_surname + "\n")
            self.log.AppendText("Nickname: " + dlg.result_nickname + "\n")
        else:
            self.log.AppendText("No Input found\n")
        dlg.Destroy()


class GetData(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Name Input", size=(650, 220))
        self.panel = wx.Panel(self, wx.ID_ANY)

        self.lblname = wx.StaticText(self.panel, label="Name", pos=(20, 20))
        self.name = wx.TextCtrl(self.panel, value="", pos=(110, 20), size=(500, -1))
        self.lblsur = wx.StaticText(self.panel, label="Surname", pos=(20, 60))
        self.surname = wx.TextCtrl(self.panel, value="", pos=(110, 60), size=(500, -1))
        self.lblnick = wx.StaticText(self.panel, label="Nickname", pos=(20, 100))
        self.nickname = wx.TextCtrl(
            self.panel, value="", pos=(110, 100), size=(500, -1)
        )
        self.saveButton = wx.Button(self.panel, label="Save", pos=(110, 160))
        self.closeButton = wx.Button(self.panel, label="Cancel", pos=(210, 160))
        self.saveButton.Bind(wx.EVT_BUTTON, self.SaveConnString)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.Show()

    def OnQuit(self, event):
        self.result_name = None
        self.Destroy()

    def SaveConnString(self, event):
        self.result_name = self.name.GetValue()
        self.result_surname = self.surname.GetValue()
        self.result_nickname = self.nickname.GetValue()
        self.Destroy()


app = wx.App()
frame = MyFrame(None)
frame.Show()
app.MainLoop()
