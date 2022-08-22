from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ConverterApp(MDApp):

    def flip(self):
        print("working..")

    def convert(self, args):
        val = int(self.txtInput.text,2)
        self.lblPrimary.text = str(val)

    def build(self):
        screen = MDScreen()
        #UI Widgets go here
        ## top toolbar
        self.toolbar = MDTopAppBar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        ##logo
        screen.add_widget(Image(source="logo.png", pos_hint = {"center_x": 0.5, "center_y": 0.7}))

        ## input
        self.txtInput = MDTextField(
            hint_text = "Enter a binary number",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            font_size = 22
        )
        screen.add_widget(self.txtInput)

        ## label primary and secondary
        self.lblSecondary = MDLabel(
            text="In decimal is: ",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color = "Secondary"
        )
        self.lblPrimary = MDLabel(
            text="888",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style = "H5"
        )
        screen.add_widget(self.lblPrimary)
        screen.add_widget(self.lblSecondary)

        ## button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            font_size = 18,
            on_press = self.convert
        ))

        return screen

if __name__ == '__main__':
    ConverterApp().run()