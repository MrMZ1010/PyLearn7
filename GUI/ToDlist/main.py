#### MohammadAli Mirzaei ####

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database
from functools import partial

# Define a subclass of QMainWindow for the main application window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create an instance of the UI defined in main_window.py
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        # Create an instance of the Database class to interact with the database
        self.db=Database()
        self.new=0
        # Lists to keep track of dynamically created widgets
        self.lablelist=[]
        self.checkboxlist=[]
        self.btnlist=[]
        # Read tasks from the database and display them
        self.read_from_database()
        self.count_for_latest_task=[]

        # Connect the 'clicked' signal of the 'btn_new_task' QPushButton to the 'new_task' method
        self.ui.btn_new_task.clicked.connect(self.new_task)

    # Method to read tasks from the database and display them in the UI
    def read_from_database(self):
        # Delete previously created widgets
        for i in range(len(self.btnlist)):
            self.btnlist[i].deleteLater()
            self.checkboxlist[i].deleteLater()
            self.lablelist[i].deleteLater()
        
        # Clear lists tracking widgets
        self.btnlist.clear()
        self.checkboxlist.clear()
        self.lablelist.clear()
        # Fetch tasks from the database and sort them by priority
        self.tasks=self.db.get_task()
        self.tasks.sort(key=lambda x: x[3])
        # Iterate through the fetched tasks
        for i in range(len(self.tasks)):
            # Keep track of the latest task
            if self.new==1:
                self.new=0
                self.count_for_latest_task.append(self.tasks[len(self.tasks)-1][0])

            # Create checkboxes, buttons, and labels for each task
            new_checkBox=QCheckBox()
            new_btn=QPushButton()
            new_label=QPushButton()
            new_btn.setText("\U0001F5D1")
            self.btnlist.append(new_btn)
            self.checkboxlist.append(new_label)
            self.lablelist.append(new_checkBox)
            new_label.setText(self.tasks[i][1])

            # Set background color based on task priority
            if self.tasks[i][4]=='1':
                new_label.setStyleSheet(u"QPushButton\n"
                                        "{\n"
                                        "background-color: rgb(255, 136, 125);\n"
                                        "}\n"
                                        "QPushButton::pressed\n"
                                        "{\n"
                                        "background-color: rgb(255, 136, 125);\n"
                                        "}\n"
                                        )
            elif self.tasks[i][4]=='0':
                new_label.setStyleSheet(u"QPushButton\n"
                                        "{\n"
                                        "background-color: rgb(85, 255, 162);\n"
                                        "}\n"
                                        "QPushButton::pressed\n"
                                        "{\n"
                                        "background-color: rgb(85, 255, 162);\n"
                                        "}\n"
                                        "")
            # Add widgets to the grid layout in the UI
            self.ui.gl_tasks.addWidget(new_btn,i,2)
            self.ui.gl_tasks.addWidget(new_label,i,1)
            self.ui.gl_tasks.addWidget(new_checkBox,i,0)
            new_checkBox.setChecked(int(self.tasks[i][3])) 
            # Connect button and checkbox signals to appropriate methods
            new_btn.clicked.connect(partial(self.db.remove_task,self.tasks[i][0],self))
            new_label.clicked.connect(partial(self.show_description,self.tasks[i][2]))
            new_btn.setFixedWidth(40)
            new_checkBox.setFixedWidth(20)
            new_checkBox.stateChanged.connect(partial(self.db.task_done,self.tasks[i][0]))

    # Method to add a new task
    def new_task(self):
        # Set flag to indicate new task creation
        self.new=1
        # Get task details from UI inputs
        new_title=self.ui.tb_new_task.text()
        new_description=self.ui.tb_new_task_description.toPlainText()
        time=self.ui.time.text()
        # Determine task priority
        if self.ui.high.isChecked():
            priority='1'
        else:
            priority='0'
        # Attempt to add new task to the database
        feedback=self.db.add_new_tasks(new_title, new_description, priority, time)
        # If task addition is successful, update UI and clear input fields
        if feedback==True:
            self.read_from_database()
            self.ui.tb_new_task.setText("")
            self.ui.tb_new_task_description.setText("")
        else:
            # Display error message if task addition fails
            msg_box=QMessageBox()
            msg_box.setText("Error!")
            msg_box.exec()

    # Method to display task description
    def show_description(self,text):
        msg_box=QMessageBox()
        msg_box.setText(text)
        msg_box.exec()

# Entry point of the application
if __name__=="__main__":
    # Create QApplication instance
    app=QApplication(sys.argv)

    # Create MainWindow instance
    mainwindow=MainWindow()
    mainwindow.show()

    # Start the event loop
    app.exec()
