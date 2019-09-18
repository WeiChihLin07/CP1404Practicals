"""Kivy box_layout_demo for CP1404/CP5632"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet user with Hello + username"""
        print('test')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_event(self):
        """Clear the Text Input field and reset the output_label field"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
