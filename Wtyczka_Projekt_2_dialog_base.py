# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wtyczka_Projekt_2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setAutoFillBackground(False)
        self.mMapLayerComboBox_layers = QgsMapLayerComboBox(Dialog)
        self.mMapLayerComboBox_layers.setGeometry(QtCore.QRect(150, 80, 160, 27))
        self.mMapLayerComboBox_layers.setObjectName("mMapLayerComboBox_layers")
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 130, 75, 24))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 130, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 130, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label_1.setObjectName("label_1")
        self.label_score = QtWidgets.QLabel(Dialog)
        self.label_score.setGeometry(QtCore.QRect(20, 260, 141, 31))
        self.label_score.setText("")
        self.label_score.setObjectName("label_score")
        self.label_description = QtWidgets.QLabel(Dialog)
        self.label_description.setGeometry(QtCore.QRect(10, 210, 251, 51))
        self.label_description.setText("")
        self.label_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_description.setWordWrap(True)
        self.label_description.setObjectName("label_description")
        self.button_box_cancel = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box_cancel.setGeometry(QtCore.QRect(230, 260, 161, 32))
        self.button_box_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box_cancel.setObjectName("button_box_cancel")
        self.mDateTimeEdit = QgsDateTimeEdit(Dialog)
        self.mDateTimeEdit.setGeometry(QtCore.QRect(-10, 0, 471, 31))
        self.mDateTimeEdit.setAutoFillBackground(True)
        self.mDateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mDateTimeEdit.setObjectName("mDateTimeEdit")
        self.mQgsFileWidget_file = QgsFileWidget(Dialog)
        self.mQgsFileWidget_file.setGeometry(QtCore.QRect(150, 40, 141, 27))
        self.mQgsFileWidget_file.setObjectName("mQgsFileWidget_file")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 151, 41))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_2.setAcceptDrops(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 180, 381, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_1.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.label_1.setText(_translate("Dialog", "Wybierz plik z danymi:"))
        self.label_2.setText(_translate("Dialog", "Wybierz wartstwę do odczytu danych:"))
from qgsdatetimeedit import QgsDateTimeEdit
from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
