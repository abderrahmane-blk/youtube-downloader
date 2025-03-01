# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'p1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import resources_rc

from clipboard_text_on_click import ClipboardPasteLineEdit 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowOpacity(0.980000000000000)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget > Qlabel{\n"
"	color :#faafff;\n"
"	font-size:26px;\n"
"font-weigt:bold;\n"
"}\n"
"\n"
"\n"
".description\n"
"{\n"
"	color :white;\n"
"	font-size:18px;\n"
"\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:rgb(53, 53, 53);\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SettingsTabWidget = QTabWidget(self.widget)
        self.SettingsTabWidget.setObjectName(u"SettingsTabWidget")
        self.SettingsTabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.SettingsTabWidget.setStyleSheet(u"QTabWidget{\n"
"background-color:#aaaaaa;\n"
"}\n"
"\n"
"QTabWidget::pane { /* Style the area *behind* the tabs (the content area) */\n"
"    background-color: #2b2f30; /* background for the pane */\n"
"    border: 0px solid white; /* Optional: Add a border to the pane */\n"
"}\n"
"\n"
"QTabWidget::tab-bar { /* Style the tab bar itself */\n"
"    alignment: center; /* Example: Center the tabs */\n"
"    /* Add spacing around the tab bar if needed: padding: 5px; */\n"
"}\n"
"\n"
"QTabBar::tab { /* Style individual tabs */\n"
"    background-color: #2b2f30; /* Example: Light gray for inactive tabs */\n"
"    color: grey; /* Dark text color for inactive tabs */\n"
"    border: 1px solid #ccc; /* Optional: Add borders to the tabs */\n"
"    border-top-left-radius: 0px; /* Optional: Round the top corners */\n"
"    border-top-right-radius: 4px;\n"
"    padding: 8px 15px; /* Adjust padding as needed */\n"
"    margin-right: 0px; /* Add spacing between tabs */\n"
"}\n"
"\n"
"QTabBar::tab:selected { /* Style the selec"
                        "ted tab */\n"
"    background-color: #2b2f30; /* Example: White background for selected tab */\n"
"    color: #007bff; /* Example: Blue text for selected tab */\n"
"    border-bottom: 2px solid #007bff; /* Example: Blue underline for selected tab */\n"
"}\n"
"\n"
"QTabBar::tab:hover { /* Style tabs on hover */\n"
"    background-color: #1b1f10; /* Example: Slightly lighter background on hover */\n"
"}")
        self.SettingsTabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.SettingsTabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.SettingsTabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.SettingsTabWidget.setDocumentMode(True)
        self.SettingsTabWidget.setTabsClosable(False)
        self.SettingsTabWidget.setTabBarAutoHide(True)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.main)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(16777215, 130))
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 16px;\n"
"    background-color: transparent; /* Semi-transparent black background */\n"
"    padding: 5px 6px; /* Add padding for better appearance */\n"
"    border-radius: 3px; /* Optional: Rounded corners */\n"
"}")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_3 = ClipboardPasteLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	background :#363b3c;\n"
"	color :white;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #363b3c; /* Light background */\n"
"    border: 1px solid #ced4da; /* Subtle border */\n"
"    border-radius: 10px; /* Slightly rounded corners */\n"
"    padding: 6px 10px; /* Comfortable padding */\n"
"    font-size: 16px; /* Readable font size */\n"
"    color: #efefef; /* Dark gray text color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #80bdff; /* Highlight border on focus */\n"
"    outline: none; /* Remove default outline */\n"
"    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); /* Subtle shadow on focus */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #adb5bd; /* Lighter placeholder color */\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setMinimumSize(QSize(60, 60))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"background :rgb(39, 141, 220);\n"
"margin-left:10px;\n"
"border-radius:3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background :#365270;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background :#102060;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/f/resources/feather/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.pushButton_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.main)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMinimumSize(QSize(0, 60))
        self.widget_4.setMaximumSize(QSize(16777215, 130))
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 16px;\n"
"    background-color: transparent; /* Semi-transparent black background */\n"
"    padding: 5px 6px; /* Add padding for better appearance */\n"
"    border-radius: 3px; /* Optional: Rounded corners */\n"
"}")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.checkBox = QCheckBox(self.widget_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px; /* Space between checkbox and text */\n"
"    color: #ffffff; /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Width of the checkbox indicator */\n"
"    height: 20px; /* Height of the checkbox indicator */\n"
"    border: 2px solid #888888; /* Border color */\n"
"    border-radius: 3px; /* Rounded corners */\n"
"    background-color: #363b3c; /* Background color */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(39, 141, 220); /* Checked background color */\n"
"    border: 2px solid rgb(39, 141, 220);/*Checked border color*/\n"
"    image: url(:/f/resources/feather/check-circle.svg); /* Replace with your checkmark icon */\n"
"    image-position: center; /* Center the checkmark */\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border-color: #80bdff; /* Highlight border on hover */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    outline: none; /* Remove default focus outline */\n"
""
                        "}")
        self.checkBox.setIconSize(QSize(36, 36))
        self.checkBox.setChecked(False)

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.main)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.widget_5.setMinimumSize(QSize(0, 60))
        self.widget_5.setMaximumSize(QSize(16777215, 130))
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(200, 16777215))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 16px;\n"
"    background-color: transparent; /* Semi-transparent black background */\n"
"    padding: 5px 6px; /* Add padding for better appearance */\n"
"    border-radius: 3px; /* Optional: Rounded corners */\n"
"}")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 16px;\n"
"    background-color: transparent; /* Semi-transparent black background */\n"
"    padding: 5px 6px; /* Add padding for better appearance */\n"
"    border-radius: 3px; /* Optional: Rounded corners */\n"
"}")
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.widget_6 = QWidget(self.main)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.widget_6.setMinimumSize(QSize(0, 60))
        self.widget_6.setMaximumSize(QSize(16777215, 130))
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setMaximumSize(QSize(200, 16777215))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 16px;\n"
"    background-color: transparent; /* Semi-transparent black background */\n"
"    padding: 5px 6px; /* Add padding for better appearance */\n"
"    border-radius: 3px; /* Optional: Rounded corners */\n"
"}")
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 16px;\n"
"    background-color: transparent; /* Semi-transparent black background */\n"
"    padding: 5px 6px; /* Add padding for better appearance */\n"
"    border-radius: 3px; /* Optional: Rounded corners */\n"
"}")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.SettingsTabWidget.addTab(self.main, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.verticalLayout = QVBoxLayout(self.settings_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.settings_tab)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 20, -1, -1)
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 16px;\n"
"    background-color: transparent; /* Semi-transparent black background */\n"
"    padding: 5px 6px; /* Add padding for better appearance */\n"
"    border-radius: 3px; /* Optional: Rounded corners */\n"
"}")
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_4 = QLineEdit(self.widget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	background :#363b3c;\n"
"	color :white;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #363b3c; /* Light background */\n"
"    border: 1px solid #ced4da; /* Subtle border */\n"
"    border-radius: 10px; /* Slightly rounded corners */\n"
"    padding: 6px 10px; /* Comfortable padding */\n"
"    font-size: 16px; /* Readable font size */\n"
"    color: #efefef; /* Dark gray text color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #80bdff; /* Highlight border on focus */\n"
"    outline: none; /* Remove default outline */\n"
"    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); /* Subtle shadow on focus */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #adb5bd; /* Lighter placeholder color */\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineEdit_4)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_7 = QWidget(self.settings_tab)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(200, 16777215))
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 16px;\n"
"    background-color: transparent; /* Semi-transparent black background */\n"
"    padding: 5px 6px; /* Add padding for better appearance */\n"
"    border-radius: 3px; /* Optional: Rounded corners */\n"
"}")
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.quality_comboBox = QComboBox(self.widget_7)
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.setObjectName(u"quality_comboBox")
        self.quality_comboBox.setMaximumSize(QSize(300, 16777215))
        self.quality_comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #0078d4; /* Or your primary color */\n"
