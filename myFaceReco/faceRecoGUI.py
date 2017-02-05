# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceReco.ui'
#
# Created: Sat Feb 04 20:39:23 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(653, 265)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(653, 265))
        Dialog.setMaximumSize(QtCore.QSize(653, 265))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 211, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lePath2Ref = QtGui.QLineEdit(Dialog)
        self.lePath2Ref.setGeometry(QtCore.QRect(30, 50, 191, 21))
        self.lePath2Ref.setObjectName(_fromUtf8("lePath2Ref"))
        self.pbParcourirDir = QtGui.QPushButton(Dialog)
        self.pbParcourirDir.setGeometry(QtCore.QRect(230, 50, 75, 23))
        self.pbParcourirDir.setObjectName(_fromUtf8("pbParcourirDir"))
        self.lePhoto = QtGui.QLineEdit(Dialog)
        self.lePhoto.setGeometry(QtCore.QRect(30, 110, 191, 21))
        self.lePhoto.setObjectName(_fromUtf8("lePhoto"))
        self.pbParcourirPhoto = QtGui.QPushButton(Dialog)
        self.pbParcourirPhoto.setGeometry(QtCore.QRect(230, 110, 75, 23))
        self.pbParcourirPhoto.setObjectName(_fromUtf8("pbParcourirPhoto"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 181, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.slideSeuil = QtGui.QSlider(Dialog)
        self.slideSeuil.setGeometry(QtCore.QRect(30, 190, 191, 19))
        self.slideSeuil.setMaximum(50)
        self.slideSeuil.setProperty("value", 20)
        self.slideSeuil.setOrientation(QtCore.Qt.Horizontal)
        self.slideSeuil.setObjectName(_fromUtf8("slideSeuil"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 191, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblPhotoToIdent = QtGui.QLabel(Dialog)
        self.lblPhotoToIdent.setGeometry(QtCore.QRect(360, 50, 125, 150))
        self.lblPhotoToIdent.setFrameShape(QtGui.QFrame.Box)
        self.lblPhotoToIdent.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPhotoToIdent.setObjectName(_fromUtf8("lblPhotoToIdent"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(520, 30, 121, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lblPhotoIdentifier = QtGui.QLabel(Dialog)
        self.lblPhotoIdentifier.setGeometry(QtCore.QRect(520, 50, 125, 150))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lblPhotoIdentifier.setFont(font)
        self.lblPhotoIdentifier.setFrameShape(QtGui.QFrame.Box)
        self.lblPhotoIdentifier.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPhotoIdentifier.setObjectName(_fromUtf8("lblPhotoIdentifier"))
        self.lblSeuil = QtGui.QLabel(Dialog)
        self.lblSeuil.setGeometry(QtCore.QRect(250, 190, 31, 21))
        self.lblSeuil.setFrameShape(QtGui.QFrame.Box)
        self.lblSeuil.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSeuil.setObjectName(_fromUtf8("lblSeuil"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 210, 31, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(200, 210, 31, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lblMatch = QtGui.QLabel(Dialog)
        self.lblMatch.setGeometry(QtCore.QRect(360, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblMatch.setFont(font)
        self.lblMatch.setFrameShape(QtGui.QFrame.Box)
        self.lblMatch.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMatch.setObjectName(_fromUtf8("lblMatch"))
        self.pbReconnaissance = QtGui.QPushButton(Dialog)
        self.pbReconnaissance.setGeometry(QtCore.QRect(360, 230, 281, 23))
        self.pbReconnaissance.setObjectName(_fromUtf8("pbReconnaissance"))
        self.lblResultat = QtGui.QLabel(Dialog)
        self.lblResultat.setGeometry(QtCore.QRect(520, 210, 121, 16))
        self.lblResultat.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResultat.setObjectName(_fromUtf8("lblResultat"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.slideSeuil, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), Dialog.changeSeuil)
        QtCore.QObject.connect(self.pbParcourirDir, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.openFileDiagRef)
        QtCore.QObject.connect(self.pbParcourirPhoto, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.openFileDiagIdent)
        QtCore.QObject.connect(self.pbReconnaissance, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reconnaissance)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Reconnaissance faciale", None))
        self.label.setText(_translate("Dialog", "Chemin des photos de références :", None))
        self.pbParcourirDir.setText(_translate("Dialog", "Parcourir...", None))
        self.pbParcourirPhoto.setText(_translate("Dialog", "Parcourir...", None))
        self.label_2.setText(_translate("Dialog", "Photo à identifier :", None))
        self.label_3.setText(_translate("Dialog", "Seuil de discrimination", None))
        self.lblPhotoToIdent.setText(_translate("Dialog", "Photo", None))
        self.label_6.setText(_translate("Dialog", "Resultat ...", None))
        self.lblPhotoIdentifier.setText(_translate("Dialog", "?", None))
        self.lblSeuil.setText(_translate("Dialog", "2", None))
        self.label_8.setText(_translate("Dialog", "0", None))
        self.label_9.setText(_translate("Dialog", "5", None))
        self.lblMatch.setText(_translate("Dialog", "MATCH ...", None))
        self.pbReconnaissance.setText(_translate("Dialog", "Lancer la reconnaissance ...", None))
        self.lblResultat.setText(_translate("Dialog", "...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

