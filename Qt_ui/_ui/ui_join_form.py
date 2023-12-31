# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_join_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_joinForm(object):
    def setupUi(self, joinForm):
        joinForm.setObjectName("joinForm")
        joinForm.resize(400, 500)
        joinForm.setMinimumSize(QtCore.QSize(400, 500))
        joinForm.setMaximumSize(QtCore.QSize(400, 500))
        self.le_id_input = QtWidgets.QLineEdit(joinForm)
        self.le_id_input.setGeometry(QtCore.QRect(110, 120, 180, 30))
        self.le_id_input.setObjectName("le_id_input")
        self.le_pw_input = QtWidgets.QLineEdit(joinForm)
        self.le_pw_input.setGeometry(QtCore.QRect(110, 160, 180, 30))
        self.le_pw_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pw_input.setObjectName("le_pw_input")
        self.le_cpw_input = QtWidgets.QLineEdit(joinForm)
        self.le_cpw_input.setGeometry(QtCore.QRect(110, 200, 180, 30))
        self.le_cpw_input.setObjectName("le_cpw_input")
        self.label = QtWidgets.QLabel(joinForm)
        self.label.setGeometry(QtCore.QRect(170, 50, 56, 20))
        self.label.setObjectName("label")
        self.le_name_input = QtWidgets.QLineEdit(joinForm)
        self.le_name_input.setGeometry(QtCore.QRect(110, 240, 180, 30))
        self.le_name_input.setObjectName("le_name_input")
        self.btn_open_login = QtWidgets.QPushButton(joinForm)
        self.btn_open_login.setGeometry(QtCore.QRect(130, 450, 140, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_open_login.setFont(font)
        self.btn_open_login.setStyleSheet("QPushButton {\n"
"background-color: #000000;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}")
        self.btn_open_login.setObjectName("btn_open_login")
        self.le_contact_input = QtWidgets.QLineEdit(joinForm)
        self.le_contact_input.setGeometry(QtCore.QRect(110, 280, 180, 30))
        self.le_contact_input.setObjectName("le_contact_input")

        self.retranslateUi(joinForm)
        QtCore.QMetaObject.connectSlotsByName(joinForm)

    def retranslateUi(self, joinForm):
        _translate = QtCore.QCoreApplication.translate
        joinForm.setWindowTitle(_translate("joinForm", "회원가입"))
        self.le_id_input.setPlaceholderText(_translate("joinForm", "차량 번호판"))
        self.le_pw_input.setPlaceholderText(_translate("joinForm", "비밀번호"))
        self.le_cpw_input.setPlaceholderText(_translate("joinForm", "비밀번호 확인"))
        self.label.setText(_translate("joinForm", "회원가입"))
        self.le_name_input.setPlaceholderText(_translate("joinForm", "이름"))
        self.btn_open_login.setText(_translate("joinForm", "가입하기"))
        self.le_contact_input.setPlaceholderText(_translate("joinForm", "연락처"))
