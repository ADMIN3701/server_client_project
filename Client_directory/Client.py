import socket
import os
import time


from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 600)
Config.set("graphics", "height", 400)

class MyApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation="vertical", size_hint=[.4, .4])

        self.text_input = TextInput(text="Enter")
        bl.add_widget(self.text_input)
        bl.add_widget(Button(text="Я кнопка, ага!", on_press=self.button_press))

        al.add_widget(bl)

        return al

    def button_press(self, instance):
        print("Кнопка нажата")
        instance.text = self.text_input.text

if __name__ == "__main__":
    MyApp().run()



# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# while True:
#     try:
#         print("Подключение...")
#         client.connect(("192.168.0.167", 1234))
#         print("Подключено!")
#         while True:
#             client.send(input().encode("utf-8"))
#     except:
#         print("Не удалось подключиться.")
#         time.sleep(2)
