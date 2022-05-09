import sys
from PyQt5 import QtCore, QtWidgets
from login import *
from register import *
from menu import *
from SignToText import *
import pyrebase 

firebaseConfig = {
  "apiKey": "AIzaSyADDYyNQOJiRy18MUi9lk3P1wG_PeZ2Ak8",
  "authDomain": "asl-interpreter-4b1fa.firebaseapp.com",
  "projectId": "asl-interpreter-4b1fa",
  "storageBucket": "asl-interpreter-4b1fa.appspot.com",
  "messagingSenderId": "661711895566",
  "appId": "1:661711895566:web:c70da854a6e3de8e9cd05f",
  "measurementId": "G-EWNBXMNCQ1",
  "databaseURL": "https://asl-interpreter-4b1fa-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()



class Controller:

    def __init__(self):
        self.flag = 0

    def show_login(self):
       
        if(self.flag ==1):
            self.RegisterForm.close()
        
        self.flag = 1
        self.Login = login()
        self.LoginForm = QtWidgets.QWidget()
        self.Login.setupUi(self.LoginForm)
        self.Login.RegisterPage.clicked.connect(self.show_register)
        self.Login.loginBTN.clicked.connect(self.LoginUser)
        self.LoginForm.show()
        
      

    def show_register(self,prev):
       
        self.LoginForm.close()
        self.RegisterForm = QtWidgets.QWidget()
        self.Register = register()
        self.Register.setupUi(self.RegisterForm)
        self.Register.LoginPage.clicked.connect(self.show_login)
        self.Register.registerBTN.clicked.connect(self.RegisterUser)
        self.RegisterForm.show()
       
    def RegisterUser(self):
        email = self.Register.email.text()
        email_id = email
        Fname = self.Register.fname.text()
        Lname = self.Register.lname.text()
        if(self.Register.pswd.text()==self.Register.confirm_pswd.text()):
            pswd = self.Register.pswd.text()
            try:
                auth.create_user_with_email_and_password(email,pswd)
                data = {'fname': str(Fname),'lname':str(Lname),'Email':str(email_id)}
                db.push(data)
                print("Registered successfully")
                self.RegisterForm.close()
                self.LoginForm.show()

            except:
                print("Invalid",Fname,Lname)
        else:
            print("password didn't match")
          
        
    def LoginUser(self):
        email = self.Login.userid.text()
        pswd = self.Login.pswd.text()
        
        try:
            auth.sign_in_with_email_and_password(email,pswd)
            print("login successful")
            self.LoginForm.close()
            self.ShowMenu()
            
            
        except:
            print("Invalid email or password")

    def ShowMenu(self):
        self.MenuForm = QtWidgets.QWidget()
        self.Menu = menu()
        self.Menu.setupUi(self.MenuForm)
        self.Menu.toText.clicked.connect(self.ConvertToText)
        self.Menu.toSign.clicked.connect(self.ConvertToSign)
        self.Menu.logout.clicked.connect(self.LogoutUser)
        self.MenuForm.show()
           
    def ConvertToText(self):
        self.MenuForm.close()
        self.SignToTextForm = QtWidgets.QWidget()
        self.SignTOText = video(self.SignToTextForm)
        self.SignToTextForm.show()
        self.SignTOText.back.clicked.connect(self.BackMenu)
              

    def ConvertToSign(self):
        pass  

    def LogoutUser(self):
        self.MenuForm.close()
        self.show_login()

    def BackMenu(self):
        self.SignToTextForm.close()
        self.ShowMenu()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.ShowMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()