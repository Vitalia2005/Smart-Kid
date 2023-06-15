# -*- coding: utf-8 -*-
import random
import sys, sqlite3

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from дизайны import Ui_welcomeForm, Ui_inputForm, Ui_regForm, Ui_MainWindow
from PyQt5 import QtGui


class WelcomeWidget(QWidget, Ui_welcomeForm):
    """ Класс первого (приветственного) окна с кнопками вход и регистрация """

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        self.initUI(args)

    def initUI(self, args):
        self.setFixedSize(640, 480)  # Фиксируем размер
        sound = QSound("data/sounds/привет.wav", self)
        sound.play()
        self.inputButton.clicked.connect(self.inp)
        self.registrationButton.clicked.connect(self.registration)

    def inp(self):  # Функция кнопки войти
        self.form = InputWidget(self, [])  # Открываем виджет входа
        self.form.show()
        self.hide()  # Прячем приветственный виджет

    def registration(self):  # функция кнопки регистрации
        self.form_reg = RegistrationWidget(self, [])  # Открываем виджет регистрации
        self.form_reg.show()
        self.hide()  # Прячем приветственный виджет


class InputWidget(QWidget, Ui_inputForm):
    """ Класс виджета входа """

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        self.initUI(args)

    def initUI(self, args):
        self.setFixedSize(640, 480)  # Фиксируем размер виджета
        self.back.clicked.connect(self.back_to_welocome)
        self.inputButton.clicked.connect(self.inp)

    def back_to_welocome(self):  # Функция кнопки назад
        form.show()
        self.hide()

    def inp(self):  # Функция нажатия на кнопку войти
        self.login = self.login_label.toPlainText()
        self.password = self.password_label.text()
        if not check_login_in_db(self.login):
            self.error.setText('Пользователя с таким логином не зарегистрировано.')
        else:
            result = cur.execute("""SELECT password FROM users WHERE login = ?""", (self.login,)).fetchall()
            if result[0][0] != self.password:
                self.error.setText('                          Неверный пароль.')
            else:
                self.back_form_welc = MainWindow(self, [], login=self.login)  # Открываем главный виджет
                self.back_form_welc.show()
                self.hide()


