# -*- coding: utf-8 -*-
# main window source code

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from table import TableModel
#mport app_rc
import csv


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 881)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/sheet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.LineEdit.setMaximumSize(QtCore.QSize(3840, 25))
        self.LineEdit.setObjectName("lineEdit")
        self.LineEdit.setToolTip('Ввід виразу починати з "==", далі вираз.')
        self.verticalLayout.addWidget(self.LineEdit, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setMaximumSize(QtCore.QSize(3840, 80))
        self.frame.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        #
        # Table
        #
        self.tableWidget = TableModel()
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        #
        # Hidden table
        #
        self.tableHidden = TableModel()
        self.tableHidden.setObjectName("tableHidden")
        self.tableHidden.setObjectName("tableWidget")
        #
        # Menubar
        #
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionOpen")
        self.actionNew.triggered.connect(self.new_table)
        icon0 = QtGui.QIcon()
        icon0.addPixmap(QtGui.QPixmap(":/iconsMain/images/new-document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon0)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconsMain/images/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.open)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconsMain/images/save2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save)
        # save value: if file has already been saved
        self.save_value = 0
        # save path: if file has already been saved
        self.save_path = ''

        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconsMain/images/save1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon3)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.triggered.connect(sys.exit)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconsMain/images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionAddRow = QtWidgets.QAction(MainWindow)
        self.actionAddRow.setObjectName("actionAddRow")
        self.actionAddRow.triggered.connect(self.add_row)
        self.actionAddColumn = QtWidgets.QAction(MainWindow)
        self.actionAddColumn.setObjectName("actionAddRow")
        self.actionAddColumn.triggered.connect(self.add_column)
        #
        # Changed:
        self.actionDelRow =QtWidgets.QAction(MainWindow)
        self.actionDelRow.setObjectName("actionDelRow")
        self.actionDelRow.triggered.connect(self.del_row)
        self.actionDelColumn =QtWidgets.QAction(MainWindow)
        self.actionDelColumn.setObjectName("actionDelCol")
        self.actionDelColumn.triggered.connect(self.del_column)
        #
        #
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(self.help)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionAddRow)
        self.menuEdit.addAction(self.actionAddColumn)
        #
        self.menuEdit.addAction(self.actionDelRow)
        self.menuEdit.addAction(self.actionDelColumn)
        #
        self.menuAbout.addAction(self.action)
        # self.menuAbout.addAction(self.action_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.tableWidget.itemChanged.connect(self.onItemChanged)
        self.tableWidget.itemSelectionChanged.connect(self.onItemSelectionChanged)
        # self.tableWidget.currentItemChanged.connect(self.onItemChanged)
        # self.tableWidget.itemActivated.connect(lambda: [print("Activated")])
        self.LineEdit.textChanged.connect(self.onTextChanged)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def onItemChanged(self, num=0):
        # пользователь вводит в ячейку ТЕКСТ
        # ТЕКСТ попадает в вторую таблицу, обрабатывается и получается РЕЗУЛЬТАТ
        # Результат попадает в ячейку
        # ТЕКСТ выводится в строчку
        # print("ON ITEM CHANGED")
        self.tableWidget.blockSignals(True)
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        item_from_cell = self.tableWidget.item(row, column)
        if type(item_from_cell) == type(None):
            # print("onItemChanged NONE")
            self.tableWidget.blockSignals(False)
            return
        cell_text = item_from_cell.text()  # input
        item_cell = QTableWidgetItem(cell_text)
        self.tableHidden.setItem(row, column, item_cell)

        result_text = self.processer(cell_text)
        result_item = QTableWidgetItem(result_text)
        self.tableWidget.setItem(row, column, result_item)
        self.LineEdit.setText(cell_text)
        self.tableWidget.blockSignals(False)
        if num == 0:
            self.onItemChanged(1)
        self.update()
        self.save_value = 0

    def onTextChanged(self):
        print("On text changed")
        # sends input to hidden table (already reworked)
        self.tableWidget.blockSignals(True)
        if not self.LineEdit.hasFocus():
            self.tableWidget.blockSignals(False)
            return
        row, column = self.tableWidget.currentRow(), self.tableWidget.currentColumn()
        if row == column == -1:
            self.tableWidget.blockSignals(False)
            return
        # print("Cell:", row, column )
        text = self.LineEdit.text()
        result = self.processer(text)
        print(text)
        print(result)
        itemH = QTableWidgetItem(text)
        self.tableHidden.setItem(row, column, itemH)
        # print(itemH.text())
        itemW = QTableWidgetItem(result)
        # print(itemW.text())
        self.tableWidget.setItem(row, column, itemW)
        self.tableWidget.blockSignals(False)
        self.update()
        self.save_value = 0

    def onItemSelectionChanged(self):
        # changes lineEdit
        self.tableWidget.blockSignals(True)
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        item_from_cell = self.tableHidden.item(row, column)
        if type(item_from_cell) == type(None):
            self.tableWidget.blockSignals(False)
            return
        cell_text = item_from_cell.text()
        self.LineEdit.setText(cell_text)
        self.tableWidget.blockSignals(False)

    def deleteContent(self):
        self.tableWidget.blockSignals(True)
        for item in self.tableWidget.selectedItems():
            row = item.row()
            col = item.column()
            self.tableWidget.setItem(row, col, QTableWidgetItem(""))
            self.tableHidden.setItem(row, col, QTableWidgetItem(""))
        self.tableWidget.blockSignals(False)
        self.update()

    def update(self):

        self.tableWidget.blockSignals(True)
        row = self.tableWidget.rowCount()
        column = self.tableWidget.columnCount()
        # print("R:", row, "COL:", column)
        for i in range(row):
            for k in range(column):
                item_from_cell = self.tableHidden.item(i, k)
                try:
                    text = item_from_cell.text()
                    if type(text) == None or text.strip() == '':
                        continue
                except Exception as exp:
                    continue
                # print(i, k)

                # print("TEXT", text)
                result_text = self.processer(text)
                result_item = QTableWidgetItem(result_text)
                # print("RES", result_item)
                self.tableWidget.setItem(i, k, result_item)
        self.tableWidget.blockSignals(False)

    def add_row(self):
        self.tableWidget.add_row()
        self.tableHidden.add_row()

    def add_column(self):
        self.tableWidget.add_column()
        self.tableHidden.add_column()

    def del_row(self):
        self.tableWidget.del_row()
        self.tableHidden.del_row()

    def del_column(self):
        self.tableWidget.del_column()
        self.tableHidden.del_column()

    def confirm_new_table(self):
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle('Допомога')
        icon0 = QtGui.QIcon()
        icon0.addPixmap(QtGui.QPixmap(":/iconsMain/images/new-document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        box.setWindowIcon(icon0)
        box.setText("Створити нову таблицю?")
        box.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        no = box.button(QMessageBox.Close)
        no.setText("Скасувати")
        yes = box.button(QMessageBox.Ok)
        yes.setText("Створити")

        box.exec()
        if box.clickedButton() == no:
            box.close()
            return False
        else:
            box.close()
            return True

    def new_table(self):
        confirmation: bool = self.confirm_new_table()
        if not confirmation:
            return
        self.table_default()
        self.setWindowTitle("Табличний редактор")
        self.LineEdit.clear()
        self.save_value = 0
        self.save_path = ''

    def table_default(self):
        self.tableWidget.to_default()
        self.tableHidden.to_default()
        self.save_value = 0
        self.save_path = ''

    #
    # Functions for saving tables
    #
    def save(self):
        # print("SELF SAVES:", self.save_value, self.save_path)
        if self.save_value == 1:
            return
        elif self.save_path != '':
            self.handleSave((self.save_path, ''))
        else:
            self.handleSave()

    def save_as(self):
        self.handleSave()

    def open(self, num = 1):
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        save = QMessageBox.Save
        box.setWindowTitle(' ')
        box.setText("Зберегти зміни в таблиці?")
        box.setStandardButtons(QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel)
        save = box.button(QMessageBox.Save)
        save.setText('Зберегти')
        dont_save = box.button(QMessageBox.Close)
        dont_save.setText("Не зберігати")
        cancel = box.button(QMessageBox.Cancel)
        cancel.setText("Скасувати")
        box.exec()

        if box.clickedButton() == dont_save:
            self.handleOpen()
        elif box.clickedButton() == save:
            self.save()
            self.handleOpen()
        else:
            pass


    #
    # save func
    #
    def handleSave(self, path=('', '')):
        self.tableWidget.blockSignals(True)
        print(path)
        try:
            if path[0] == '':
                path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')
            print(path)
            if path != '' and path is not None:
                with open(path[0], 'w', encoding='utf-8') as stream:
                    writer = csv.writer(stream)
                    for row in range(self.tableWidget.rowCount()):
                        rowdata = []
                        for column in range(self.tableWidget.columnCount()):
                            item = self.tableWidget.item(row, column)
                            if item is not None:
                                rowdata.append(
                                    (item.text()))
                            else:
                                rowdata.append('')
                        writer.writerow(rowdata)
                with open(path[0][:-4] + 'h' + path[0][-4:], 'w', encoding='utf-8') as stream:
                    writer = csv.writer(stream)
                    for row in range(self.tableHidden.rowCount()):
                        rowdata = []
                        for column in range(self.tableHidden.columnCount()):
                            item = self.tableHidden.item(row, column)
                            if item is not None:
                                rowdata.append(
                                    (item.text()))
                            else:
                                rowdata.append('')
                        writer.writerow(rowdata)
                self.save_value = 1
                self.save_path = path[0]
                print("NEW SAVE PATH", path[0])
                self.setWindowTitle("Табличний редактор" + path[0][:-4] + 'h' + path[0][-4:])
        except Exception as exp:
            self.LineEdit.setText(f"{exp}")
        finally:
            self.tableWidget.blockSignals(False)

    #
    # open func
    #

    def handleOpen(self, ):
        self.tableWidget.blockSignals(True)
        try:
            path = QtWidgets.QFileDialog.getOpenFileName(
                self, 'Open File', '', 'CSV(*.csv)')
            if path[0] != '' and path is not None:
                with open(path[0], 'r', encoding='utf-8') as stream:
                    #if not self.confirm_new_table():
                    #    return
                    self.tableWidget.setRowCount(0)
                    self.tableWidget.setColumnCount(0)
                    self.tableHidden.setRowCount(0)
                    self.tableHidden.setColumnCount(0)
                    data = list(csv.reader(stream))[::2]
                    for i in range(len(data)):  # rows
                        for k in range(len(data[i])):  # cols
                            cell = data[i][k]
                            if cell is None or cell == "":
                                item = QtWidgets.QTableWidgetItem("")
                            else:
                                item = QtWidgets.QTableWidgetItem(cell)
                                # print(cell)
                            if i >= self.tableWidget.rowCount(): self.add_row()
                            if k >= self.tableWidget.columnCount(): self.add_column()
                            self.tableWidget.setItem(i, k, item)
                with open(path[0][:-4] + 'h' + path[0][-4:], 'r', encoding='utf-8') as stream:
                    data = list(csv.reader(stream))[::2]
                    for i in range(len(data)):
                        for k in range(len(data[i])):
                            cell = data[i][k]
                            if cell is None or cell == "":
                                item = QtWidgets.QTableWidgetItem("")
                            else:
                                item = QtWidgets.QTableWidgetItem(cell)
                            self.tableHidden.setItem(i, k, item)
                self.save_value = 1
                self.save_path = path[0]
                self.setWindowTitle("VExcel" + path[0][:-4] + 'h' + path[0][-4:])
        except Exception as exp:
            self.LineEdit.setText(f"{exp}")
        finally:
            self.tableWidget.blockSignals(False)

    #
    # Processer
    #
    def processer(self, item: str, num=10):
        # gets calculated value
        # needs to be called every time sth changes
        if num == 0:
            # recursion limit
            return "Recursion limit: " + item
        try:
            text = item
            # if not formula returns itself
            if not text.startswith("=="):
                # print("NOT ==")
                return text

            new_text = text[2:].replace("mod", "%").replace("div", "//").replace("max", "max") \
                .replace("min", "min").replace("^", "**").replace("Хиба", "False").replace('Істина', 'True')
            to_replace = []
            replace_with = []
            for i in range(len(new_text) - 1):
                row, column = 0, 0
                first_letter = new_text[i]
                # print("FL: " + first_letter)
                alphabet = self.tableWidget.alphabet
                if first_letter in alphabet:
                    # print("first letter in alphabet")
                    second_letter = new_text[i + 1]
                    # print(second_letter)
                    # A1
                    ind = ''
                    if second_letter in '1234567890':
                        # print(second_letter + "in nums")
                        for k in range(i + 1, len(new_text)):
                            if new_text[k] in '1234567890':
                                ind += new_text[k]
                            else:
                                break
                        if ind == '':
                            result = "#No index:  " + (text)
                            return result
                        to_replace.append(first_letter + ind)
                        row = int(ind) - 1
                        column = self.tableWidget.alpha.index(first_letter)
                    # AA2
                    elif second_letter in alphabet:
                        # print(second_letter + " 2 in alphabet")
                        for k in range(i + 2, len(new_text)):
                            if new_text[k].isnumeric():
                                ind += new_text[k]
                            else:
                                break
                        if ind == '':
                            result = "No index: " + (text)
                            return result
                        to_replace.append(first_letter + second_letter + ind)
                        row = int(ind) - 1
                        # print(first_letter + second_letter)
                        try:
                            column = self.tableWidget.alpha.index(first_letter + second_letter)
                        except:
                            result = "#Possible wrong indices error: " + (text)
                            return result
                    else:
                        # print("A1 and AA2 doesnt match")
                        result = "#Wrong input: " + (text)
                        return result

                    # print("row", row)
                    # print("col ", column)
                    item_from_cell = self.tableHidden.item(row, column)
                    if type(item_from_cell) == type(None):
                        # print("TYPE NONE")
                        result = "#Empty cell error: " + (text)
                        return result

                    result_from_cell = self.processer(item_from_cell.text(), num - 1)
                    replace_with.append(result_from_cell)
                # print("TO REPLACE:", to_replace)
                # print("WITH:", replace_with)
                # a2+a2
            for i in range(len(to_replace)):
                new_text = new_text.replace(to_replace[i], replace_with[i])
            new_text = new_text.replace("mod", "%").replace("div", "//").replace("max", "max") \
                .replace("min", "min").replace("^", "**").replace("Хиба", "False").replace('Істина', 'True')
            # print(new_text)
            for i in new_text:
                if i not in '1234567890<>,.+-/*&%||()= minaxTrueFalse':
                    # print(i)
                    # print("Bad symbol")
                    return "#Bad symbol: " + text
            try:
                result = eval(new_text)
            except ZeroDivisionError:
                result = "#Zero division error: " + (text)
            except:
                # print("Eval doesnt calc")
                result = "#Bad expression: " + (text)
            # print("Result: ", result)
            if result == True and type(result) == bool:
                result = "Істина"
            elif result == False and type(result) == bool:
                result = "Хиба"
            return str(result)
        except Exception as exp:
            result = f"#{exp}: " + (text)
            return result

    #
    def help(self):
        box = QMessageBox()
        box.setIcon(QMessageBox.Information)
        box.setWindowTitle('Допомога')
        icon0 = QtGui.QIcon()
        icon0.addPixmap(QtGui.QPixmap(":/iconsMain/images/new-document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        box.setWindowIcon(icon0)
        box.setText("Привіт!\nВ цій програмі ти можеш користуватись табличним редактором.\nОсновні функції:\n" \
                    "+, -, *, / (бінарні операції);\n^ (піднесення у степінь);\n =, <, >;<=, >=, <>;" \
                    "\n max(x,y), mіn(x,y);\nіnc, dec.\n\nPrepared by Нікітіна Софія\nГрупа: К-24\nВаріант: 11")
        box.setStandardButtons(QMessageBox.Close)
        close = box.button(QMessageBox.Close)
        close.setText("Ок")

        box.exec()
        if box.clickedButton() == close:
            box.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Табличний редактор"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menuEdit.setTitle(_translate("MainWindow", "Редагувати"))
        self.menuAbout.setTitle(_translate("MainWindow", "Про програму"))
        self.actionNew.setText(_translate("MainWindow", "Нова таблиця"))
        self.actionOpen.setText(_translate("MainWindow", "Відкрити"))
        self.actionSave.setText(_translate("MainWindow", "Зберегти"))
        self.actionSave_as.setText(_translate("MainWindow", "Зберегти як..."))
        self.actionExit.setText(_translate("MainWindow", "Вийти"))
        self.action.setText(_translate("MainWindow", "Інфо"))
        self.action_2.setText(_translate("MainWindow", "Інфо"))
        self.actionAddRow.setText(_translate("MainWindow", "Додати строчку"))
        self.actionAddColumn.setText(_translate("MainWindow", "Додати колонку"))
        self.actionDelRow.setText(_translate("MainWindow", "Видалити строчку"))
        self.actionDelColumn.setText(_translate("MainWindow", "Видалити колонку"))