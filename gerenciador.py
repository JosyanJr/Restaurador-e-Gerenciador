import os
import sys
import pyodbc
import shutil
import subprocess
import rarfile
import win32api
import psutil


from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QLabel,
    QMessageBox, QScrollArea, QWidget
)
from PySide6.QtCore import Qt

def obter_diretorio_base():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

PASTA_PRINCIPAL = obter_diretorio_base()
PASTA_VERSOES = os.path.join(PASTA_PRINCIPAL, "Versoes")
PASTA_ATUALIZAR = os.path.join(PASTA_VERSOES, "Atualiza")
PASTA_RAR = os.path.join(PASTA_VERSOES, "rar")
ARQUIVO_CONTROLE = os.path.join(PASTA_RAR, "extraidos.txt")


CONN_STR = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=(local);"
    "UID=sa;"
    "PWD=macro01"
)

class GerenciadorController:
    def __init__(self, ui):
        self.ui = ui
        self.ini_path = os.path.join(PASTA_PRINCIPAL, "max.ini")

        # cria pastas necessárias
        os.makedirs(PASTA_VERSOES, exist_ok=True)
        os.makedirs(PASTA_ATUALIZAR, exist_ok=True)
        os.makedirs(PASTA_RAR, exist_ok=True)
        if not os.path.exists(ARQUIVO_CONTROLE):
            open(ARQUIVO_CONTROLE, "w").close()

        self._configurar_layouts()

        # conexões
        self.ui.bselecionarg.clicked.connect(self.abrir_seletor_banco)
        self.ui.batualizag.clicked.connect(self.processar_versoes)  # botão agora processa tudo
        self.ui.bpastaver.clicked.connect(self.abrir_pasta_versoes)

        # inicializações
        self.atualizar_labels_ini()
        self.atualizar_interface()
        self.atualizar_versao_inicial()

    # ================= CONEXÃO BANCO =================
    def get_conn_str(self, banco):
        return (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=(local);"
            f"DATABASE={banco};"
            "UID=sa;PWD=macro01;"
        )

    # ================= LAYOUT =================
    def _configurar_layouts(self):
        self.layout_manager = self.ui.scrollAreaWidgetContents.layout()
        self.layout_atualiza = self.ui.scrollAreaWidgetContents_2.layout()
        self.layout_manager.setAlignment(Qt.AlignTop)
        self.layout_atualiza.setAlignment(Qt.AlignTop)

    def _limpar_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    # ================= INI =================
    def ler_ini(self):
        banco, servidor = "-", "-"
        if not os.path.exists(self.ini_path):
            return banco, servidor
        with open(self.ini_path, "r", encoding="latin-1") as f:
            for linha in f:
                l = linha.lower()
                if l.startswith("initial catalog="):
                    banco = linha.split("=", 1)[1].strip()
                elif l.startswith("data source="):
                    servidor = linha.split("=", 1)[1].strip()
        return banco, servidor

    def alterar_ini(self, banco, servidor):
        if not os.path.exists(self.ini_path):
            QMessageBox.warning(None, "Arquivo não encontrado", "Arquivo max.ini não encontrado.")
            return
        with open(self.ini_path, "r", encoding="latin-1") as f:
            linhas = f.readlines()
        with open(self.ini_path, "w", encoding="latin-1") as f:
            for linha in linhas:
                l = linha.lower()
                if l.startswith("initial catalog="):
                    f.write(f"Initial Catalog={banco}\n")
                elif l.startswith("data source="):
                    f.write(f"Data Source={servidor}\n")
                else:
                    f.write(linha)
        self.atualizar_labels_ini()

    def atualizar_labels_ini(self):
        banco, servidor = self.ler_ini()
        self.ui.lbanco.setText(f"Banco: {banco}")
        self.ui.lservidor.setText(f"Servidor: {servidor}")

    # ================= SQL =================
    def listar_bancos(self):
        conn = pyodbc.connect(CONN_STR)
        cur = conn.cursor()
        cur.execute("""
            SELECT name
            FROM sys.databases
            WHERE name LIKE 'Max_%'
              AND name NOT LIKE '%_AUX'
            ORDER BY name
        """)
        bancos = [r.name for r in cur.fetchall()]
        conn.close()
        return bancos

    def buscar_versao_banco(self, banco):
        try:
            conn = pyodbc.connect(self.get_conn_str(banco), timeout=3)
            cursor = conn.cursor()
            cursor.execute("SELECT TOP 1 cofMaxAtualizaVersao FROM config")
            row = cursor.fetchone()
            conn.close()
            if row and row[0]:
                versao = str(row[0])
                if len(versao) > 4:
                    versao = versao[4:]
                return versao
            return "-"
        except Exception as e:
            print(f"Erro ao buscar versão: {e}")
            return "Erro"

    def atualizar_versao_inicial(self):
        banco, _ = self.ler_ini()
        versao = self.buscar_versao_banco(banco) if banco != "-" else "-"
        self.ui.lversao.setText(f"Versão: {versao}")

    # ================= RAR =================
    def carregar_lista_extraidos(self):
        if not os.path.exists(ARQUIVO_CONTROLE):
            return set()
        with open(ARQUIVO_CONTROLE, "r", encoding="utf-8") as f:
            return set(linha.strip() for linha in f)

    def salvar_arquivo_extraido(self, nome_arquivo):
        with open(ARQUIVO_CONTROLE, "a", encoding="utf-8") as f:
            f.write(f"{nome_arquivo}\n")

    def extrair_arquivos_rar(self):
        try:
            arquivos_existentes = [f for f in os.listdir(PASTA_RAR) if f.endswith(".exe")]
            extraidos = self.carregar_lista_extraidos()

            for arquivo in os.listdir(PASTA_RAR):
                if arquivo.lower().endswith(".rar") and arquivo not in extraidos:
                    caminho_rar = os.path.join(PASTA_RAR, arquivo)
                    try:
                        with rarfile.RarFile(caminho_rar) as rf:
                            rf.extractall(PASTA_RAR)
                            print(f"Extraído: {arquivo}")
                            self.salvar_arquivo_extraido(arquivo)
                            # renomeia EXEs extraídos
                            for item in os.listdir(PASTA_RAR):
                                if item.endswith(".exe") and item not in arquivos_existentes:
                                    caminho_exe = os.path.join(PASTA_RAR, item)
                                    versao = self.obter_versao_arquivo(caminho_exe)
                                    if versao:
                                        novo_nome = f"{item.split('.')[0]}_{versao}.exe"
                                        os.replace(caminho_exe, os.path.join(PASTA_RAR, novo_nome))
                                        print(f"Renomeado: {item} -> {novo_nome}")
                    except rarfile.RarCannotExec as e:
                        print(f"Erro ao extrair {arquivo}: {e}")
                elif arquivo.lower().endswith(".rar"):
                    print(f"Ignorado (já extraído): {arquivo}")
        except Exception as e:
            print(f"Erro ao acessar a pasta de arquivos RAR: {e}")

    def obter_versao_arquivo(self, caminho_arquivo):
        try:
            info = win32api.GetFileVersionInfo(caminho_arquivo, "\\")
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            return f"{ms >> 16}.{ms & 0xFFFF}.{ls >> 16}.{ls & 0xFFFF}"
        except:
            return None

    def mover_arquivos(self):
        try:
            for arquivo in os.listdir(PASTA_RAR):
                if "MAX_Manager" in arquivo and arquivo.endswith(".exe"):
                    shutil.move(os.path.join(PASTA_RAR, arquivo), os.path.join(PASTA_VERSOES, arquivo))
                elif "MAX_Atualiza" in arquivo and arquivo.endswith(".exe"):
                    shutil.move(os.path.join(PASTA_RAR, arquivo), os.path.join(PASTA_ATUALIZAR, arquivo))
            # limpa restos de EXEs
            for arquivo in os.listdir(PASTA_RAR):
                if arquivo.lower().endswith(".exe"):
                    os.remove(os.path.join(PASTA_RAR, arquivo))
        except Exception as e:
            print(f"Erro ao mover arquivos: {e}")

    def renomear_arquivos_versao(self):
        for pasta, prefixo in [(PASTA_VERSOES, "M"), (PASTA_ATUALIZAR, "T")]:
            for arquivo in os.listdir(pasta):
                if arquivo.endswith(".exe"):
                    caminho = os.path.join(pasta, arquivo)
                    versao = self.obter_versao_arquivo(caminho)
                    if versao:
                        versao = versao[4:]  # remove primeiros 4 caracteres
                        novo_nome = f"{prefixo}_{versao}.exe"
                        os.replace(caminho, os.path.join(pasta, novo_nome))

    # ================= PROCESSO COMPLETO =================
    def processar_versoes(self):
        self.extrair_arquivos_rar()
        self.mover_arquivos()
        self.renomear_arquivos_versao()
        self.atualizar_interface()

    def abrir_pasta_versoes(self):
        try:
            os.makedirs(PASTA_VERSOES, exist_ok=True)
            if sys.platform.startswith("win"):
                os.startfile(PASTA_VERSOES)
            else:
                subprocess.Popen(["xdg-open", PASTA_VERSOES])
        except Exception as e:
            QMessageBox.critical(None, "Erro ao abrir pasta", str(e))

    # ================= SELETOR BANCO =================
    def abrir_seletor_banco(self):
        dialog = QDialog()
        dialog.setWindowTitle("Selecionar Banco")
        dialog.resize(300, 400)

        layout = QVBoxLayout(dialog)
        titulo = QLabel("Selecione o banco de dados")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-weight: bold;")
        layout.addWidget(titulo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        cont = QWidget()
        vbox = QVBoxLayout(cont)
        vbox.setAlignment(Qt.AlignTop)

        for banco in self.listar_bancos():
            btn = QPushButton(banco)
            btn.clicked.connect(lambda _, b=banco: self._selecionar_banco(b, dialog))
            vbox.addWidget(btn)

        scroll.setWidget(cont)
        layout.addWidget(scroll)
        dialog.exec()

    def _selecionar_banco(self, banco, dialog):
        self.alterar_ini(banco, "(local)")
        versao = self.buscar_versao_banco(banco)
        self.ui.lversao.setText(f"Versão: {versao}")
        dialog.accept()

    # ================= EXECUÇÃO VERSÕES =================

    def copiar_e_executar(self, origem_exe):
        try:
            if not os.path.exists(origem_exe):
                QMessageBox.warning(None, "Arquivo não encontrado", origem_exe)
                return

            nome = os.path.basename(origem_exe)
            destino = os.path.join(PASTA_PRINCIPAL, nome)

            # verifica se o processo já está rodando
            processo_rodando = any(
                p.info['name'].lower() == nome.lower()
                for p in psutil.process_iter(['name'])
            )

            if not processo_rodando:
                # só copia se não estiver rodando
                shutil.copy2(origem_exe, destino)

            # executa sempre
            subprocess.Popen([destino], cwd=PASTA_PRINCIPAL, shell=False)

        except Exception as e:
            QMessageBox.critical(None, "Erro ao executar", str(e))


    # ================= LISTAR E ATUALIZAR =================
    def listar(self, pasta):
        if not os.path.exists(pasta):
            return []
        return sorted(f for f in os.listdir(pasta) if f.lower().endswith(".exe"))

    def atualizar_interface(self):
        self._limpar_layout(self.layout_manager)
        self._limpar_layout(self.layout_atualiza)
        for exe in self.listar(PASTA_VERSOES):
            caminho = os.path.join(PASTA_VERSOES, exe)
            btn = QPushButton(exe)
            btn.clicked.connect(lambda _, p=caminho: self.copiar_e_executar(p))
            self.layout_manager.addWidget(btn)
        for exe in self.listar(PASTA_ATUALIZAR):
            caminho = os.path.join(PASTA_ATUALIZAR, exe)
            btn = QPushButton(exe)
            btn.clicked.connect(lambda _, p=caminho: self.copiar_e_executar(p))
            self.layout_atualiza.addWidget(btn)
