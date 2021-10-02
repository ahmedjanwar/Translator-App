from re import MULTILINE
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from translate import Translator
#configure the keybord problem not needed mostly
#from kivy.config import Config
#Config.set('kivy', 'keyboard_mode', 'systemandmulti')

class translatorApp(App):
    def build(self,**kwargs):
        self.window = GridLayout()
        #colomnst needed(any as you want)
        self.window.cols=1
        #....................................
        #design and style
        #..........................................
        self.window.size_hint =(0.6,0.7)
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}
        #images
        self.window.add_widget(Image(source="logo.jpg"))
        #lable 
        #question
        self.question =Label(
            text="write the word to be translated",
            font_size = 25,
            color= '#FFFF00'
            )
        self.window.add_widget(self.question)
        #result
        #self.result=Label(text="")
        #self.window.add_widget(self.result)
        #user input 
        # text
        self.user=TextInput(
            multiline=False,
            size_hint =(1,0.5)
            )
        self.window.add_widget(self.user)
        #lang_label
        self.lang=Label(
            text="write the language as en for english",
            font_size=25,
            color='#FFFF00'
            )
        self.window.add_widget(self.lang)
         #language 
        self.lang=TextInput(
                multiline=False,
                size_hint =(1,0.5)
                )
        self.window.add_widget(self.lang)
        #Button T
        self.btn =Button(
            text="Translate",
            font_size=20,
            size_hint=(0.5,0.5),
            bold= True,
            background_color='#964B00'
            )
        self.btn.bind(on_press=self.action_btn)
        self.window.add_widget(self.btn)
        #Button ch
        #self.btns=Button(text="spanish")
        #self.btns.bind
        #trans function     
        return self.window
        #event handling or call back action
    def action_btn(self,instance):#instance or event 
      translator=Translator(from_lang="english",to_lang=self.lang.text)
      trans=translator.translate(self.user.text)
      self.question.text="Translated : " + trans

if __name__ == "__main__":
    translatorApp().run()
    
