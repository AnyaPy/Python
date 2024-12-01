import sys
from PyQt5.QtWidgets import *
from users_database import users

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("будь який тайтл")
        self.setGeometry(700, 450, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        form_layout = QFormLayout()



        self.username_input = QLineEdit()

        self.password_input = QLineEdit()


        form_layout.addRow("Username", self.username_input)
        form_layout.addRow("Password", self.password_input)
        main_layout = QVBoxLayout(central_widget)
        main_layout.addLayout(form_layout)

        get_data_button = QPushButton("Зареєструватися")
        main_layout.addWidget(get_data_button)

        get_data_button.clicked.connect(self.get_values)

    def get_values(self):
        name = self.username_input.text()
        password = self.password_input.text()
        print(name)
        print(password)
        if name in users:
            print("Hi, " + name)
        else:
            print("Hi, Anonym")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())