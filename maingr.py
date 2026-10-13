# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingr.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widgetmanager = QWidget(self.centralwidget)
        self.widgetmanager.setObjectName(u"widgetmanager")
        self.verticalLayout_2 = QVBoxLayout(self.widgetmanager)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lmanager = QLabel(self.widgetmanager)
        self.lmanager.setObjectName(u"lmanager")

        self.verticalLayout_2.addWidget(self.lmanager)

        self.areamanager = QScrollArea(self.widgetmanager)
        self.areamanager.setObjectName(u"areamanager")
        self.areamanager.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 143, 533))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mbot1 = QPushButton(self.scrollAreaWidgetContents)
        self.mbot1.setObjectName(u"mbot1")

        self.verticalLayout_5.addWidget(self.mbot1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.areamanager.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.areamanager)


        self.horizontalLayout.addWidget(self.widgetmanager)

        self.widgetinfo = QWidget(self.centralwidget)
        self.widgetinfo.setObjectName(u"widgetinfo")
        self.verticalLayout_3 = QVBoxLayout(self.widgetinfo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widgetinfo)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.lbanco = QLabel(self.widgetinfo)
        self.lbanco.setObjectName(u"lbanco")

        self.verticalLayout_3.addWidget(self.lbanco)

        self.lservidor = QLabel(self.widgetinfo)
        self.lservidor.setObjectName(u"lservidor")

        self.verticalLayout_3.addWidget(self.lservidor)

        self.lversao = QLabel(self.widgetinfo)
        self.lversao.setObjectName(u"lversao")

        self.verticalLayout_3.addWidget(self.lversao)

        self.batualizag = QPushButton(self.widgetinfo)
        self.batualizag.setObjectName(u"batualizag")

        self.verticalLayout_3.addWidget(self.batualizag)

        self.bselecionarg = QPushButton(self.widgetinfo)
        self.bselecionarg.setObjectName(u"bselecionarg")

        self.verticalLayout_3.addWidget(self.bselecionarg)

        self.bpastaver = QPushButton(self.widgetinfo)
        self.bpastaver.setObjectName(u"bpastaver")

        self.verticalLayout_3.addWidget(self.bpastaver)


        self.horizontalLayout.addWidget(self.widgetinfo, 0, Qt.AlignVCenter)

        self.widgetatualiza = QWidget(self.centralwidget)
        self.widgetatualiza.setObjectName(u"widgetatualiza")
        self.verticalLayout = QVBoxLayout(self.widgetatualiza)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.latualiza = QLabel(self.widgetatualiza)
        self.latualiza.setObjectName(u"latualiza")

        self.verticalLayout.addWidget(self.latualiza)

        self.areaatualiza = QScrollArea(self.widgetatualiza)
        self.areaatualiza.setObjectName(u"areaatualiza")
        self.areaatualiza.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 143, 533))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.abot1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.abot1.setObjectName(u"abot1")

        self.verticalLayout_4.addWidget(self.abot1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.areaatualiza.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.areaatualiza)


        self.horizontalLayout.addWidget(self.widgetatualiza)

        self.widgetrestaurador = QWidget(self.centralwidget)
        self.widgetrestaurador.setObjectName(u"widgetrestaurador")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetrestaurador.sizePolicy().hasHeightForWidth())
        self.widgetrestaurador.setSizePolicy(sizePolicy)
        self.widgetrestaurador.setMinimumSize(QSize(350, 0))
        self.verticalLayout_6 = QVBoxLayout(self.widgetrestaurador)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.widgetrestaurador)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pagerest = QWidget()
        self.pagerest.setObjectName(u"pagerest")
        self.lselecaorest = QLabel(self.pagerest)
        self.lselecaorest.setObjectName(u"lselecaorest")
        self.lselecaorest.setGeometry(QRect(10, 50, 321, 16))
        self.batualizarest = QPushButton(self.pagerest)
        self.batualizarest.setObjectName(u"batualizarest")
        self.batualizarest.setGeometry(QRect(120, 70, 91, 23))
        self.linenomebanco = QLineEdit(self.pagerest)
        self.linenomebanco.setObjectName(u"linenomebanco")
        self.linenomebanco.setGeometry(QRect(60, 320, 221, 20))
        self.brestaurar = QPushButton(self.pagerest)
        self.brestaurar.setObjectName(u"brestaurar")
        self.brestaurar.setGeometry(QRect(130, 340, 75, 23))
        self.btelaexcluir = QPushButton(self.pagerest)
        self.btelaexcluir.setObjectName(u"btelaexcluir")
        self.btelaexcluir.setGeometry(QRect(190, 20, 101, 23))
        self.label_4 = QLabel(self.pagerest)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 0, 81, 20))
        self.btelarestaurar_2 = QPushButton(self.pagerest)
        self.btelarestaurar_2.setObjectName(u"btelarestaurar_2")
        self.btelarestaurar_2.setEnabled(False)
        self.btelarestaurar_2.setGeometry(QRect(30, 20, 101, 23))
        self.tableViewrestaurar = QTableView(self.pagerest)
        self.tableViewrestaurar.setObjectName(u"tableViewrestaurar")
        self.tableViewrestaurar.setGeometry(QRect(0, 100, 331, 211))
        self.stackedWidget.addWidget(self.pagerest)
        self.pageexclu = QWidget()
        self.pageexclu.setObjectName(u"pageexclu")
        self.btelarestaurar = QPushButton(self.pageexclu)
        self.btelarestaurar.setObjectName(u"btelarestaurar")
        self.btelarestaurar.setGeometry(QRect(30, 20, 101, 23))
        self.bexcluir = QPushButton(self.pageexclu)
        self.bexcluir.setObjectName(u"bexcluir")
        self.bexcluir.setGeometry(QRect(130, 320, 75, 23))
        self.batualizaexclu = QPushButton(self.pageexclu)
        self.batualizaexclu.setObjectName(u"batualizaexclu")
        self.batualizaexclu.setGeometry(QRect(120, 70, 91, 23))
        self.label_5 = QLabel(self.pageexclu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 0, 81, 20))
        self.lselecaoexclu = QLabel(self.pageexclu)
        self.lselecaoexclu.setObjectName(u"lselecaoexclu")
        self.lselecaoexclu.setGeometry(QRect(10, 50, 311, 16))
        self.btelaexcluir_2 = QPushButton(self.pageexclu)
        self.btelaexcluir_2.setObjectName(u"btelaexcluir_2")
        self.btelaexcluir_2.setEnabled(False)
        self.btelaexcluir_2.setGeometry(QRect(190, 20, 101, 23))
        self.tableViewexclu = QTableView(self.pageexclu)
        self.tableViewexclu.setObjectName(u"tableViewexclu")
        self.tableViewexclu.setGeometry(QRect(0, 100, 331, 211))
        self.stackedWidget.addWidget(self.pageexclu)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widgetrestaurador)

        self.exibir_ocultar = QToolButton(self.centralwidget)
        self.exibir_ocultar.setObjectName(u"exibir_ocultar")

        self.horizontalLayout.addWidget(self.exibir_ocultar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lmanager.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Manager</span></p></body></html>", None))
        self.mbot1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"By: Cronos", None))
        self.lbanco.setText(QCoreApplication.translate("MainWindow", u"Banco:", None))
        self.lservidor.setText(QCoreApplication.translate("MainWindow", u"Servidor:", None))
        self.lversao.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o:", None))
        self.batualizag.setText(QCoreApplication.translate("MainWindow", u"Atualizar Listas", None))
        self.bselecionarg.setText(QCoreApplication.translate("MainWindow", u"Selecionar Banco", None))
        self.bpastaver.setText(QCoreApplication.translate("MainWindow", u"Pasta vers\u00e3o", None))
        self.latualiza.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Atualiza</span></p></body></html>", None))
        self.abot1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lselecaorest.setText(QCoreApplication.translate("MainWindow", u"Selecione um arquivo de backup (.BAK / .MAX)", None))
        self.batualizarest.setText(QCoreApplication.translate("MainWindow", u"Atualizar Lista", None))
        self.linenomebanco.setInputMask("")
        self.linenomebanco.setText("")
        self.linenomebanco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Banco (Sem Max_)", None))
        self.brestaurar.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.btelaexcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir Banco", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RESTAURADOR", None))
        self.btelarestaurar_2.setText(QCoreApplication.translate("MainWindow", u"Restaurar Banco", None))
        self.btelarestaurar.setText(QCoreApplication.translate("MainWindow", u"Restaurar Banco", None))
        self.bexcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.batualizaexclu.setText(QCoreApplication.translate("MainWindow", u"Atualizar Lista", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RESTAURADOR", None))
        self.lselecaoexclu.setText(QCoreApplication.translate("MainWindow", u"Selecione um banco de dados para exclus\u00e3o", None))
        self.btelaexcluir_2.setText(QCoreApplication.translate("MainWindow", u"Excluir Banco", None))
        self.exibir_ocultar.setText(QCoreApplication.translate("MainWindow", u">", None))
    # retranslateUi

