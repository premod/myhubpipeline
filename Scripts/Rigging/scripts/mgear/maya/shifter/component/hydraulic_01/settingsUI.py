# MGEAR is under the terms of the MIT License

# Copyright (c) 2016 Jeremie Passerin, Miquel Campos

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author:     Jeremie Passerin      geerem@hotmail.com  www.jeremiepasserin.com
# Author:     Miquel Campos         hello@miquel-campos.com  www.miquel-campos.com
# Date:       2016 / 10 / 10

import mgear.maya.pyqt as gqt
QtGui, QtCore, QtWidgets, wrapInstance = gqt.qt_import()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(269, 560)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.divisions_label = QtWidgets.QLabel(self.layoutWidget)
        self.divisions_label.setObjectName("divisions_label")
        self.horizontalLayout.addWidget(self.divisions_label)
        self.div_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.div_spinBox.setMinimum(2)
        self.div_spinBox.setProperty("value", 2)
        self.div_spinBox.setObjectName("div_spinBox")
        self.horizontalLayout.addWidget(self.div_spinBox)
        self.upvRefArray_groupBox = QtWidgets.QGroupBox(Form)
        self.upvRefArray_groupBox.setGeometry(QtCore.QRect(7, 39, 249, 176))
        self.upvRefArray_groupBox.setObjectName("upvRefArray_groupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.upvRefArray_groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 231, 141))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.upvRefArray_horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.upvRefArray_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.upvRefArray_horizontalLayout.setObjectName("upvRefArray_horizontalLayout")
        self.upvRefArray_verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.upvRefArray_verticalLayout_1.setObjectName("upvRefArray_verticalLayout_1")
        self.refArray_listWidget = QtWidgets.QListWidget(self.layoutWidget_2)
        self.refArray_listWidget.setDragDropOverwriteMode(True)
        self.refArray_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.refArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.refArray_listWidget.setAlternatingRowColors(True)
        self.refArray_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.refArray_listWidget.setSelectionRectVisible(False)
        self.refArray_listWidget.setObjectName("refArray_listWidget")
        self.upvRefArray_verticalLayout_1.addWidget(self.refArray_listWidget)
        self.upvRefArray_horizontalLayout.addLayout(self.upvRefArray_verticalLayout_1)
        self.upvRefArray_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.upvRefArray_verticalLayout_2.setObjectName("upvRefArray_verticalLayout_2")
        self.refArrayAdd_pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.refArrayAdd_pushButton.setObjectName("refArrayAdd_pushButton")
        self.upvRefArray_verticalLayout_2.addWidget(self.refArrayAdd_pushButton)
        self.refArrayRemove_pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.refArrayRemove_pushButton.setObjectName("refArrayRemove_pushButton")
        self.upvRefArray_verticalLayout_2.addWidget(self.refArrayRemove_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.upvRefArray_verticalLayout_2.addItem(spacerItem)
        self.upvRefArray_horizontalLayout.addLayout(self.upvRefArray_verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.divisions_label.setText(gqt.fakeTranslate("Form", "Divisions", None, -1))
        self.upvRefArray_groupBox.setTitle(gqt.fakeTranslate("Form", "Tip Reference Array", None, -1))
        self.refArrayAdd_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.refArrayRemove_pushButton.setText(gqt.fakeTranslate("Form", ">>", None, -1))

