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
        Form.resize(269, 293)
        self.jointConnexionSettings_groupBox = QtWidgets.QGroupBox(Form)
        self.jointConnexionSettings_groupBox.setGeometry(QtCore.QRect(11, 136, 249, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jointConnexionSettings_groupBox.sizePolicy().hasHeightForWidth())
        self.jointConnexionSettings_groupBox.setSizePolicy(sizePolicy)
        self.jointConnexionSettings_groupBox.setObjectName("jointConnexionSettings_groupBox")
        self.widget = QtWidgets.QWidget(self.jointConnexionSettings_groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 16, 231, 47))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.useJointIndex_checkBox = QtWidgets.QCheckBox(self.widget)
        self.useJointIndex_checkBox.setObjectName("useJointIndex_checkBox")
        self.verticalLayout.addWidget(self.useJointIndex_checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.parentJointIndex_label = QtWidgets.QLabel(self.widget)
        self.parentJointIndex_label.setObjectName("parentJointIndex_label")
        self.horizontalLayout.addWidget(self.parentJointIndex_label)
        self.parentJointIndex_spinBox = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parentJointIndex_spinBox.sizePolicy().hasHeightForWidth())
        self.parentJointIndex_spinBox.setSizePolicy(sizePolicy)
        self.parentJointIndex_spinBox.setMinimum(-1)
        self.parentJointIndex_spinBox.setMaximum(999999)
        self.parentJointIndex_spinBox.setProperty("value", -1)
        self.parentJointIndex_spinBox.setObjectName("parentJointIndex_spinBox")
        self.horizontalLayout.addWidget(self.parentJointIndex_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(11, 220, 249, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(10, 19, 231, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.host_label = QtWidgets.QLabel(self.widget1)
        self.host_label.setObjectName("host_label")
        self.horizontalLayout_2.addWidget(self.host_label)
        self.host_lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.host_lineEdit.setObjectName("host_lineEdit")
        self.horizontalLayout_2.addWidget(self.host_lineEdit)
        self.host_pushButton = QtWidgets.QPushButton(self.widget1)
        self.host_pushButton.setObjectName("host_pushButton")
        self.horizontalLayout_2.addWidget(self.host_pushButton)
        self.mainSettings_groupBox = QtWidgets.QGroupBox(Form)
        self.mainSettings_groupBox.setGeometry(QtCore.QRect(11, 11, 249, 119))
        self.mainSettings_groupBox.setTitle("")
        self.mainSettings_groupBox.setObjectName("mainSettings_groupBox")
        self.widget2 = QtWidgets.QWidget(self.mainSettings_groupBox)
        self.widget2.setGeometry(QtCore.QRect(10, 10, 231, 100))
        self.widget2.setObjectName("widget2")
        self.formLayout = QtWidgets.QFormLayout(self.widget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(self.widget2)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(self.widget2)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.side_label = QtWidgets.QLabel(self.widget2)
        self.side_label.setObjectName("side_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.side_label)
        self.side_comboBox = QtWidgets.QComboBox(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_comboBox.sizePolicy().hasHeightForWidth())
        self.side_comboBox.setSizePolicy(sizePolicy)
        self.side_comboBox.setObjectName("side_comboBox")
        self.side_comboBox.addItem("")
        self.side_comboBox.addItem("")
        self.side_comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.side_comboBox)
        self.componentIndex_label = QtWidgets.QLabel(self.widget2)
        self.componentIndex_label.setObjectName("componentIndex_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.componentIndex_label)
        self.componentIndex_spinBox = QtWidgets.QSpinBox(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.componentIndex_spinBox.sizePolicy().hasHeightForWidth())
        self.componentIndex_spinBox.setSizePolicy(sizePolicy)
        self.componentIndex_spinBox.setObjectName("componentIndex_spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.componentIndex_spinBox)
        self.conector_label = QtWidgets.QLabel(self.widget2)
        self.conector_label.setObjectName("conector_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.conector_label)
        self.connector_comboBox = QtWidgets.QComboBox(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connector_comboBox.sizePolicy().hasHeightForWidth())
        self.connector_comboBox.setSizePolicy(sizePolicy)
        self.connector_comboBox.setObjectName("connector_comboBox")
        self.connector_comboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.connector_comboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.jointConnexionSettings_groupBox.setTitle(gqt.fakeTranslate("Form", "Joint Connexion Settings", None, -1))
        self.useJointIndex_checkBox.setText(gqt.fakeTranslate("Form", "Use Joint Index", None, -1))
        self.parentJointIndex_label.setText(gqt.fakeTranslate("Form", "Parent Joint Index:", None, -1))
        self.groupBox.setTitle(gqt.fakeTranslate("Form", "Channels Host Settings", None, -1))
        self.host_label.setText(gqt.fakeTranslate("Form", "Host:", None, -1))
        self.host_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.name_label.setText(gqt.fakeTranslate("Form", "Name:", None, -1))
        self.side_label.setText(gqt.fakeTranslate("Form", "Side:", None, -1))
        self.side_comboBox.setItemText(0, gqt.fakeTranslate("Form", "Center", None, -1))
        self.side_comboBox.setItemText(1, gqt.fakeTranslate("Form", "Left", None, -1))
        self.side_comboBox.setItemText(2, gqt.fakeTranslate("Form", "Right", None, -1))
        self.componentIndex_label.setText(gqt.fakeTranslate("Form", "Component Index:", None, -1))
        self.conector_label.setText(gqt.fakeTranslate("Form", "Connector:", None, -1))
        self.connector_comboBox.setItemText(0, gqt.fakeTranslate("Form", "standard", None, -1))

