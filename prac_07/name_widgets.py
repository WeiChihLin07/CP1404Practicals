"""CP1404/CP5632 -
Create an app that has a list of names (strings) and displays each one as a separate Label."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class NameWidgetsApp(App):
    """Main program - Kivy app to name widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_label = ["James Brian", "Peter Parker", "Hugh Jackman"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Name Widgets"
        self.root = Builder.load_file('name_widgets.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Labels from list entries and add them to the GUI."""
        for name in self.name_to_label:
            self.root.ids.entries_box(name)


NameWidgetsApp().run()
