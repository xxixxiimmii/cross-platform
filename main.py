from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# อ่านไฟล์ KV
Builder.load_file('login.kv')

class LoginScreen(Screen):
    def validate_login(self, username, password):
        if username == 'admin' and password == 'password':
            self.manager.current = 'training'
        else:
            print("Invalid username or password")

class TrainingScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class LicenseApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(TrainingScreen(name='training'))
        sm.add_widget(RegisterScreen(name='register'))
        return sm

if __name__ == '__main__':
    LicenseApp().run()
