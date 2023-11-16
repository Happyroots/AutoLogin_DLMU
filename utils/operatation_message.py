from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt, pyqtSignal
import sys
import asyncio

dir_login_cache = 'login_cache.txt'

def save_message(username, password, domain = 'Mobile'):
    with open(dir_login_cache,'w+',encoding='utf-8') as message:
        dict = {'username': username, 'password': password, 'domain': domain}
        message.write(str(dict))

def read_message():
    try:
        with open(dir_login_cache, 'r', encoding='utf-8') as message:
            dict = eval(message.read())
            #print(dict)
            username = dict['username']
            password = dict['password']
            domain = dict['domain']
            file_state = 1
            if(username == ""  or password == ""):
                message.close()
                get_usernamePassword_from_user()
                file_state,username,password,domain = read_message()
            #print("read complite")
            return file_state,username,password,domain
    except SyntaxError:
        #print('no message')
        file_state = 0
        username = 0
        password = 0
        domain = 0
        return file_state,username,password,domain
    except KeyError:
        #print('no key')
        file_state = 0
        username = 0
        password = 0
        domain = 0
        return file_state,username,password,domain
    except FileNotFoundError:
        #print('no file')
        file_state = 0
        username = 0
        password = 0
        domain = 0
        return file_state,username,password,domain
    except TypeError:
        #print('no str')
        file_state = 0
        username = 0
        password = 0
        domain = 0
        return file_state,username,password,domain


class LoginWindow(QWidget):
    login_successful = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("输入密码后再运行一次吧\n如果还不行，就修改login_cache.txt")
        self.setGeometry(0, 0, 300, 200)

        self.username_label = QLabel("Username:", self)
        self.username_label.move(50, 30)
        self.username_edit = QLineEdit(self)
        self.username_edit.move(120, 30)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(50, 70)
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.move(120, 70)

        self.login_button = QPushButton("Login", self)
        self.login_button.move(120, 120)
        self.login_button.clicked.connect(self.login)

        self.center_on_screen()

    def center_on_screen(self):
        screen = QDesktopWidget().availableGeometry()
        window_size = self.geometry()
        x = (screen.width() - window_size.width()) / 2
        y = (screen.height() - window_size.height()) / 2
        self.move(x, y)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.login()

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        print(f"Username: {username}")
        print(f"Password: {password}")

        if username and password:
            self.login_successful.emit(username, password)
            self.close()  # Close the window if both username and password are provided

def get_usernamePassword_from_user():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.login_successful.connect(save_message)
    window.show()
    sys.exit(app.exec_())

