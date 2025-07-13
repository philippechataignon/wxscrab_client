# -*- coding: utf-8 -*-
import wx
import utils
import settings


class TooMuchTry(Exception):
    pass


class dlgconnframe(wx.Dialog):
    def __init__(self, parent=None):
        super().__init__(parent=None, title="wxScrab Connexion", size=(400, 300))
        panel = wx.Panel(self)
        icon = wx.Icon("images/wxscrab.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.settings = settings.settings()

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)

        fgs.Add(wx.StaticText(panel, label="Serveur"))
        self.txtaddr = wx.ComboBox(
            panel,
            value=self.settings["server_servers"][0],
            size=(250, -1),
            choices=self.settings["server_servers"],
        )
        self.txtaddr.SetFocus()
        fgs.Add(self.txtaddr, flag=wx.EXPAND)

        fgs.Add(wx.StaticText(panel, label="Port"))
        self.txtport = wx.TextCtrl(panel, value=str(self.settings["server_port"]))
        fgs.Add(self.txtport, flag=wx.EXPAND)

        fgs.Add(wx.StaticText(panel, label="Pseudo"))
        self.txtnom = wx.TextCtrl(
            panel, size=(150, -1), value=self.settings["user_pseudo"]
        )
        fgs.Add(self.txtnom, flag=wx.EXPAND)
        bok = wx.Button(panel, size=(150, 28), label="OK")
        bok.SetDefault()
        fgs.Add(10, 10)
        fgs.Add(10, 10)
        fgs.Add(10, 10)
        fgs.Add(bok, flag=wx.ALIGN_RIGHT)
        hbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)
        self.Bind(wx.EVT_CLOSE, self.onQuit)
        self.Bind(wx.EVT_BUTTON, self.click_button_ok, bok)
        self.Show()

    def onQuit(self, evt):
        self.nick = None
        self.host = None
        self.port = None
        self.Unbind(wx.EVT_CLOSE)
        self.Unbind(wx.EVT_BUTTON)
        self.EndModal(wx.CLOSE)

    def click_button_ok(self, evt):
        self.nick = self.txtnom.GetValue().strip()
        self.host = self.txtaddr.GetValue().strip()
        porterror = False
        try:
            self.port = int(self.txtport.GetValue())
        except ValueError:
            porterror = True
            utils.errordlg("Port invalide", "Erreur")

        if porterror:
            pass
        elif len(self.nick) == 0:
            utils.errordlg("Vous n'avez pas reglé de pseudo", "Erreur")
        elif len(self.nick) > 20:
            utils.errordlg("Pas plus de 20 caractères pour le pseudo", "Erreur")
        else:
            self.Unbind(wx.EVT_CLOSE)
            self.settings["server_port"] = self.port
            self.settings["user_pseudo"] = self.nick
            self.settings.insert_list("server_servers", self.host)
            self.settings.write()
            self.EndModal(wx.OK)

if __name__ == "__main__":

    class App(wx.App):
        def OnInit(self):
            # wx.InitAllImageHandlers()
            dlg = dlgconnframe()
            dlg.ShowModal()
            print(dlg.nick, dlg.host, dlg.port)
            return True

    app = App()
    app.MainLoop()