class RegistrationWidget(QWidget, Ui_regForm):
    """ Класс виджета регистрации """

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        self.initUI(args)

    def initUI(self, args):
        self.setFixedSize(640, 480)  # Фиксируем размер виджета
        self.back.clicked.connect(self.back_to_welocome)
        self.registrationButton.clicked.connect(self.registration)

    def back_to_welocome(self):  # Функция кнопки назад
        form.show()
        self.hide()

    def registration(self):
        self.error_label.setStyleSheet("color: rgb(255, 0, 0);")
        errors = []  # Список ошибок

        self.name = self.name_text.toPlainText().capitalize()  # Вводим имя и проверяем его
        e = '                           Имя введено некорректно.'
        if not self.name.isalpha() or len(self.name) < 2:
            # Если имя состоит не только из букв или оно короче 2 символов,
            # то добавим ошибку в список с ошибками
            errors.append(e)

        self.login = self.login_text.toPlainText()  # Вводим логин и проверяем его
        e = '                            Этот логин уже занят.'
        if check_login_in_db(self.login):
            errors.append(e)
        e = '                           Слишком короткий логин.'
        if len(self.login) <= 3:
            errors.append(e)

        self.password = self.password_text.text()  # Проверяем первый пароль
        k = check_password(self.password)
        if k != 'ok':
            errors.append(k)

        self.password2 = self.password2_text.text()

        # Провряем, чтобы второй пароль совпадал с первым
        if self.password2 != self.password:
            errors.append('                                Пароли не совпадают.')

        # Вывод ошибок в поле
        if errors:
            self.error_label.setText(errors[0])
        else:
            self.error_label.setText('')
            cur.execute("""INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (self.login, self.password, self.name, 1, 0, 0, 0, 0, 0, 0, 0, 0)).fetchall()
            con.commit()
            self.error_label.setStyleSheet("color: rgb(0, 170, 0)")
            self.error_label.setText(f'Пользователь с логином {self.login} успешно зарегистрирован.')


class MainWindow(QMainWindow, Ui_MainWindow):
    """ Класс главного окна """

    def __init__(self, *args, login):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        self.login = login
        self.name = cur.execute("""SELECT name FROM users WHERE login = ?""",
                                (self.login,)).fetchall()[0][0]
        self.playing = False
        self.initUI(args)

    def initUI(self, args):
        self.menu2.hide()
        self.close_all()
        self.cross.hide()
        self.profileButton.hide()
        self.alphabetButton.hide()
        self.digitsButton.hide()
        self.animalsButton.hide()
        self.settingsButton.hide()
        self.pushButton.clicked.connect(self.open_menu)  # Нажали на кнопку открытия меню
        self.cross.clicked.connect(self.close_menu)  # Нажали на крестик (в меню)
        self.profileButton.clicked.connect(self.profile_open)  # Нажали на кнопку 'профиль' в меню
        self.genderBox.currentIndexChanged.connect(self.on_combobox_func)  # Изменили пол в comboBox
        self.alphabetButton.clicked.connect(self.open_alphabet_games)  # Кнопка 'Алфавит'
        self.animalsButton.clicked.connect(self.open_animals_games)  # Кнопка 'Животные'
        self.settingsButton.clicked.connect(self.open_about_programm)  # Кнопка 'О программе'
        self.pushButton_1.clicked.connect(self.open_povtoray_alphabet)  # Игра 'Повторяй за мной'(алфавит)
        self.pushButton_2.clicked.connect(self.open_chto_alphabet)  # Игра 'Что это за буква?'(алфавит)
        self.pushButton_4.clicked.connect(self.open_bykvi_alphabet)  # Игра 'Восстанови порядок'(алфавит)
        self.delete_profile.clicked.connect(self.delete_pr)  # Кнопка 'Удалить профиль'
        self.exit_profile.clicked.connect(self.exit_pr)  # Кнопка 'Выйти из аккаунта'
        self.pushButton_animal_1.clicked.connect(self.open_animal_1)  # Кнопка 'Учим животных'
        self.pushButton_animal_2.clicked.connect(self.open_animal_2)  # Кнопка 'Отгадай животное'
        self.animal_button1.clicked.connect(self.btn_animal_1)  # Кнопка ответа № 1 в игре 'Отгадай животное'
        self.animal_button2.clicked.connect(self.btn_animal_2)  # Кнопка ответа № 2 в игре 'Отгадай животное'
        self.animal_button1.installEventFilter(self)  # Устнавливаем обработчик курсора для варианта ответа 1
        self.animal_button2.installEventFilter(self)  # Устнавливаем обработчик курсора для варианта ответа 2
        self.digitsButton.clicked.connect(self.open_digits_games)  # Кнопка 'Цифры'
        self.pushButton_number_1.clicked.connect(self.open_ychim_zifri)  # Кнопка игры 'Учим цифры'
        self.pushButton_number_2.clicked.connect(self.open_verno_ili_net)  # Кнопка игры 'Верно или нет?'
        self.verno_button.clicked.connect(self.verno_b)  # Кнопка ДА игры 'Верно или нет?'
        self.neverno_button.clicked.connect(self.neverno_b)  # Кнопка НЕТ игры 'Верно или нет?'
        self.verno_button.installEventFilter(self)  # Устнавливаем обработчик курсора для варианта ответа ДА
        self.neverno_button.installEventFilter(self)  # Устнавливаем обработчик курсора для варианта ответа НЕТ

        # Кнопки букв в играх 'Повторяй за мной', 'Что это за буква?'(алфавит)
        self.aButton.clicked.connect(self.buttons_of_alphabet_games('а'))
        self.bButton.clicked.connect(self.buttons_of_alphabet_games('б'))
        self.vButton.clicked.connect(self.buttons_of_alphabet_games('в'))
        self.gButton.clicked.connect(self.buttons_of_alphabet_games('г'))
        self.dButton.clicked.connect(self.buttons_of_alphabet_games('д'))
        self.eButton.clicked.connect(self.buttons_of_alphabet_games('е'))
        self.yoButton.clicked.connect(self.buttons_of_alphabet_games('ё'))
        self.jButton.clicked.connect(self.buttons_of_alphabet_games('ж'))
        self.zButton.clicked.connect(self.buttons_of_alphabet_games('з'))
        self.iButton.clicked.connect(self.buttons_of_alphabet_games('и'))
        self.ikrButton.clicked.connect(self.buttons_of_alphabet_games('й'))
        self.kButton.clicked.connect(self.buttons_of_alphabet_games('к'))
        self.lButton.clicked.connect(self.buttons_of_alphabet_games('л'))
        self.mButton.clicked.connect(self.buttons_of_alphabet_games('м'))
        self.nButton.clicked.connect(self.buttons_of_alphabet_games('н'))
        self.oButton.clicked.connect(self.buttons_of_alphabet_games('о'))
        self.pButton.clicked.connect(self.buttons_of_alphabet_games('п'))
        self.rButton.clicked.connect(self.buttons_of_alphabet_games('р'))
        self.sButton.clicked.connect(self.buttons_of_alphabet_games('с'))
        self.tButton.clicked.connect(self.buttons_of_alphabet_games('т'))
        self.yButton.clicked.connect(self.buttons_of_alphabet_games('у'))
        self.fButton.clicked.connect(self.buttons_of_alphabet_games('ф'))
        self.xButton.clicked.connect(self.buttons_of_alphabet_games('х'))
        self.tseButton.clicked.connect(self.buttons_of_alphabet_games('ц'))
        self.chButton.clicked.connect(self.buttons_of_alphabet_games('ч'))
        self.shButton.clicked.connect(self.buttons_of_alphabet_games('ш'))
        self.shaButton.clicked.connect(self.buttons_of_alphabet_games('щ'))
        self.tvButton.clicked.connect(self.buttons_of_alphabet_games('ъ'))
        self.yiButton.clicked.connect(self.buttons_of_alphabet_games('ы'))
        self.myaButton.clicked.connect(self.buttons_of_alphabet_games('ь'))
        self.eeButton.clicked.connect(self.buttons_of_alphabet_games('э'))
        self.jyButton.clicked.connect(self.buttons_of_alphabet_games('ю'))
        self.yaButton.clicked.connect(self.buttons_of_alphabet_games('я'))

        # Кнопки-цифры в игре 'Учим цифры'
        self.number0_button.clicked.connect(self.buttons_of_numbers('0'))
        self.number1_button.clicked.connect(self.buttons_of_numbers('1'))
        self.number2_button.clicked.connect(self.buttons_of_numbers('2'))
        self.number3_button.clicked.connect(self.buttons_of_numbers('3'))
        self.number4_button.clicked.connect(self.buttons_of_numbers('4'))
        self.number5_button.clicked.connect(self.buttons_of_numbers('5'))
        self.number6_button.clicked.connect(self.buttons_of_numbers('6'))
        self.number7_button.clicked.connect(self.buttons_of_numbers('7'))
        self.number8_button.clicked.connect(self.buttons_of_numbers('8'))
        self.number9_button.clicked.connect(self.buttons_of_numbers('9'))

    def close_all(self):  # Функция закрытия всех вкладок из меню (профиль, алфавит и т.д.)
        self.profileWidget.hide()
        self.alphabetWidget.hide()
        self.alphabet_povtoray.hide()
        self.animals_widget.hide()
        self.animals_widget2.hide()
        self.alphabet_bykvi.hide()
        self.about_programm_widget.hide()
        self.animals_games_widget.hide()
        self.numbers_games_widget.hide()
        self.numbers_uchim.hide()
        self.numbers_verno.hide()

    def open_menu(self):  # Функия открытия меню
        self.pushButton.hide()
        self.close_all()
        self.menu2.show()
        self.cross.show()
        self.klyaksa.show()
        self.label_smart_kid2.show()
        self.animals_games_widget.hide()
        self.label_jpg_smart_kid.hide()
        self.label_smart_kid.hide()
        self.profileButton.show()
        self.alphabetButton.show()
        self.digitsButton.show()
        self.animalsButton.show()
        self.settingsButton.show()

    def close_menu(self):  # Функция закрытия меню
        self.menu2.hide()
        self.cross.hide()
        self.profileButton.hide()
        self.alphabetButton.hide()
        self.label_smart_kid2.hide()
        self.label_jpg_smart_kid.hide()
        self.label_smart_kid.show()
        self.klyaksa.show()
        self.digitsButton.hide()
        self.animalsButton.hide()
        self.settingsButton.hide()
        self.pushButton.show()

    def open_alphabet_games(self):  # Функция кнопки 'Алфавит'
        self.close_all()
        self.alphabetWidget.show()
        self.close_menu()
        self.label_jpg_smart_kid.show()
        self.label_smart_kid.hide()
        self.klyaksa.hide()

    def open_animals_games(self):  # Функция кнопки 'Животные'
        self.close_all()
        self.animals_games_widget.show()
        self.close_menu()
        self.label_smart_kid.hide()
        self.klyaksa.hide()
        self.label_jpg_smart_kid.show()

    def open_about_programm(self):  # Функция кнопки 'О программе'
        self.close_all()
        self.about_programm_widget.show()
        self.close_menu()
        self.label_jpg_smart_kid.show()
        self.klyaksa.hide()

    def open_digits_games(self):  # Функция кнопки 'Цифры'
        self.close_all()
        self.numbers_games_widget.show()
        self.close_menu()
        self.label_jpg_smart_kid.show()
        self.klyaksa.hide()

    def profile_open(self):  # Функция кнопки 'Профиль'
        self.close_all()
        self.close_menu()
        self.label_jpg_smart_kid.show()
        self.klyaksa.hide()
        self.profileWidget.show()
        self.nameLabel.setText(self.name)
        self.true_chto_eto_za_bykva = cur.execute("""
                SELECT true_chto_eto_za_bykva FROM users WHERE login = ?""", (self.login,)).fetchall()[0][0]
        self.false_chto_eto_za_bykva = cur.execute("""
                SELECT false_chto_eto_za_bykva FROM users WHERE login = ?""", (self.login,)).fetchall()[0][0]
        self.label_6.setText(str(self.true_chto_eto_za_bykva) + ' правильных, ' +
                             str(self.false_chto_eto_za_bykva) + ' неправильных')
        self.true_bykvi_v_alphabete = cur.execute("""
                        SELECT true_bykvi_v_alphabete FROM users WHERE login = ?""", (self.login,)).fetchall()[0][0]
        self.false_bykvi_v_alphabete = cur.execute("""
                        SELECT false_bykvi_v_alphabete FROM users WHERE login = ?""", (self.login,)).fetchall()[0][0]
        self.label_7.setText(str(self.true_bykvi_v_alphabete) + ' правильных, ' +
                             str(self.false_bykvi_v_alphabete) + ' неправильных')
        self.true_animals = cur.execute("""
                            SELECT true_animals FROM users WHERE login = ?""", (self.login,)).fetchall()[0][0]
        self.false_animals = cur.execute("""
                            SELECT false_animals FROM users WHERE login = ?""", (self.login,)).fetchall()[0][0]
        self.label_8.setText(str(self.true_animals) + ' правильных, ' +
                             str(self.false_animals) + ' неправильных')
        self.true_numbers = cur.execute("""
                            SELECT true_numbers FROM users WHERE login = ?""", (self.login,)).fetchall()[0][0]
        self.false_numbers = cur.execute("""
                            SELECT false_numbers FROM users WHERE login = ?""", (self.login,)).fetchall()[0][0]
        self.label_9.setText(str(self.true_numbers) + ' правильных, ' +
                             str(self.false_numbers) + ' неправильных')
        self.genderBox.setCurrentIndex(cur.execute("""SELECT gender FROM users WHERE login = ?""",
                                                   (self.login,)).fetchall()[0][0])

    def open_bykvi_alphabet(self):  # Открыть игру 'Восстанови порядок'(алфавит)
        self.close_all()
        self.play_sound("data/sounds/буквы_в_алфавите")
        self.alphabet_bykvi.show()
        self.let = random.choice([alphabet[i:i + 3] for i in range(31)])
        self.label_letters_three.setText(self.let.upper()[0] + '?' + self.let.upper()[2])

    def open_povtoray_alphabet(self):  # Открыть игру 'Повторяй за мной!'
        self.close_all()
        self.play_sound("data/sounds/повторяй")
        self.alphabet_povtoray.show()
        self.label_name.setText('Повторяй за мной!')

    def open_chto_alphabet(self):  # Открыть игру 'Что это за буква?'
        self.close_all()
        self.play_sound('data/sounds/что_за_буква')
        self.flag = False
        self.alphabet_povtoray.show()
        self.letterLabel.setText('')
        self.label_name.setText('Что это за буква?')

    def open_animal_1(self):  # Открыть игру 'Учим животных'
        self.animals_widget.show()
        self.play_sound("data/sounds/животные")
        self.close_menu()
        self.label_jpg_smart_kid.show()
        self.klyaksa.hide()
        self.animal_name.setText('')
        self.animal_jpg.setPixmap(QtGui.QPixmap())

    def open_animal_2(self):  # Открыть игру 'Отгадай животное'
        self.animals_widget2.show()
        self.play_sound('data/sounds/что_это_за_животное')
        self.close_menu()
        self.label_jpg_smart_kid.show()
        self.klyaksa.hide()
        self.random_animals_button()

    def open_ychim_zifri(self):  # Открыть игру 'Учим цифры'
        self.play_sound('data/sounds/нажми_на_цифру')
        self.close_menu()
        self.numbers_uchim.show()
        self.label_jpg_smart_kid.show()
        self.klyaksa.hide()

    def open_verno_ili_net(self):  # Открыть игру 'Верно или нет?'
        self.close_menu()
        self.klyaksa.hide()
        self.numbers_verno.show()
        self.label_jpg_smart_kid.show()
        self.random_digit()

    # Функция создания случайных кнопок (чтобы правильный ответ был не всегда в одной кнопке)
    def random_animals_button(self):
        self.als = random.sample(animals_data, 2)
        self.ind = random.choice([1, 2])
        self.an = self.als[0].capitalize()
        self.animal_jpg2.setPixmap(QtGui.QPixmap('data/animals/' + self.an.lower() + '.jpg'))
        if self.ind == 1:
            self.animal_button1.setText(self.an)
            self.animal_button2.setText(self.als[1].capitalize())
        else:
            self.animal_button2.setText(self.an)
            self.animal_button1.setText(self.als[1].capitalize())

    def random_digit(self):  # Функия случайного отображения и озвучивания цифр в игре "Верно или нет?"
        self.data = random.sample(list(numbers), 2) # Выбираем два случайных числа
        self.d = self.data[0]
        self.ind1 = random.choice([0, 1])  # Выбираем индекс числа, которое отобразится на экране
        self.ind2 = random.choice([0, 1])  # Выбираем индекс числа, которое озвучится
        self.label_number_verno.setText(str(self.data[self.ind1]))
        self.play_sound('data/digits/' + str(self.data[self.ind2]))

    def verno_b(self):  # Нажали на кнопку 'ДА' в игре "Верно или нет?"
        if self.ind1 != self.ind2:  # Если закадровый голос говорил не ту цифру, что изображена на экране
            self.play_sound("data/sounds/неправильно")
            cur.execute(
                """UPDATE users SET false_numbers = false_numbers + 1 WHERE login = ?""", (self.login,))
            con.commit()
        else:
            cur.execute(
                """UPDATE users SET true_numbers = true_numbers + 1 WHERE login = ?""", (self.login,))
            con.commit()
            self.random_digit()

    def neverno_b(self):  # Нажали на кнопку 'НЕТ' в игре "Верно или нет?"
        if self.ind1 == self.ind2:  # Если закадровый голос говорил ту же цифру, что и изображена
            self.play_sound("data/sounds/неправильно")
            cur.execute(
                """UPDATE users SET false_numbers = false_numbers + 1 WHERE login = ?""", (self.login,))
            con.commit()
        else:
            cur.execute(
                """UPDATE users SET true_numbers = true_numbers + 1 WHERE login = ?""", (self.login,))
            con.commit()
            self.random_digit()

    def btn_animal_1(self):  # Нажали на кнопку ответа 1 в игре 'Отгадай животное'
        if self.an == self.animal_button1.text():
            self.play_sound("data/sounds/правильно")
            cur.execute(
                """UPDATE users SET true_animals = true_animals + 1 WHERE login = ?""", (self.login,))
            con.commit()
            self.random_animals_button()
        else:
            self.play_sound("data/sounds/неправильно")
            sound = QSound("data/sounds/неправильно.wav", self)
            sound.play()
            cur.execute(
                """UPDATE users SET false_animals = false_animals + 1 WHERE login = ?""", (self.login,))
            con.commit()

    def btn_animal_2(self):  # Нажали на кнопку ответа 2 в игре 'Отгадай животное'
        if self.an == self.animal_button2.text():
            self.play_sound('data/sounds/правильно')
            cur.execute(
                """UPDATE users SET true_animals = true_animals + 1 WHERE login = ?""", (self.login,))
            self.random_animals_button()
        else:
            self.play_sound('data/sounds/неправильно')
            cur.execute(
                """UPDATE users SET false_animals = false_animals + 1 WHERE login = ?""", (self.login,))

    def keyPressEvent(self, event):  # Обработчик клавиатуры
        if self.alphabet_povtoray.isVisible() and \
                self.label_name.text() == 'Повторяй за мной!':  # в игре 'Повторяй за мной!'(алфавит)
            if event.text().lower() in alphabet:
                self.letterLabel.setText(event.text().upper())
                self.play_sound('data/letters/' + str(event.text()))
        elif self.alphabet_povtoray.isVisible() and \
                self.label_name.text() == 'Что это за буква?':
            if self.flag and event.text() == self.let:
                self.let = random.choice(list(alphabet))
                self.play_sound('data/letters/' + self.let)
                cur.execute(
                    """UPDATE users SET true_chto_eto_za_bykva = true_chto_eto_za_bykva + 1 WHERE login = ?""",
                    (self.login,))
                con.commit()
            elif self.flag:
                self.play_sound("data/sounds/неправильно")
                cur.execute(
                    """UPDATE users SET false_chto_eto_za_bykva = false_chto_eto_za_bykva + 1 WHERE login = ?""",
                    (self.login,))
                con.commit()
            elif not self.flag:
                self.let = random.choice(list(alphabet))
                self.play_sound('data/letters/' + self.let)
                self.flag = True
        elif self.alphabet_bykvi.isVisible() and \
                self.label_name_three.text() == 'Восстанови порядок':
            if event.text() == self.let[1]:
                self.play_sound("data/sounds/правильно")
                self.let = random.choice([alphabet[i:i + 3] for i in range(31)])
                self.label_letters_three.setText(self.let.upper()[0] + '?' + self.let.upper()[2])
                cur.execute(
                    """UPDATE users SET true_bykvi_v_alphabete = true_bykvi_v_alphabete + 1 WHERE login = ?""",
                    (self.login,))
                con.commit()
            else:
                self.play_sound("data/sounds/неправильно")
                cur.execute(
                    """UPDATE users SET false_bykvi_v_alphabete = false_bykvi_v_alphabete + 1 WHERE login = ?""",
                    (self.login,))
                con.commit()
        elif self.animals_widget.isVisible():  # Если это игра 'Животные'
            self.animal = random.choice(animals_data)
            self.animal_name.setText(self.animal.capitalize())
            self.animal_jpg.setPixmap(QtGui.QPixmap('data/animals/' + self.animal + ".jpg"))
            self.play_sound('data/animals/' + self.animal)

        elif self.numbers_uchim.isVisible():  # Если это игра 'Учим цифры'
            if event.text() in '0123456789':
                self.label_number1.setText(event.text())
                self.label_name_of_number1.setText(numbers[int(event.text())])
                self.play_sound('data/digits/' + event.text())

    def eventFilter(self, object, event):  # Обработчик курсора (для игр 'Отгадай животное' и 'Верно или нет?')
        # Если событие от нужных нам кнопок
        if object == self.animal_button1 or object == self.animal_button2:
            if event.type() == QEvent.Enter:
                self.play_sound('data/animals/' + object.text())
                return False
        elif object == self.verno_button:
            if event.type() == QEvent.Enter:
                self.play_sound("data/sounds/да")
                return False
        elif object == self.neverno_button:
            if event.type() == QEvent.Enter:
                self.play_sound("data/sounds/нет")
                return False
        return super().eventFilter(object, event)

    def on_combobox_func(self):  # Поменяли пол (значит меняем аватарку)
        self.g = self.genderBox.currentIndex()
        cur.execute("""UPDATE users SET gender = ? WHERE login = ?""", (self.g, self.login)).fetchall()
        con.commit()
        if self.g == 0:
            self.avatarLabel.setPixmap(QtGui.QPixmap("data/images/boy.png"))
        else:
            self.avatarLabel.setPixmap(QtGui.QPixmap("data/images/girl.png"))

    def delete_pr(self):  # Функция кнопки удалить профиль
        self.close()
        form.show()  # Открываем приветственный виджет
        self.hide()  # Прячем главный виджет
        cur.execute("""DELETE FROM users WHERE login = ?""", (self.login,)).fetchall()
        con.commit()

    def exit_pr(self):  # Функция кнопки выйти из аккаунта
        self.close()
        form.show()  # Открываем приветственный виджет
        self.hide()  # Прячем главный виджет

    def play_sound(self, name):  # Функция проигрывания звуков
        if self.playing:  # Если какой-то звук уже играет - остановить его
            self.sound.stop()
        else:
            self.playing = True
        self.sound = QSound(name + '.wav', self)
        self.sound.play()


    # Эта функция создана, чтобы упростить код нажатия на кнопки алфавита.
    # В неё передается текст кнопки, исходя из которого она воспроизводит тот или иной звук
    def buttons_of_alphabet_games(self, m):
        def calluser():
            if self.alphabet_povtoray.isVisible() and \
                    self.label_name.text() == 'Повторяй за мной!':  # в игре 'Повторяй за мной!'(алфавит)
                sound = QSound('data/letters/' + str(m) + '.wav', self)
                sound.play()
                self.letterLabel.setText(m.upper())
            elif self.alphabet_povtoray.isVisible() and \
                    self.label_name.text() == 'Что это за буква?':  # в игре 'Что это за буква?'(алфавит)
                if self.flag and m == self.let:
                    self.let = random.choice(list(alphabet))
                    sound = QSound('data/letters/' + self.let + ".wav", self)
                    sound.play()
                    cur.execute(
                        """UPDATE users SET true_chto_eto_za_bykva = true_chto_eto_za_bykva + 1 WHERE login = ?""",
                        (self.login,))
                    con.commit()
                elif self.flag:
                    sound = QSound("data/sounds/неправильно.wav", self)
                    sound.play()
                    cur.execute(
                        """UPDATE users SET false_chto_eto_za_bykva = false_chto_eto_za_bykva + 1 WHERE login = ?""",
                        (self.login,))
                    con.commit()
                elif not self.flag:
                    self.let = random.choice(list(alphabet))
                    sound = QSound('data/letters/' + self.let + ".wav", self)
                    sound.play()
                self.flag = True
        return calluser

    # Эта функция кнопок-цифр. Она запускат их озвучку и выводит цифру на экран.
    def buttons_of_numbers(self, m):
        def calluser():
            self.label_number1.setText(m)
            self.label_name_of_number1.setText(numbers[int(m)])
            sound = QSound('data/digits/' + m + '.wav', self)
            sound.play()
        return calluser


def check_login_in_db(log):  # Эта функция проверяет, есть ли уже пользователь с таким логином
    result = cur.execute("""SELECT * FROM users WHERE login = ?""", (log,)).fetchall()
    if len(result) > 0:
        return True
    return False


def check_password(password):
    if len(password) < 8:
        return '    Длина пароля должна быть не меньше 8 символов.'
    elif password.isupper() or password.islower() or password.isdigit():
        return '  Пароль должен содержать символы разного регистра.'
    elif '1' not in password and '2' not in password and '3' not in password and \
            '4' not in password and '5' not in password and '6' not in password and \
            '7' not in password and '8' not in password and \
            '9' not in password and '0' not in password:
        return '           Пароль должен содержать хотя бы 1 цифру.'
    return 'ok'


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    con = sqlite3.connect('profils_db.db')
    QFontDatabase.addApplicationFont(":/PF Cosmonut Pro.ttf")
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    numbers = {0: ' Ноль', 1: 'Один', 2: '  Два', 3: '  Три', 4: 'Четыре', 5: ' Пять', 6: ' Шесть', 7: ' Семь',
               8: 'Восемь', 9: 'Девять'}
    f = open('data/animals/животные.txt', encoding="utf-8-sig")
    animals_data = f.read().split()
    f.close()
    cur = con.cursor()
    app = QApplication(sys.argv)
    form = WelcomeWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
