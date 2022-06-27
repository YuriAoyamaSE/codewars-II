import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()


def gerar_cnx():
    cnx = mysql.connector.connect(
        host=os.getenv('HOST'),
        database=os.getenv('NAME'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        port=os.getenv('PORT'),
    )
    return cnx


def salvar_commit(cnx):
    cnx.commit()


def fechar_cnx(cnx):
    cnx.close()


def gerar_cursor(cnx):
    return cnx.cursor()


def fechar_cursor(cursor):
    cursor.close()


""""Padrão:

    def funcao(self) -> None:
        cnx = gerar_cnx()
        cursor = gerar_cursor()
        
        salvar_commit()
        fechar_cursor()
        fechar_cnx()
"""