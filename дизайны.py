from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_welcomeForm(object):
    """ Класс дизайна приветственного виджета """

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/images/фон_вход_и_рег.jpg"))
        self.label.setObjectName("label")
        self.inputButton = QtWidgets.QPushButton(Form)
        self.inputButton.setGeometry(QtCore.QRect(250, 160, 171, 61))
        self.inputButton.setStyleSheet("font: 75 16pt \"a_AlbionicTitulBrk\";\n"
                                       "border-color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(236, 57, 126);\n"
                                       "background-color: rgb(62, 186, 186);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "")
        self.inputButton.setObjectName("inputButton")
        self.registrationButton = QtWidgets.QPushButton(Form)
        self.registrationButton.setGeometry(QtCore.QRect(250, 240, 171, 61))
        self.registrationButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                              "background-color: rgb(255, 255, 0);\n"
                                              "font: 75 14pt \"a_AlbionicTitulBrk\";\n"
                                              "color:rgb(234, 48, 15);\n"
                                              "border-color: rgb(0, 0, 0);\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(255, 149, 19);\n"
                                              "background-color: rgb(255, 170, 0);\n"
                                              "")
        self.registrationButton.setObjectName("registrationButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вход и регистрация"))
        self.inputButton.setText(_translate("Form", "ВХОД"))
        self.registrationButton.setText(_translate("Form", "РЕГИСТРАЦИЯ"))


class Ui_inputForm(object):
    """ Класс дизайна виджета входа """

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/images/фон_вход_и_рег.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 60, 81, 41))
        self.label_2.setStyleSheet("font: 63 30pt \"PF Cosmonut Pro\";\n"
                                   "color: rgb(199, 64, 141);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(210, 140, 61, 31))
        self.label_3.setStyleSheet("color: rgb(85, 0, 255);\n"
                                   "font: 63 18pt \"PF Cosmonut Pro\";\n"
                                   "color: rgb(199, 64, 141);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 220, 81, 31))
        self.label_4.setStyleSheet("color: rgb(85, 0, 255);\n"
                                   "font: 63 18pt \"PF Cosmonut Pro\";\n"
                                   "color: rgb(199, 64, 141);")
        self.label_4.setObjectName("label_4")
        self.login_label = QtWidgets.QTextEdit(Form)
        self.login_label.setGeometry(QtCore.QRect(290, 140, 181, 31))
        self.login_label.setStyleSheet("\n"
                                       "font: 63 12pt \"Myriad Pro Light\";")
        self.login_label.setObjectName("login_label")
        self.password_label = QtWidgets.QLineEdit(Form)
        self.password_label.setGeometry(QtCore.QRect(290, 220, 181, 31))
        self.password_label.setStyleSheet("font: 63 12pt \"Myriad Pro Light\";")
        self.password_label.setObjectName("password_label")
        self.password_label.setEchoMode(2)
        self.error = QtWidgets.QLabel(Form)
        self.error.setGeometry(QtCore.QRect(170, 260, 331, 31))
        self.error.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 0, 0);")
        self.error.setText("")
        self.error.setObjectName("error")
        self.inputButton = QtWidgets.QPushButton(Form)
        self.inputButton.setGeometry(QtCore.QRect(270, 300, 121, 41))
        self.inputButton.setStyleSheet("font: 63 20pt \"PF Cosmonut Pro\";\n"
                                       "color: rgb(199, 64, 141);\n"
                                       "background-color: rgb(230, 230, 230);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.inputButton.setObjectName("inputButton")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(0, 0, 51, 31))
        self.back.setStyleSheet(
                                "font: 10pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(199, 64, 141);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "")
        self.back.setObjectName("back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вход"))
        self.label_2.setText(_translate("Form", "Вход"))
        self.label_3.setText(_translate("Form", "Логин"))
        self.label_4.setText(_translate("Form", "Пароль"))
        self.inputButton.setText(_translate("Form", "Войти"))
        self.back.setText(_translate("Form", "Назад"))


class Ui_regForm(object):
    """ Класс дизайна виджета регистрации """

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 60, 181, 31))
        self.label.setStyleSheet("font: 22pt \"Yikes!\";\n"
                                 "color: rgb(199, 64, 141);\n"
                                 "font: 63 23pt \"PF Cosmonut Pro\";\n"
                                 "")
        self.label.setObjectName("label")
        self.name_text = QtWidgets.QTextEdit(Form)
        self.name_text.setGeometry(QtCore.QRect(320, 120, 181, 31))
        self.name_text.setStyleSheet(
                                     "font: 63 13pt \"Myriad Pro Light\";\n"
                                     "color: rgb(0, 0, 0);")
        self.name_text.setObjectName("name_text")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 120, 111, 31))
        self.label_2.setStyleSheet("color: rgb(199, 64, 141);\n"
                                   "font: 63 17pt \"PF Cosmonut Pro\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("data/images/фон_вход_и_рег.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 170, 51, 31))
        self.label_4.setStyleSheet(
                                   "font: 63 17pt \"PF Cosmonut Pro\";\n"
                                   "color: rgb(199, 64, 141);")
        self.label_4.setObjectName("label_4")
        self.login_text = QtWidgets.QTextEdit(Form)
        self.login_text.setGeometry(QtCore.QRect(320, 170, 181, 31))
        self.login_text.setStyleSheet("font: 63 13pt \"Myriad Pro Light\";\n"
                                      "color: rgb(0, 0, 0);")
        self.login_text.setObjectName("login_text")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(210, 220, 71, 31))
        self.label_5.setStyleSheet("font: 14pt \"Yikes!\";\n"
                                   "color: rgb(170, 0, 0);\n"
                                   "color: rgb(0, 170, 255);\n"
                                   "font: 63 18pt \"PF Cosmonut Pro\";\n"
                                   "color: rgb(199, 64, 141);")
        self.label_5.setObjectName("label_5")
        self.password_text = QtWidgets.QLineEdit(Form)
        self.password_text.setGeometry(QtCore.QRect(320, 220, 181, 31))
        self.password_text.setStyleSheet("font: 63 13pt \"Myriad Pro Light\";\n"
                                         "color: rgb(0, 0, 0);")
        self.password_text.setObjectName("password_text")
        self.password_text.setEchoMode(2)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(140, 280, 171, 16))
        self.label_6.setStyleSheet("font: 14pt \"Yikes!\";\n"
                                   "color: rgb(170, 0, 0);\n"
                                   "color: rgb(0, 170, 255);\n"
                                   "font: 63 17pt \"PF Cosmonut Pro\";\n"
                                   "color: rgb(199, 64, 141);")
        self.label_6.setObjectName("label_6")
        self.password2_text = QtWidgets.QLineEdit(Form)
        self.password2_text.setGeometry(QtCore.QRect(320, 270, 181, 31))
        self.password2_text.setStyleSheet("font: 63 13pt \"Myriad Pro Light\";\n"
                                          "color: rgb(0, 0, 0);")
        self.password2_text.setObjectName("password2_text")
        self.password2_text.setEchoMode(2)
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(0, 0, 51, 31))
        self.back.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "font: 10pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(199, 64, 141);\n"
                                "background-color: rgb(239, 239, 239);")
        self.back.setObjectName("back")
        self.registrationButton = QtWidgets.QPushButton(Form)
        self.registrationButton.setGeometry(QtCore.QRect(230, 330, 181, 31))
        self.registrationButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 63 16pt \"PF Cosmonut Pro\";\n"
                                              "color: rgb(199, 64, 141);\n"
                                              "background-color: rgb(230, 230, 230);")
        self.registrationButton.setObjectName("registrationButton")
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setGeometry(QtCore.QRect(170, 310, 381, 20))
        self.error_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.label_3.raise_()
        self.label.raise_()
        self.name_text.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.login_text.raise_()
        self.label_5.raise_()
        self.password_text.raise_()
        self.label_6.raise_()
        self.password2_text.raise_()
        self.back.raise_()
        self.registrationButton.raise_()
        self.error_label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Регистрация"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.label_2.setText(_translate("Form", "Имя малыша"))
        self.label_4.setText(_translate("Form", "Логин"))
        self.label_5.setText(_translate("Form", "Пароль"))
        self.label_6.setText(_translate("Form", "Повторите пароль"))
        self.back.setText(_translate("Form", "Назад"))
        self.registrationButton.setText(_translate("Form", "Зарегистрироваться"))


