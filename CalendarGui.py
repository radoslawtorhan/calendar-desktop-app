from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from user import UserAPI


class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.user = UserAPI()

        # Create widgets
        self.calendar = QtWidgets.QCalendarWidget()
        self.event_list = QtWidgets.QListWidget()
        self.event_input = QtWidgets.QLineEdit()
        self.add_event_button = QtWidgets.QPushButton("Add Event")
        self.user_combo_box = QtWidgets.QComboBox()
        self.user_combo_box.addItems(self.user.get_all_users())
        self.add_user_button = QtWidgets.QPushButton("Add User")
        self.user_input = QtWidgets.QLineEdit()

        # Create layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.event_list)
        layout.addWidget(self.event_input)
        layout.addWidget(self.add_event_button)
        layout.addWidget(self.user_combo_box)
        layout.addWidget(self.user_input)
        layout.addWidget(self.add_user_button)

        # Set layout
        self.setLayout(layout)

        # Connect signals
        self.calendar.selectionChanged.connect(self.display_events)
        self.add_event_button.clicked.connect(self.add_event)
        self.user_combo_box.currentIndexChanged.connect(self.update_user)
        self.add_user_button.clicked.connect(self.add_user)

    def display_events(self):
        if self.user.current_user:
            date = self.calendar.selectedDate()
            events = self.user.get_events(date)
            self.event_list.clear()
            self.event_list.addItems(events)
        else:
            print('add user first')

    def add_event(self):
        if self.user.current_user:
            event = self.event_input.text()
            date = self.calendar.selectedDate()
            self.user.add_event(date, event)
            self.display_events()
        else:
            print('add user first')

    def add_user(self):
        name = self.user_input.text()
        self.user.add_user(name)
        self.user_combo_box.addItem(name)
        print('user added')

    def update_user(self):
        user = self.user_combo_box.currentText()
        self.user.set_current_user(user)
        self.display_events()



if __name__ == '__main__':
    app = QApplication([])
    calendar_organizer = GUI()
    calendar_organizer.show()
    app.exec_()