# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET

# XSD schema for the employee details
xsd = '''<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="employee">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="name" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="department" type="xs:string"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
'''

# Sample XML document for the employee details
xml = '''<?xml version="1.0"?>
<employees>
  <employee>
    <Eid>1</Eid>
    <name>Vaibhavi Patki</name>
    <age>20</age>
    <department>HR</department>
  </employee>
  <employee>
    <Eid>2</Eid>
    <name>Sakshi Kadam</name>
    <age>20</age>
    <department>Marketing</department>
  </employee>
  <employee>
    <Eid>3</Eid>
    <name>Prerana Lavhate</name>
    <age>21</age>
    <department>Research</department>
  </employee>
  <employee>
    <Eid>4</Eid>
    <name>Saklap Patil</name>
    <age>21</age>
    <department>Finance</department>
  </employee>
  <employee>
    <Eid>5</Eid>
    <name>Shivam Patil</name>
    <age>20</age>
    <department>Development</department>
  </employee>
  <employee>
    <Eid>6</Eid>
    <name>Rutuja Kagwade</name>
    <age>20</age>
    <department>Testing</department>
  </employee>
  <employee>
    <Eid>7</Eid>
    <name>Shreya Patil</name>
    <age>22</age>
    <department>Management</department>
  </employee>
  <employee>
    <Eid>8</Eid>
    <name>Sayali Mokashi</name>
    <age>21</age>
    <department>Marketing</department>
  </employee>
  <employee>
    <Eid>9</Eid>
    <name>Sanjana Kanmadi</name>
    <age>22</age>
    <department>HR</department>
  </employee>
  <employee>
    <Eid>10</Eid>
    <name>Ruturaj Gaikwad</name>
    <age>25</age>
    <department>Development</department>
  </employee>
  <employee>
    <Eid>11</Eid>
    <name>Parth Powar</name>
    <age>26</age>
    <department>Testing</department>
  </employee>
  <employee>
    <Eid>12</Eid>
    <name>Nita More</name>
    <age>30</age>
    <department>Management</department>
  </employee>
  <employee>
    <Eid>13</Eid>
    <name>Aayushi Kulkarni</name>
    <age>30</age>
    <department>Research</department>
  </employee>
  <employee>
    <Eid>14</Eid>
    <name>Gauri Joshi</name>
    <age>27</age>
    <department>HR</department>
  </employee>
  <employee>
    <Eid>15</Eid>
    <name>Akanksha Deshpande</name>
    <age>20</age>
    <department>Testing</department>
  </employee>
  <employee>
    <Eid>16</Eid>
    <name>Skand Kulkarni</name>
    <age>21</age>
    <department>Development</department>
  </employee>
  <employee>
    <Eid>17</Eid>
    <name>Ruchika Jadhav</name>
    <age>23</age>
    <department>Marketing</department>
  </employee>
  <employee>
    <Eid>18</Eid>
    <name>Pratik Sathe</name>
    <age>26</age>
    <department>Finance</department>
  </employee>
  <employee>
    <Eid>19</Eid>
    <name>Priya Mali</name>
    <age>27</age>
    <department>Finance</department>
  </employee>
  <employee>
    <Eid>20</Eid>
    <name>Suraj Suryawanshi</name>
    <age>25</age>
    <department>Testing</department>
  </employee>
</employees>
'''

# Load the XML document
root = ET.fromstring(xml)



class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(560, 531)
        MainWindow1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(236, 185, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_eid = QtWidgets.QLabel(self.centralwidget)
        self.label_eid.setGeometry(QtCore.QRect(120, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_eid.setFont(font)
        self.label_eid.setObjectName("label_eid")
        self.eid_input = QtWidgets.QLineEdit(self.centralwidget)
        self.eid_input.setGeometry(QtCore.QRect(290, 131, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eid_input.setFont(font)
        self.eid_input.setObjectName("eid_input")
        self.Getdetails_button = QtWidgets.QPushButton(self.centralwidget)
        self.Getdetails_button.setGeometry(QtCore.QRect(200, 220, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Getdetails_button.setFont(font)
        self.Getdetails_button.setObjectName("Getdetails_button")
        
        #pushbutton
        self.Getdetails_button.clicked.connect(self.get_employee_details)

        
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(100, 300, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(100, 360, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")
        self.label_department = QtWidgets.QLabel(self.centralwidget)
        self.label_department.setGeometry(QtCore.QRect(100, 420, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_department.setFont(font)
        self.label_department.setObjectName("label_department")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 22))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.label.setText(_translate("MainWindow1", "      EMPLOYEE DETAILS"))
        self.label_eid.setText(_translate("MainWindow1", "EID"))
        self.Getdetails_button.setText(_translate("MainWindow1", "Get Details"))
        self.label_name.setText(_translate("MainWindow1", "NAME"))
        self.label_age.setText(_translate("MainWindow1", "AGE"))
        self.label_department.setText(_translate("MainWindow1", "DEPARTMENT"))

    def get_employee_details(self):
        
        eid = self.eid_input.text()  # get the entered EID
        for employee in root.findall('employee'):  # loop over all employee elements
            if employee.find('Eid').text == eid:  # check if the current employee's Eid matches the entered EID
                # if there's a match, set the name, age, and department labels to the corresponding values
                self.label_name.setText(f"NAME: {employee.find('name').text}")
                self.label_age.setText(f"AGE: {employee.find('age').text}")
                self.label_department.setText(f"DEPARTMENT: {employee.find('department').text}")
                return  # exit the function
        # if no match is found, show an error message
        QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Employee not found")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())