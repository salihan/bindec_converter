from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ConverterApp(MDApp):

    def flip(self):
        self.lblPrimary.text = ""
        self.txtInput.text = ""
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to binary"
            self.txtInput.hint_text = "Enter a decimal number"
            self.lblSecondary.text = "In binary: "
        else:
            self.state = 0
            self.toolbar.title = "Binary to decimal"
            self.txtInput.hint_text = "Enter a binary number"
            self.lblSecondary.text = "In decimal: "


    def convert(self, args):
        if self.state == 0:
            val = int(self.txtInput.text,2)
            self.lblPrimary.text = str(val)
        else:
            val = bin(int(self.txtInput.text))[2:]
            self.lblPrimary.text = val

    def build(self):
        screen = MDScreen()
        self.state = 0
        self.theme_cls.primary_palette = "DeepOrange"
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
            text = "In decimal:",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color = "Secondary"
        )
        self.lblPrimary = MDLabel(
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