# coding: utf-8
import netifaces
import rumps


class Yasa(rumps.App):

    @rumps.clicked('Hi')
    def sayhi(self, _):
        rumps.notification('Hi', 'sub title', 'Hello rumps!')

if __name__ == '__main__':
    Yasa('Yasa').run()