"    outline: none; /* Remove default focus outline */\n"
"    box-shadow: 0 0 3px rgba(0, 120, 212, 0.5); /* Optional subtle glow */\n"
"} \n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid rgb(0, 123, 255);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(your_down_arrow_icon.png); /* Replace with your icon */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    background-color: white;\n"
"    selection-background-color: #e0e0e0; /* Selected item background */\n"
"    selection-color: bl"
                        "ack;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 5px;\n"
"    min-height: 20px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.quality_comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addWidget(self.widget_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.SettingsTabWidget.addTab(self.settings_tab, "")

        self.verticalLayout_2.addWidget(self.SettingsTabWidget)


        self.horizontalLayout_6.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.SettingsTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter url", None))
        self.lineEdit_3.setText("")
        self.pushButton_9.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"is it a playlist ?", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"yes", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"is it a downloading ?", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"no", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"is it complete", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.SettingsTabWidget.setTabText(self.SettingsTabWidget.indexOf(self.main), QCoreApplication.translate("MainWindow", u"download", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"download path", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"./downloads/", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"preferred quality  ( or less )", None))
        self.quality_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"best quality", None))
        self.quality_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"audio only", None))
        self.quality_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"144", None))
        self.quality_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"360", None))
        self.quality_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"480", None))
        self.quality_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"560", None))
        self.quality_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"720", None))
        self.quality_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"1080", None))
        self.quality_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"1440", None))
        self.quality_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"2560", None))

        self.SettingsTabWidget.setTabText(self.SettingsTabWidget.indexOf(self.settings_tab), QCoreApplication.translate("MainWindow", u"settings", None))
    # retranslateUi

