import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from maingr import Ui_MainWindow
from restaurador import RestauradorController
from gerenciador import GerenciadorController
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icone.ico"))
        self.setWindowTitle("Gerenciador Manager")
        self.restaurador = RestauradorController(self.ui)
        self.gerenciador = GerenciadorController(self.ui)

        self.largura_aberto = 846
        self.largura_fechado = 490  

        self.restaurador_visivel = False

        self.ui.exibir_ocultar.clicked.connect(self.toggle_restaurador)

        self.iniciar_fechado()

    def iniciar_fechado(self):
        self.ui.widgetrestaurador.setVisible(False)
        self.ui.widgetrestaurador.setMinimumWidth(0)

        self.setFixedWidth(self.largura_fechado)
        self.ui.exibir_ocultar.setText(">")

    def toggle_restaurador(self):
        self.restaurador_visivel = not self.restaurador_visivel

        if self.restaurador_visivel:
            self.ui.widgetrestaurador.setVisible(True)
            self.ui.widgetrestaurador.setMinimumWidth(350)

            self.setFixedWidth(self.largura_aberto)
            self.ui.exibir_ocultar.setText("<")

        else:
            self.ui.widgetrestaurador.setVisible(False)
            self.ui.widgetrestaurador.setMinimumWidth(0)

            self.setFixedWidth(self.largura_fechado)
            self.ui.exibir_ocultar.setText(">")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()             
    sys.exit(app.exec())       
