import socket
import os
import time


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.core.window import Window
Window.size = (300, 500)

class MyApp(App):
    def build(self):

        al = AnchorLayout()
        bl = BoxLayout(orientation="vertical", padding=25, spacing=25)
        self.text_input = TextInput(text="Введите текст...")
        self.label = Label()

        bl.add_widget(self.label)
        bl.add_widget(self.text_input)
        bl.add_widget(Button(text="Подтвердить текст", on_press=self.add_operation))

        al.add_widget(bl)
        return al

    def add_operation(self, instate):
        self.label.text = self.text_input.text
        print(self.text_input.text)


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
