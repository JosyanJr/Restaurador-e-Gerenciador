import os
import pyodbc
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView

PASTA_BACKUP = r"C:\Max\Backup"

CONN_STR = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=master;"
    "UID=sa;PWD=macro01"
)

BTN_ATIVO = """
QPushButton {
    background-color: #0078D7;
    color: white;
    font-weight: bold;
    border: 1px solid #005A9E;
}
"""

BTN_NORMAL = ""


class RestauradorController:
    def __init__(self, ui):
        self.ui = ui
        self.bak_path = ""

        # ================= MODELO RESTAURAR =================
        self.model_restore = QStandardItemModel()
        self.model_restore.setHorizontalHeaderLabels(["Arquivo"])
        self.ui.tableViewrestaurar.setModel(self.model_restore)
        self.ui.tableViewrestaurar.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.ui.tableViewrestaurar.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.ui.tableViewrestaurar.horizontalHeader().setStretchLastSection(True)
        self.ui.tableViewrestaurar.verticalHeader().setVisible(False)
        self.ui.tableViewrestaurar.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # ================= MODELO EXCLUIR =================
        self.model_excluir = QStandardItemModel()
        self.model_excluir.setHorizontalHeaderLabels(["Banco de Dados"])
        self.ui.tableViewexclu.setModel(self.model_excluir)
        self.ui.tableViewexclu.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.ui.tableViewexclu.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.ui.tableViewexclu.horizontalHeader().setStretchLastSection(True)
        self.ui.tableViewexclu.verticalHeader().setVisible(False)
        self.ui.tableViewexclu.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # ================= CONEXÕES =================
        self.ui.brestaurar.clicked.connect(self.restaurar)
        self.ui.batualizarest.clicked.connect(self.carregar_listas)
        self.ui.tableViewrestaurar.clicked.connect(self.selecionar_backup)

        self.ui.bexcluir.clicked.connect(self.drop_database)
        self.ui.batualizaexclu.clicked.connect(self.carregar_listas)
        self.ui.tableViewexclu.clicked.connect(self.selecionar_banco)

        self.ui.btelarestaurar.clicked.connect(self.ativar_restaurar)
        self.ui.btelaexcluir.clicked.connect(self.ativar_excluir)

        # Inicial
        self.carregar_listas()
        self.ativar_restaurar()

    # ================= TELAS =================
    def ativar_restaurar(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.btelaexcluir.setEnabled(True)
        self.ui.btelaexcluir.setStyleSheet(BTN_NORMAL)

        self.bak_path = ""
        self.ui.lselecaorest.setText(
            "Selecione um arquivo de backup (.BAK / .MAX)"
        )
        self.ui.tableViewrestaurar.clearSelection()

        # 🔥 ATUALIZA LISTA APENAS AO ENTRAR NA TELA
        self.carregar_baks()


    def ativar_excluir(self):
        self.ui.stackedWidget.setCurrentIndex(1)

        self.ui.btelarestaurar.setEnabled(True)
        self.ui.btelarestaurar.setStyleSheet(BTN_NORMAL)

        self.ui.lselecaoexclu.setText(
            "Selecione um banco de dados para exclusão"
        )
        self.ui.tableViewexclu.clearSelection()

        # 🔥 ATUALIZA LISTA APENAS AO ENTRAR NA TELA
        self.carregar_bancos()


    # ================= LISTAS =================
    def carregar_listas(self):
        self.carregar_baks()
        self.carregar_bancos()

    def carregar_baks(self):
        self.model_restore.removeRows(0, self.model_restore.rowCount())

        if not os.path.exists(PASTA_BACKUP):
            return

        for arq in os.listdir(PASTA_BACKUP):
            if arq.lower().endswith((".bak", ".max")):
                self.model_restore.appendRow([
                    QStandardItem(arq)
                ])

    def carregar_bancos(self):
        self.model_excluir.removeRows(0, self.model_excluir.rowCount())

        conn = pyodbc.connect(CONN_STR)
        cur = conn.cursor()
        cur.execute("""
            SELECT name FROM sys.databases
            WHERE name LIKE 'Max_%'
            ORDER BY name
        """)

        for row in cur.fetchall():
            self.model_excluir.appendRow([
                QStandardItem(row.name)
            ])

    # ================= SELEÇÃO =================
    def selecionar_backup(self, index):
        nome = self.model_restore.item(index.row(), 0).text()
        self.bak_path = os.path.join(PASTA_BACKUP, nome)
        self.ui.lselecaorest.setText(
            f"Arquivo selecionado: {nome}"
        )

    def selecionar_banco(self, index):
        nome = self.model_excluir.item(index.row(), 0).text()
        self.ui.lselecaoexclu.setText(
            f"Banco selecionado: {nome}"
        )

    # ================= RESTORE =================
    def restaurar(self):
        nome_digitado = self.ui.linenomebanco.text().strip()

        if not self.bak_path or not nome_digitado:
            QMessageBox.warning(
                None, "Erro",
                "Selecione um backup e informe o nome do banco"
            )
            return

        banco = f"Max_{nome_digitado}"

        resp = QMessageBox.question(
            None, "Confirmar restauração",
            f"Deseja restaurar o banco:\n\n{banco} ?",
            QMessageBox.Yes | QMessageBox.No
        )
        if resp != QMessageBox.Yes:
            return

        pasta_db = os.path.join(r"C:\Max\Dados", banco)
        os.makedirs(pasta_db, exist_ok=True)

        mdf = os.path.join(pasta_db, "SID_DATA.MDF")
        ldf = os.path.join(pasta_db, "SID_Log.LDF")

        try:
            conn = pyodbc.connect(CONN_STR)
            conn.autocommit = True
            cur = conn.cursor()

            cur.execute(f"""
                RESTORE DATABASE [{banco}]
                FROM DISK = '{self.bak_path}'
                WITH
                    MOVE 'SID_DATA' TO '{mdf}',
                    MOVE 'SID_Log'  TO '{ldf}',
                    REPLACE;
            """)
            QMessageBox.information( None, "Sucesso", f"{banco} restaurado com sucesso" )

            self.ativar_restaurar()

        except Exception as e:
            QMessageBox.critical(None, "Erro", str(e))

    # ================= DROP =================
    def drop_database(self):
        index = self.ui.tableViewexclu.currentIndex()
        if not index.isValid():
            QMessageBox.warning(None, "Erro", "Selecione um banco")
            return

        banco = self.model_excluir.item(index.row(), 0).text()

        resp = QMessageBox.question(
            None, "Confirmar",
            f"Deseja excluir o banco {banco}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if resp != QMessageBox.Yes:
            return

        try:
            conn = pyodbc.connect(CONN_STR)
            conn.autocommit = True
            cur = conn.cursor()

            cur.execute(f"""
                ALTER DATABASE [{banco}]
                SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
                DROP DATABASE [{banco}];
            """)

            # ================= REMOVER PASTA SE ESTIVER VAZIA =================
            pasta_db = os.path.join(r"C:\Max\Dados", banco)

            if os.path.exists(pasta_db):
                try:
                    if not os.listdir(pasta_db):  # pasta vazia
                        os.rmdir(pasta_db)
                    else:
                        print(f"Pasta não vazia, não removida: {pasta_db}")
                except Exception as e:
                    print(f"Erro ao remover pasta {pasta_db}: {e}")
                    
            QMessageBox.information( None, "Sucesso", f"{banco} excluído com sucesso" )


            self.ativar_excluir()

        except Exception as e:
            QMessageBox.critical(None, "Erro", str(e))

