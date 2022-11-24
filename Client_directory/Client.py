import pyautogui
import socket
import os
import time


from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 600)
Config.set("graphics", "height", 400)

class MyApp(App):
    def build(self):
        bl = BoxLayout()
        fl = FloatLayout(size = (200, 200))
        self.text_input = TextInput()
        bl.add_widget(self.text_input(
            text="Введите текст",
            pos=(600 / 2 - 150, 400 / 2 - 50),
            size_hint=(.5, .25)))

        bl.add_widget(Button(
            text="Я кнопка!",
            on_press=self.button_press,
            pos=(600/2 - 150, 400/2 - 50),
            size_hint=(.5, .25)))

        print(self.text_input)

        return bl

    def button_press(self, instance):
        print("Кнопка нажата")
        instance.text = "Я нажата!"

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
