import os
import menu

class agent:
    def __init__(self, name, listener, remoteip, hostname, Type, key):

        self.name = name
        self.listener = listener
        self.remoteip = remoteip
        self.hostname = hostname
        self.Type = Type
        self.key = key

        self.sleept = 3

        self.path = "data/listeners/{}/agents/{}/".format(self.listener, self.name)
        self.taskPath = "{}tasks".format(self.path, self.name)

        if os.path.exists(self.path) == False:
            os.mkdir(self.path)

        self.menu = menu.Menu(self.name)
        self.menu.registerCommand("shell", "Execute a shell command.", "<command>")
        self.menu.registerCommand("powershell", "Execute a powershell command.", "<command>")
        self.menu.registerCommand("sleep", "Change agent's sleep time.", "<time (s)>")
        self.menu.registerCommand("clear", "Clear tasks.", "")
        self.menu.registerCommand("quit", "Task agent to quit.", "")

        