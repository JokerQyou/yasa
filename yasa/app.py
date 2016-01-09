# coding: utf-8
from __future__ import unicode_literals
# import netifaces
import requests
import rumps
import webbrowser


class Yasa(rumps.App):

    @rumps.clicked('实时图像（静态）')
    def sayhi(self, sender):
        webbrowser.open('http://192.168.1.233:9876/camera/shot')

    @rumps.timer(60)
    def show_temperature(self, sender):
        data = requests.get(
            'http://192.168.1.233:9876/sensors/temperature'
        ).json()
        self.title = '气温 {:.2f}°C'.format(
            data['temperature']
        )

if __name__ == '__main__':
    Yasa('Yasa').run()
