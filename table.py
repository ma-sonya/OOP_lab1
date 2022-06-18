# table class with new functions
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class TableModel(QtWidgets.QTableWidget):
    def __init__(self):
        super(TableModel, self).__init__()
        # headers
        self.alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.n = 5
        self.last_header = self.alpha[-1]
        self.create_table_cells()
        self.initialize_cells()
        self.setToolTip("DEL видаляє зміст")
        self.set_borders()

    def create_table_cells(self):
        # creates table with columns of alphabet and rows of numbers till 200
        self.setColumnCount(len(self.alpha))
        self.setRowCount(self.n)
        for i in range(len(self.alpha)):
            item = QtWidgets.QTableWidgetItem()
            # print(self.alpha[i])
            item.setText(self.alpha[i])
            self.setHorizontalHeaderItem(i, item)

        for i in range(self.n):
            # print(i+1)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i + 1))
            self.setVerticalHeaderItem(i, item)
        self.last_header = self.alpha[-1]

    def initialize_cells(self):
        for i in range(self.n):
            for k in range(len(self.alpha)):
                self.setItem(i, k, QtWidgets.QTableWidgetItem(""))

    def add_row(self, num=1):
        for _ in range(num):
            self.insertRow(self.rowCount())
            self.n += 1

    def del_row(self, num=1):
        for _ in range(num):
            if self.rowCount() > 1:
                self.removeRow(self.rowCount())
                self.n -= 1
            else :
                error = QMessageBox()  # створення випливаючого вікна
                error.setWindowTitle("Помилка")
                error.setText("Досягнуто мінімальний розмір таблиці")
                error.setIcon(QMessageBox.Warning)  # вибираєш якого типу випливе вікно
                error.setStandardButtons(QMessageBox.Ok)  # підсвічується та, що перша вписана

                error.setDefaultButton(QMessageBox.Ok)  # встановлює виділення на Ок
                error.exec_()

        self.create_table_cells()

    def del_column(self, num=1):
        for _ in range(num):
            if(self.columnCount() > 1):
                last_header = self.alpha[-2]
                self.last_header = last_header
                self.removeColumn(self.columnCount())
                deleted = self.alpha[-1]
                del self.alpha[-1]
                self.setColumnCount(len(self.alpha) - 1)
        self.create_table_cells()
        #self.alpha.append(deleted)

    def add_column(self, num=1):
        for _ in range(num):
            header = ''
            last_header = self.last_header
            if last_header == "Z":
                header = "AA"
            elif len(last_header) == 2:
                first_letter = last_header[0]
                second_letter = last_header[1]
                if second_letter == "Z":
                    ind1 = self.alphabet.index(first_letter) + 1
                    ind2 = 0
                    header = self.alpha[ind1] + self.alpha[ind2]
                elif second_letter in self.alphabet:
                    ind2 = self.alphabet.index(second_letter) + 1
                    header = first_letter + self.alphabet[ind2]
                else:
                    break
            # CHANGED
            #
            #
            elif last_header in self.alphabet:
                index = 0
                header = ''
                for i in self.alphabet:
                    if i == last_header:
                        #self.alpha.append(self.alphabet[index +1])
                        header = self.alphabet[index +1]
                        break
                    index +=1
            #
            #
            #
            else:
                print("STH bad hapenned")
                break
            self.alpha.append(header)
            # print(self.alpha)
            self.last_header = header
        self.create_table_cells()

    def to_default(self):
        self.clearContents()
        self.alpha = self.alphabet
        self.n = 200
        self.create_table_cells()
        self.initialize_cells()

    def set_borders(self):
        self.setStyleSheet(
            "QHeaderView::section{"
            "border-top:0px solid #D8D8D8;"
            "border-left:0px solid #D8D8D8;"
            "border-right:1px solid #D8D8D8;"
            "border-bottom: 1px solid #D8D8D8;"
            "background-color:orange;"
            "padding:4px;"
            "}"
            "QTableCornerButton::section{"
            "border-top:0px solid #D8D8D8;"
            "border-left:0px solid #D8D8D8;"
            "border-right:1px solid #D8D8D8;"
            "border-bottom: 1px solid #D8D8D8;"
            "background-color:green;"
            "}")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = TableModel()
        self.setCentralWidget(self.table)
        self.table.add_row(3)
        self.table.add_column(680)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()