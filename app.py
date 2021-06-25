import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.clock import Clock


Builder.load_string("""
<MenuScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Remover"
            
        MDLabel:
            text: "Clicca su 'enter url' per immettere un immagine dal web oppure clicca sulla fotocamera per fare una foto"
            halign: "center"
            
        MDRaisedButton:
            text: "Enter URL"
            md_bg_color: 1, 0, 1, 1
            pos: 500, 300
            pos_hint: {'center_x': 0.5}
            on_press: app.show_confirmation_dialog()
        
        MDBottomAppBar:

            MDToolbar:
                icon: "camera"
                type: "bottom"
                mode: "free-end"   
<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    namee: namee
    MDTextField:
        id: namee
        hint_text: "URL"
        on_text: app.process()
    MDRaisedButton:
        text: "Enter URL"
        md_bg_color: 1, 0, 1, 1
        pos: 500, 300
        pos_hint: {'center_x': 0.5}
    MDRectangleFlatButton:
        text: "Submit"
        pos_hint : {'center_x':0.5 ,'center_y':0.4}
        text_color: 0, 0, 1, 1
        md_bg_color: 1, 1, 0, 1
        on_release:
            print("success")
            app.submit()

""")

class MenuScreen(Screen):
    namee = ObjectProperty()
    pass

class Content(BoxLayout):
    namee = ObjectProperty()
    screen_manager = ObjectProperty()
    pass

class Test(MDApp):
    dialog = None
    namee = ObjectProperty()
    def build(self, **kwargs):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        return sm

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()
    
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        Clock.schedule_once(self.init_namee, 0)  
    
    def init_seq_text_box(self, *args):
        self.namee = self.parent.ids.namee
        
    def process(self,**kwargs):
        super(Test, self).__init__(**kwargs)
        print(self.root.ids.namee.text)
    


Test().run()


