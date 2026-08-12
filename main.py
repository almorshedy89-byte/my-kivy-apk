import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

import arabic_reshaper
from bidi.algorithm import get_display

ARABIC_FONT = 'arial.ttf'

def fix_arabic(text):
    # إعادة تشكيل الحروف العربية وتوصيلها وتعديل الاتجاه
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

class DemoApp(App):
    def build(self):
        self.title = "Kivy Test App"
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = Label(
            text=fix_arabic("مرحباً بك في Kivy!"), 
            font_size='26sp',
            font_name=ARABIC_FONT
        )
        layout.add_widget(self.label)
        
        btn = Button(
            text=fix_arabic("اضغط هنا للاختبار"),
            font_size='20sp',
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 1, 1),
            font_name=ARABIC_FONT
        )
        btn.bind(on_press=self.on_button_click)
        layout.add_widget(btn)
        
        return layout

    def on_button_click(self, instance):
        self.label.text = fix_arabic("التطبيق شغال بنجاح 100%!")
        self.label.color = (random.random(), random.random(), random.random(), 1)

if __name__ == '__main__':
    DemoApp().run()