class Ui_MainWindow(object):
    """ Класс дизайна главного виджета """

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setFixedSize(740, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu1 = QtWidgets.QLabel(self.centralwidget)
        self.menu1.setGeometry(QtCore.QRect(0, 0, 41, 601))
        self.menu1.setStyleSheet("background-color: rgb(242, 147, 39);")
        self.menu1.setText("")
        self.menu1.setObjectName("menu1")
        self.klyaksa = QtWidgets.QLabel(self.centralwidget)
        self.klyaksa.setGeometry(QtCore.QRect(570, -50, 251, 301))
        self.klyaksa.setPixmap(QtGui.QPixmap("data/images/imgonline-com-ua-Resize-ebA6UoTlji.png"))
        self.label_smart_kid = QtWidgets.QLabel(self.centralwidget)
        self.label_smart_kid.setGeometry(QtCore.QRect(210, 270, 400, 50))
        self.label_smart_kid.setPixmap(QtGui.QPixmap("data/images/img_fonts.png"))
        self.label_smart_kid2 = QtWidgets.QLabel(self.centralwidget)
        self.label_smart_kid2.setGeometry(QtCore.QRect(330, 270, 400, 50))
        self.label_smart_kid2.setPixmap(QtGui.QPixmap("data/images/img_fonts.png"))
        self.label_smart_kid2.hide()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 41, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("background-color: rgb(242, 147, 39);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/images/Безымянный23.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(500, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_jpg_smart_kid = QtWidgets.QLabel(self.centralwidget)
        self.label_jpg_smart_kid.setGeometry(QtCore.QRect(570, 570, 171, 21))
        self.label_jpg_smart_kid.setText("")
        self.label_jpg_smart_kid.setPixmap(QtGui.QPixmap("data/images/imgonline-com-ua-Resize-bGWPEjq7aj16k.jpg"))
        self.label_jpg_smart_kid.setObjectName("label_2")
        self.label_jpg_smart_kid.hide()
        self.menu2 = QtWidgets.QLabel(self.centralwidget)
        self.menu2.setGeometry(QtCore.QRect(0, 0, 281, 611))
        self.menu2.setStyleSheet("background-color: rgb(242, 147, 39);")
        self.menu2.setText("")
        self.menu2.setObjectName("menu2")
        self.cross = QtWidgets.QPushButton(self.centralwidget)
        self.cross.setGeometry(QtCore.QRect(260, 0, 21, 21))
        self.cross.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(242, 147, 39);\n"
                                 "font: 14pt \"MS Shell Dlg 2\";\n"
                                 "")
        self.cross.setObjectName("cross")
        self.profileButton = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton.setGeometry(QtCore.QRect(60, 50, 161, 51))
        self.profileButton.setStyleSheet("color: rgb(242, 147, 39);\n"
                                         "font: 75 22pt \"PF Cosmonut Pro\";")
        self.profileButton.setObjectName("profileButton")
        self.alphabetButton = QtWidgets.QPushButton(self.centralwidget)
        self.alphabetButton.setGeometry(QtCore.QRect(60, 160, 161, 51))
        self.alphabetButton.setStyleSheet("color: rgb(242, 147, 39);\n"
                                          "font: 75 22pt \"PF Cosmonut Pro\";")
        self.alphabetButton.setObjectName("alphabetButton")
        self.animalsButton = QtWidgets.QPushButton(self.centralwidget)
        self.animalsButton.setGeometry(QtCore.QRect(60, 270, 161, 51))
        self.animalsButton.setStyleSheet("color: rgb(242, 147, 39);\n"
                                         "font: 75 22pt \"PF Cosmonut Pro\";")
        self.animalsButton.setObjectName("animalsButton")
        self.digitsButton = QtWidgets.QPushButton(self.centralwidget)
        self.digitsButton.setGeometry(QtCore.QRect(60, 380, 161, 51))
        self.digitsButton.setStyleSheet("color: rgb(242, 147, 39);\n"
                                        "font: 75 22pt \"PF Cosmonut Pro\";")
        self.digitsButton.setObjectName("digitssButton")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(60, 490, 161, 51))
        self.settingsButton.setStyleSheet("color: rgb(242, 147, 39);\n"
                                          "font: 75 22pt \"PF Cosmonut Pro\";")
        self.settingsButton.setObjectName("settingsButton")

        # Это дизайн окна, открывающегося при нажатии на кнопку 'Профиль'
        self.profileWidget = QtWidgets.QWidget(self.centralwidget)
        self.profileWidget.setGeometry(QtCore.QRect(50, 30, 611, 531))
        self.profileWidget.setObjectName("profileWidget")
        self.genderBox = QtWidgets.QComboBox(self.profileWidget)
        self.genderBox.setGeometry(QtCore.QRect(100, 200, 111, 31))
        self.genderBox.setStyleSheet("color: rgb(242, 147, 39);\n"
                                     "font: 75 18pt \"PF Cosmonut Pro\";\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(242, 147, 39);")
        self.genderBox.setObjectName("genderBox")
        self.genderBox.addItem("")
        self.genderBox.addItem("")
        self.avatarLabel = QtWidgets.QLabel(self.profileWidget)
        self.avatarLabel.setGeometry(QtCore.QRect(90, 40, 141, 131))
        self.avatarLabel.setText("")
        self.avatarLabel.setPixmap(QtGui.QPixmap("data/images/boy.png"))
        self.avatarLabel.setObjectName("avatarLabel")
        self.nameLabel = QtWidgets.QLabel(self.profileWidget)
        self.nameLabel.setGeometry(QtCore.QRect(270, 80, 291, 61))
        self.nameLabel.setStyleSheet("color: rgb(242, 147, 39);\n"
                                     "font: 75 35pt \"PF Cosmonut Pro\";")
        self.nameLabel.setObjectName("nameLabel")
        self.label = QtWidgets.QLabel(self.profileWidget)
        self.label.setGeometry(QtCore.QRect(230, 260, 171, 31))
        self.label.setStyleSheet("color: rgb(242, 147, 39);\n"
                                 "font: 75 22pt \"PF Cosmonut Pro\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.profileWidget)
        self.label_2.setGeometry(QtCore.QRect(50, 330, 200, 16))
        self.label_2.setStyleSheet("color: rgb(242, 147, 39);\n"
                                   "font: 75 16pt \"PF Cosmonut Pro\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.profileWidget)
        self.label_3.setGeometry(QtCore.QRect(50, 370, 200, 16))
        self.label_3.setStyleSheet("color: rgb(242, 147, 39);\n"
                                   "font: 75 16pt \"PF Cosmonut Pro\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.profileWidget)
        self.label_4.setGeometry(QtCore.QRect(50, 410, 200, 16))
        self.label_4.setStyleSheet("color: rgb(242, 147, 39);\n"
                                   "font: 75 16pt \"PF Cosmonut Pro\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.profileWidget)
        self.label_5.setGeometry(QtCore.QRect(50, 450, 200, 16))
        self.label_5.setStyleSheet("color: rgb(242, 147, 39);\n"
                                   "font: 75 16pt \"PF Cosmonut Pro\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.profileWidget)
        self.label_6.setGeometry(QtCore.QRect(350, 330, 500, 16))
        self.label_6.setStyleSheet("color: rgb(242, 147, 39);\n"
                                   "font: 75 16pt \"PF Cosmonut Pro\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.profileWidget)
        self.label_7.setGeometry(QtCore.QRect(350, 370, 500, 16))
        self.label_7.setStyleSheet("color: rgb(242, 147, 39);\n"
                                   "font: 75 16pt \"PF Cosmonut Pro\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.profileWidget)
        self.label_8.setGeometry(QtCore.QRect(350, 410, 500, 16))
        self.label_8.setStyleSheet("color: rgb(242, 147, 39);\n"
                                   "font: 75 16pt \"PF Cosmonut Pro\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.profileWidget)
        self.label_9.setGeometry(QtCore.QRect(350, 450, 500, 16))
        self.label_9.setStyleSheet("color: rgb(242, 147, 39);\n"
                                   "font: 75 16pt \"PF Cosmonut Pro\";")
        self.label_9.setObjectName("label_9")

        # Это дизайн окна, открывающегося при нажатии на кнопку 'Алфавит'
        self.alphabetWidget = QtWidgets.QWidget(self.centralwidget)
        self.alphabetWidget.setGeometry(QtCore.QRect(100, 30, 611, 531))
        self.alphabetWidget.setObjectName("alphabetWidget")
        self.alphabetWidget.resize(611, 530)

        self.pushButton_1 = QtWidgets.QPushButton(self.alphabetWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(130, 120, 291, 91))
        self.pushButton_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 75 22pt \"PF Cosmonut Pro\";\n"
                                        "background-color: rgb(242, 147, 39);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.alphabetWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 260, 291, 91))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 75 22pt \"PF Cosmonut Pro\";\n"
                                        "background-color: rgb(242, 147, 39);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.alphabetWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 400, 291, 91))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 75 22pt \"PF Cosmonut Pro\";\n"
                                        "background-color: rgb(242, 147, 39);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.alphabetLabel = QtWidgets.QLabel(self.alphabetWidget)
        self.alphabetLabel.setGeometry(QtCore.QRect(200, 40, 181, 41))
        self.alphabetLabel.setStyleSheet("color: rgb(242, 147, 39);\n"
                                         "font: 75 35pt \"PF Cosmonut Pro\";")
        self.alphabetLabel.setObjectName("alphabetLabel")

        # Это дизайн игр 'Повторяй за мной!', 'Что это за буква?'
        self.alphabet_povtoray = QtWidgets.QWidget(self.centralwidget)
        self.alphabet_povtoray.setGeometry(QtCore.QRect(100, 30, 611, 550))
        self.alphabet_povtoray.setObjectName("alphabet_povtoray")
        self.alphabet_povtoray.resize(611, 530)
        self.aButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.aButton.setGeometry(QtCore.QRect(50, 60, 51, 41))
        self.aButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.aButton.setObjectName("aButton")
        self.label_name = QtWidgets.QLabel(self.alphabet_povtoray)
        self.label_name.setGeometry(QtCore.QRect(120, 0, 361, 51))
        self.label_name.setStyleSheet("color: rgb(242, 147, 39);\n"
                                      "font: 75 35pt \"PF Cosmonut Pro\";")
        self.label_name.setObjectName("label_name")
        self.bButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.bButton.setGeometry(QtCore.QRect(120, 60, 51, 41))
        self.bButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.bButton.setObjectName("bButton")
        self.vButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.vButton.setGeometry(QtCore.QRect(190, 60, 51, 41))
        self.vButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.vButton.setObjectName("vButton")
        self.gButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.gButton.setGeometry(QtCore.QRect(260, 60, 51, 41))
        self.gButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.gButton.setObjectName("gButton")
        self.dButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.dButton.setGeometry(QtCore.QRect(330, 60, 51, 41))
        self.dButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.dButton.setObjectName("dButton")
        self.eButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.eButton.setGeometry(QtCore.QRect(400, 60, 51, 41))
        self.eButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.eButton.setObjectName("eButton")
        self.yoButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.yoButton.setGeometry(QtCore.QRect(470, 60, 51, 41))
        self.yoButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                    "background-color: rgb(242, 147, 39);")
        self.yoButton.setObjectName("yoButton")
        self.jButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.jButton.setGeometry(QtCore.QRect(50, 120, 51, 41))
        self.jButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.jButton.setObjectName("jButton")
        self.zButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.zButton.setGeometry(QtCore.QRect(120, 120, 51, 41))
        self.zButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.zButton.setObjectName("zButton")
        self.iButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.iButton.setGeometry(QtCore.QRect(190, 120, 51, 41))
        self.iButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.iButton.setObjectName("iButton")
        self.ikrButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.ikrButton.setGeometry(QtCore.QRect(260, 120, 51, 41))
        self.ikrButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                     "background-color: rgb(242, 147, 39);")
        self.ikrButton.setObjectName("ikrButton")
        self.kButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.kButton.setGeometry(QtCore.QRect(330, 120, 51, 41))
        self.kButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.kButton.setObjectName("kButton")
        self.lButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.lButton.setGeometry(QtCore.QRect(400, 120, 51, 41))
        self.lButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.lButton.setObjectName("lButton")
        self.mButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.mButton.setGeometry(QtCore.QRect(470, 120, 51, 41))
        self.mButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.mButton.setObjectName("mButton")
        self.nButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.nButton.setGeometry(QtCore.QRect(50, 180, 51, 41))
        self.nButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.nButton.setObjectName("nButton")
        self.oButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.oButton.setGeometry(QtCore.QRect(120, 180, 51, 41))
        self.oButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.oButton.setObjectName("oButton")
        self.pButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.pButton.setGeometry(QtCore.QRect(190, 180, 51, 41))
        self.pButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.pButton.setObjectName("pButton")
        self.rButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.rButton.setGeometry(QtCore.QRect(260, 180, 51, 41))
        self.rButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.rButton.setObjectName("rButton")
        self.sButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.sButton.setGeometry(QtCore.QRect(330, 180, 51, 41))
        self.sButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.sButton.setObjectName("sButton")
        self.tButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.tButton.setGeometry(QtCore.QRect(400, 180, 51, 41))
        self.tButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.tButton.setObjectName("tButton")
        self.yButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.yButton.setGeometry(QtCore.QRect(470, 180, 51, 41))
        self.yButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.yButton.setObjectName("yButton")
        self.fButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.fButton.setGeometry(QtCore.QRect(50, 240, 51, 41))
        self.fButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.fButton.setObjectName("fButton")
        self.xButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.xButton.setGeometry(QtCore.QRect(120, 240, 51, 41))
        self.xButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                   "background-color: rgb(242, 147, 39);")
        self.xButton.setObjectName("xButton")
        self.tseButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.tseButton.setGeometry(QtCore.QRect(190, 240, 51, 41))
        self.tseButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                     "background-color: rgb(242, 147, 39);")
        self.tseButton.setObjectName("tseButton")
        self.chButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.chButton.setGeometry(QtCore.QRect(260, 240, 51, 41))
        self.chButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                    "background-color: rgb(242, 147, 39);")
        self.chButton.setObjectName("chButton")
        self.shButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.shButton.setGeometry(QtCore.QRect(330, 240, 51, 41))
        self.shButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                    "background-color: rgb(242, 147, 39);")
        self.shButton.setObjectName("shButton")
        self.shaButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.shaButton.setGeometry(QtCore.QRect(400, 240, 51, 41))
        self.shaButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                     "background-color: rgb(242, 147, 39);")
        self.shaButton.setObjectName("shaButton")
        self.tvButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.tvButton.setGeometry(QtCore.QRect(470, 240, 51, 41))
        self.tvButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                    "background-color: rgb(242, 147, 39);")
        self.tvButton.setObjectName("tvButton")
        self.yiButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.yiButton.setGeometry(QtCore.QRect(50, 300, 51, 41))
        self.yiButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                    "background-color: rgb(242, 147, 39);")
        self.yiButton.setObjectName("yiButton")
        self.myaButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.myaButton.setGeometry(QtCore.QRect(120, 300, 51, 41))
        self.myaButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                     "background-color: rgb(242, 147, 39);")
        self.myaButton.setObjectName("myaButton")
        self.eeButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.eeButton.setGeometry(QtCore.QRect(190, 300, 51, 41))
        self.eeButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                    "background-color: rgb(242, 147, 39);")
        self.eeButton.setObjectName("eeButton")
        self.jyButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.jyButton.setGeometry(QtCore.QRect(260, 300, 51, 41))
        self.jyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                    "background-color: rgb(242, 147, 39);")
        self.jyButton.setObjectName("jyButton")
        self.yaButton = QtWidgets.QPushButton(self.alphabet_povtoray)
        self.yaButton.setGeometry(QtCore.QRect(330, 300, 51, 41))
        self.yaButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 25pt \"PF Cosmonut Pro\";\n"
                                    "background-color: rgb(242, 147, 39);")
        self.yaButton.setObjectName("yaButton")
        self.letterLabel = QtWidgets.QLabel(self.alphabet_povtoray)
        self.letterLabel.setGeometry(QtCore.QRect(220, 350, 161, 191))
        self.letterLabel.setStyleSheet("color: rgb(242, 147, 39);\n"
                                       "font: 75 130pt \"PF Cosmonut Pro\";")
        self.letterLabel.setText("")
        self.letterLabel.setObjectName("letterLabel")

        # Это дизайн игры 'Восстанови порядок'
        self.alphabet_bykvi = QtWidgets.QWidget(self.centralwidget)
        self.alphabet_bykvi.setGeometry(QtCore.QRect(100, 30, 611, 550))
        self.alphabet_bykvi.setObjectName("alphabet_bykvi")
        self.alphabet_bykvi.resize(611, 530)
        self.label_name_three = QtWidgets.QLabel(self.alphabet_bykvi)
        self.label_name_three.setGeometry(QtCore.QRect(110, 0, 371, 61))
        self.label_name_three.setStyleSheet("color: rgb(242, 147, 39);\n"
                                            "font: 75 35pt \"PF Cosmonut Pro\";")
        self.label_name_three.setObjectName("label")
        self.label_letters_three = QtWidgets.QLabel(self.alphabet_bykvi)
        self.label_letters_three.setGeometry(QtCore.QRect(150, 190, 341, 161))
        self.label_letters_three.setStyleSheet("color: rgb(242, 147, 39);\n"
                                               "font: 75 130pt \"PF Cosmonut Pro\";")
        self.label_letters_three.setObjectName("label_2")

        # Это окно открывается при нажатии на кнопку 'Животные'
        self.animals_games_widget = QtWidgets.QWidget(self.centralwidget)
        self.animals_games_widget.setGeometry(QtCore.QRect(0, 0, 700, 550))
        self.animals_games_widget.setObjectName("animals_games_widget")
        self.animal_name_label = QtWidgets.QLabel(self.animals_games_widget)
        self.animal_name_label.setGeometry(QtCore.QRect(290, 60, 300, 40))
        self.animal_name_label.setStyleSheet("color: rgb(242, 147, 39);\n"
                                             "font: 75 35pt \"PF Cosmonut Pro\";")
        self.pushButton_animal_1 = QtWidgets.QPushButton(self.animals_games_widget)
        self.pushButton_animal_1.setGeometry(QtCore.QRect(240, 200, 291, 91))
        self.pushButton_animal_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "font: 75 22pt \"PF Cosmonut Pro\";\n"
                                               "background-color: rgb(242, 147, 39);")
        self.pushButton_animal_1.setObjectName("pushButton_animal_1")
        self.pushButton_animal_2 = QtWidgets.QPushButton(self.animals_games_widget)
        self.pushButton_animal_2.setGeometry(QtCore.QRect(240, 400, 291, 91))
        self.pushButton_animal_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "font: 75 22pt \"PF Cosmonut Pro\";\n"
                                               "background-color: rgb(242, 147, 39);")
        self.pushButton_animal_2.setObjectName("pushButton_animal_2")

        # Это дизайн игры 'Учим животных'
        self.animals_widget = QtWidgets.QWidget(self.centralwidget)
        self.animals_widget.setGeometry(QtCore.QRect(0, 0, 700, 550))
        self.animals_widget.setObjectName("animals_widget")
        self.animal_jpg = QtWidgets.QLabel(self.animals_widget)
        self.animal_jpg.setGeometry(QtCore.QRect(200, 70, 500, 470))
        self.animal_jpg.setText("")
        self.animal_jpg.setObjectName("animal_jpg")
        self.animal_name = QtWidgets.QLabel(self.animals_widget)
        self.animal_name.setGeometry(QtCore.QRect(280, 10, 200, 41))
        self.animal_name.setStyleSheet("color: rgb(242, 147, 39);\n"
                                       "font: 75 35pt \"PF Cosmonut Pro\";")
        self.animal_name.setText("")
        self.animal_name.setObjectName("animal_name")

        # Это дизайн игры 'Отгадай животное'
        self.animals_widget2 = QtWidgets.QWidget(self.centralwidget)
        self.animals_widget2.setGeometry(QtCore.QRect(0, 0, 700, 550))
        self.animals_widget2.setObjectName("animals_widget2")
        self.animal_jpg2 = QtWidgets.QLabel(self.animals_widget2)
        self.animal_jpg2.setGeometry(QtCore.QRect(200, 0, 500, 470))
        self.animal_jpg2.setText("")
        self.animal_jpg2.setObjectName("animal_jpg2")
        self.animal_button1 = QtWidgets.QPushButton(self.animals_widget2)
        self.animal_button1.setGeometry(QtCore.QRect(200, 500, 100, 40))
        self.animal_button1.setStyleSheet("font: 75 18pt \"PF Cosmonut Pro\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(242, 147, 39);")
        self.animal_button1.setObjectName("animal_button1")
        self.animal_button2 = QtWidgets.QPushButton(self.animals_widget2)
        self.animal_button2.setGeometry(QtCore.QRect(430, 500, 100, 40))
        self.animal_button2.setStyleSheet("font: 75 18pt \"PF Cosmonut Pro\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(242, 147, 39);")
        self.animal_button2.setObjectName("animal_button1")

        # Это окно открывается при нажатии на кнопку 'Цифры'
        self.numbers_games_widget = QtWidgets.QWidget(self.centralwidget)
        self.numbers_games_widget.setGeometry(QtCore.QRect(0, 0, 700, 550))
        self.numbers_games_widget.setObjectName("numbers_games_widget")
        self.number_name_label = QtWidgets.QLabel(self.numbers_games_widget)
        self.number_name_label.setGeometry(QtCore.QRect(320, 60, 300, 40))
        self.number_name_label.setStyleSheet("color: rgb(242, 147, 39);\n"
                                             "font: 75 35pt \"PF Cosmonut Pro\";")
        self.pushButton_number_1 = QtWidgets.QPushButton(self.numbers_games_widget)
        self.pushButton_number_1.setGeometry(QtCore.QRect(240, 200, 291, 91))
        self.pushButton_number_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "font: 75 22pt \"PF Cosmonut Pro\";\n"
                                               "background-color: rgb(242, 147, 39);")
        self.pushButton_number_1.setObjectName("pushButton_animal_1")
        self.pushButton_number_2 = QtWidgets.QPushButton(self.numbers_games_widget)
        self.pushButton_number_2.setGeometry(QtCore.QRect(240, 400, 291, 91))
        self.pushButton_number_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "font: 75 22pt \"PF Cosmonut Pro\";\n"
                                               "background-color: rgb(242, 147, 39);")
        self.pushButton_number_2.setObjectName("pushButton_animal_2")

        # Это дизайн игры 'Учим цифры'
        self.numbers_uchim = QtWidgets.QWidget(self.centralwidget)
        self.numbers_uchim.setGeometry(QtCore.QRect(40, 0, 700, 550))
        self.numbers_uchim.setObjectName("numbers_uchim")
        self.label_ychim_zifri = QtWidgets.QLabel(self.numbers_uchim)
        self.label_ychim_zifri.setGeometry(QtCore.QRect(240, 10, 211, 61))
        self.label_ychim_zifri.setStyleSheet("color: rgb(242, 147, 39);\n"
                                             "font: 75 35pt \"PF Cosmonut Pro\";")
        self.label_ychim_zifri.setObjectName("label_ychim_zifri")
        self.number0_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number0_button.setGeometry(QtCore.QRect(10, 110, 51, 51))
        self.number0_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number0_button.setObjectName("number0_button")
        self.number1_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number1_button.setGeometry(QtCore.QRect(75, 110, 51, 51))
        self.number1_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number1_button.setObjectName("number1_button")
        self.number2_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number2_button.setGeometry(QtCore.QRect(145, 110, 51, 51))
        self.number2_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number2_button.setObjectName("number2_button")
        self.number3_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number3_button.setGeometry(QtCore.QRect(215, 110, 51, 51))
        self.number3_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number3_button.setObjectName("number3_button")
        self.number4_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number4_button.setGeometry(QtCore.QRect(285, 110, 51, 51))
        self.number4_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number4_button.setObjectName("number4_button")
        self.number5_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number5_button.setGeometry(QtCore.QRect(355, 110, 51, 51))
        self.number5_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number5_button.setObjectName("number5_button")
        self.number6_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number6_button.setGeometry(QtCore.QRect(425, 110, 51, 51))
        self.number6_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number6_button.setObjectName("number6_button")
        self.number7_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number7_button.setGeometry(QtCore.QRect(495, 110, 51, 51))
        self.number7_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number7_button.setObjectName("number7_button")
        self.number8_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number8_button.setGeometry(QtCore.QRect(565, 110, 51, 51))
        self.number8_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number8_button.setObjectName("number8_button")
        self.number9_button = QtWidgets.QPushButton(self.numbers_uchim)
        self.number9_button.setGeometry(QtCore.QRect(630, 110, 51, 51))
        self.number9_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.number9_button.setObjectName("number9_button")
        self.label_number1 = QtWidgets.QLabel(self.numbers_uchim)
        self.label_number1.setGeometry(QtCore.QRect(290, 200, 131, 181))
        self.label_number1.setStyleSheet("color: rgb(242, 147, 39);\n"
                                         "font: 75 200pt \"PF Cosmonut Pro\";\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "")
        self.label_number1.setText("")
        self.label_number1.setObjectName("label_number1")
        self.label_name_of_number1 = QtWidgets.QLabel(self.numbers_uchim)
        self.label_name_of_number1.setGeometry(QtCore.QRect(290, 420, 141, 51))
        self.label_name_of_number1.setStyleSheet("color: rgb(242, 147, 39);\n"
                                                 "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                                 "background-color: rgb(255, 255, 255);\n"
                                                 "")
        self.label_name_of_number1.setText("")
        self.label_name_of_number1.setObjectName("label_name_of_number1")

        # Это дизайн игры 'Верно или нет?'
        self.numbers_verno = QtWidgets.QWidget(self.centralwidget)
        self.numbers_verno.setGeometry(QtCore.QRect(40, 0, 700, 550))
        self.numbers_verno.setObjectName("numbers_verno")
        self.label_verno = QtWidgets.QLabel(self.numbers_verno)
        self.label_verno.setGeometry(QtCore.QRect(200, 10, 399, 61))
        self.label_verno.setStyleSheet("color: rgb(242, 147, 39);\n"
                                       "font: 75 35pt \"PF Cosmonut Pro\";")
        self.label_verno.setObjectName("label_verno")
        self.verno_button = QtWidgets.QPushButton(self.numbers_verno)
        self.verno_button.setGeometry(QtCore.QRect(150, 450, 150, 51))
        self.verno_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                        "background-color: rgb(242, 147, 39);")
        self.verno_button.setObjectName("verno_button")
        self.neverno_button = QtWidgets.QPushButton(self.numbers_verno)
        self.neverno_button.setGeometry(QtCore.QRect(400, 450, 150, 51))
        self.neverno_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 35pt \"PF Cosmonut Pro\";\n"
                                          "background-color: rgb(242, 147, 39);")
        self.neverno_button.setObjectName("neverno_button")
        self.label_number_verno = QtWidgets.QLabel(self.numbers_verno)
        self.label_number_verno.setGeometry(QtCore.QRect(290, 200, 131, 181))
        self.label_number_verno.setStyleSheet("color: rgb(242, 147, 39);\n"
                                              "font: 75 200pt \"PF Cosmonut Pro\";\n"
                                              "background-color: rgb(255, 255, 255);\n"
                                              "")
        self.label_number_verno.setText("")
        self.label_number_verno.setObjectName("label_number_verno")

        # Это дизайн окна 'О программе'
        self.about_programm_widget = QtWidgets.QWidget(self.centralwidget)
        self.about_programm_widget.setGeometry(QtCore.QRect(40, 0, 700, 560))
        self.about_programm_widget.setObjectName("about_programm_widget")
        self.about_programm_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.about_programm_widget.setAutoFillBackground(False)
        self.about_programm_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.about_programm_widget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_about_programm = QtWidgets.QLabel(self.about_programm_widget)
        self.label_about_programm.setGeometry(QtCore.QRect(220, 20, 251, 41))
        self.label_about_programm.setStyleSheet("color: rgb(242, 147, 39);\n"
                                                "font: 75 35pt \"PF Cosmonut Pro\";")
        self.label_about_programm.setObjectName("label_about_programm")
        self.text_about_programm = QtWidgets.QPlainTextEdit(self.about_programm_widget)
        self.text_about_programm.setGeometry(QtCore.QRect(0, 80, 701, 131))
        self.text_about_programm.setStyleSheet("color: rgb(242, 147, 39);\n"
                                               "font: 75 17pt \"PF Cosmonut Pro\";\n"
                                               "border-color: rgb(0, 0, 0);\n"
                                               "selection-color: rgb(255, 255, 255);\n"
                                               "selection-background-color: rgb(242, 147, 39);")
        self.text_about_programm.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.text_about_programm.setReadOnly(True)
        self.text_about_programm.setObjectName("text_about_programm")
        self.istochniki_label = QtWidgets.QPlainTextEdit(self.about_programm_widget)
        self.istochniki_label.setGeometry(QtCore.QRect(0, 250, 701, 181))
        self.istochniki_label.setStyleSheet("color: rgb(242, 147, 39);\n"
                                            "font: 75 14pt \"PF Cosmonut Pro\";\n"
                                            "border-color: rgb(0, 0, 0);\n"
                                            "selection-color: rgb(255, 255, 255);\n"
                                            "selection-background-color: rgb(242, 147, 39);\n"
                                            "")
        self.istochniki_label.setReadOnly(True)
        self.istochniki_label.setObjectName("istochniki_label")
        self.delete_profile = QtWidgets.QPushButton(self.about_programm_widget)
        self.delete_profile.setGeometry(QtCore.QRect(140, 490, 191, 51))
        self.delete_profile.setStyleSheet("font: 75 18pt \"PF Cosmonut Pro\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(242, 147, 39);")
        self.delete_profile.setObjectName("delete_profile")
        self.exit_profile = QtWidgets.QPushButton(self.about_programm_widget)
        self.exit_profile.setGeometry(QtCore.QRect(360, 490, 191, 51))
        self.exit_profile.setStyleSheet("font: 75 18pt \"PF Cosmonut Pro\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(242, 147, 39);")
        self.exit_profile.setObjectName("exit_profile")

        self.retranslateUi(self.about_programm_widget)
        QtCore.QMetaObject.connectSlotsByName(self.about_programm_widget)

        self.profileWidget.raise_()
        self.alphabetWidget.raise_()
        self.menu2.raise_()
        self.menu1.raise_()
        self.label_jpg_smart_kid.raise_()
        self.cross.raise_()
        self.profileButton.raise_()
        self.alphabetButton.raise_()
        self.digitsButton.raise_()
        self.animalsButton.raise_()
        self.settingsButton.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart Kid"))
        self.cross.setText(_translate("MainWindow", "✖"))
        self.profileButton.setText(_translate("MainWindow", "ПРОФИЛЬ"))
        self.alphabetButton.setText(_translate("MainWindow", "АЛФАВИТ"))
        self.animalsButton.setText(_translate("MainWindow", "ЖИВОТНЫЕ"))
        self.digitsButton.setText(_translate("MainWindow", "ЦИФРЫ"))
        self.settingsButton.setText(_translate("MainWindow", "О ПРОГРАММЕ"))
        self.genderBox.setItemText(0, _translate("widget", " Мальчик"))
        self.genderBox.setItemText(1, _translate("widget", " Девочка"))
        self.nameLabel.setText(_translate("widget", ""))
        self.label.setText(_translate("widget", "Мой прогресс:"))
        self.label_2.setText(_translate("widget", "'Что это за буква?':"))
        self.label_3.setText(_translate("widget", "'Восстанови порядок':"))
        self.label_4.setText(_translate("widget", "'Отгадай животное':"))
        self.label_5.setText(_translate("widget", "'Верно или нет?':"))
        self.label_6.setText(_translate("widget", ""))
        self.label_7.setText(_translate("widget", ""))
        self.label_8.setText(_translate("widget", ""))
        self.label_9.setText(_translate("widget", ""))
        self.pushButton_1.setText(_translate("alphabetWidget", "Повторяй за мной!"))
        self.pushButton_2.setText(_translate("alphabetWidget", "Что это за буква?"))
        self.pushButton_4.setText(_translate("alphabetWidget", "Восстанови порядок"))
        self.alphabetLabel.setText(_translate("alphabetWidget", "Алфавит"))
        self.aButton.setText(_translate("alphabet_povtoray", "А"))
        self.bButton.setText(_translate("alphabet_povtoray", "Б"))
        self.vButton.setText(_translate("alphabet_povtoray", "В"))
        self.gButton.setText(_translate("alphabet_povtoray", "Г"))
        self.dButton.setText(_translate("alphabet_povtoray", "Д"))
        self.eButton.setText(_translate("alphabet_povtoray", "Е"))
        self.yoButton.setText(_translate("alphabet_povtoray", "Ё"))
        self.jButton.setText(_translate("alphabet_povtoray", "Ж"))
        self.zButton.setText(_translate("alphabet_povtoray", "З"))
        self.iButton.setText(_translate("alphabet_povtoray", "И"))
        self.ikrButton.setText(_translate("alphabet_povtoray", "Й"))
        self.kButton.setText(_translate("alphabet_povtoray", "К"))
        self.lButton.setText(_translate("alphabet_povtoray", "Л"))
        self.mButton.setText(_translate("alphabet_povtoray", "М"))
        self.nButton.setText(_translate("alphabet_povtoray", "Н"))
        self.oButton.setText(_translate("alphabet_povtoray", "О"))
        self.pButton.setText(_translate("alphabet_povtoray", "П"))
        self.rButton.setText(_translate("alphabet_povtoray", "Р"))
        self.sButton.setText(_translate("alphabet_povtoray", "С"))
        self.tButton.setText(_translate("alphabet_povtoray", "Т"))
        self.yButton.setText(_translate("alphabet_povtoray", "У"))
        self.fButton.setText(_translate("alphabet_povtoray", "Ф"))
        self.xButton.setText(_translate("alphabet_povtoray", "Х"))
        self.tseButton.setText(_translate("alphabet_povtoray", "Ц"))
        self.chButton.setText(_translate("alphabet_povtoray", "Ч"))
        self.shButton.setText(_translate("alphabet_povtoray", "Ш"))
        self.shaButton.setText(_translate("alphabet_povtoray", "Щ"))
        self.tvButton.setText(_translate("alphabet_povtoray", "Ъ"))
        self.yiButton.setText(_translate("alphabet_povtoray", "Ы"))
        self.myaButton.setText(_translate("alphabet_povtoray", "Ь"))
        self.eeButton.setText(_translate("alphabet_povtoray", "Э"))
        self.jyButton.setText(_translate("alphabet_povtoray", "Ю"))
        self.yaButton.setText(_translate("alphabet_povtoray", "Я"))
        self.animal_name_label.setText(_translate("animals_games_widget", "Животные"))
        self.pushButton_animal_1.setText(_translate("animals_games_widget", "Учим животных"))
        self.pushButton_animal_2.setText(_translate("animals_games_widget", "Отгадай животное"))
        self.label_name_three.setText(_translate("alphabet_bykvi", "Восстанови порядок"))
        self.label_letters_three.setText(_translate("alphabet_bykvi", ""))
        self.number_name_label.setText(_translate("numbers_games_widget", "Цифры"))
        self.pushButton_number_1.setText(_translate("numbers__games_widget", "Учим цифры"))
        self.pushButton_number_2.setText(_translate("numbers__games_widget", "Верно или нет?"))
        self.label_ychim_zifri.setText(_translate("numbers_uchim", "Учим цифры"))
        self.number1_button.setText(_translate("numbers_uchim", "0"))
        self.number1_button.setText(_translate("numbers_uchim", "1"))
        self.number2_button.setText(_translate("numbers_uchim", "2"))
        self.number3_button.setText(_translate("numbers_uchim", "3"))
        self.number4_button.setText(_translate("numbers_uchim", "4"))
        self.number5_button.setText(_translate("numbers_uchim", "5"))
        self.number6_button.setText(_translate("numbers_uchim", "6"))
        self.number7_button.setText(_translate("numbers_uchim", "7"))
        self.number8_button.setText(_translate("numbers_uchim", "8"))
        self.number9_button.setText(_translate("numbers_uchim", "9"))
        self.number0_button.setText(_translate("numbers_uchim", "0"))
        self.label_verno.setText(_translate("numbers_verno", "Верно или нет?"))
        self.neverno_button.setText(_translate("numbers_verno", "НЕТ"))
        self.verno_button.setText(_translate("numbers_verno", "ДА"))
        self.label_about_programm.setText(_translate("about_programm_widget", "О программе"))
        self.text_about_programm.setPlainText(_translate("about_programm_widget",
                                                         "Smart Kid — это обучающее приложение для детей "
                                                         "дошкольного возраста, которое поможет вашему ребёнку "
                                                         "самостоятельно выучить алфавит, освоить счет и "
                                                         "проведёт знакомство с новыми животными. "
                                                         "Свои идеи по развитию приложения присылайте на "
                                                         "почту vitaliya2604@yandex.ru"))
        self.istochniki_label.setPlainText(
            _translate("about_programm_widget", "Озвучка предложений - сервис Yandex SpeechKit\n"
                                                "\n"
                                                "Озвучка алфавита — zvukipro.com\n"
                                                "\n"
                                                "Картинки животных — stranamam.ru\n"
                                                "\n"
                                                "Логотип Smart Kid — fonts-online.ru"))
        self.delete_profile.setText(_translate("about_programm_widget", "Удалить профиль"))
        self.exit_profile.setText(_translate("about_programm_widget", "Выйти из аккаунта"))
