import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

cnx = mysql.connector.connect(
    host=os.getenv('HOST'),
    database=os.getenv('NAME'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    port=os.getenv('PORT'),
)

cursor = cnx.cursor()

insert_query = "INSERT INTO codewars2.cargos(codigo, descricao, salario_base, comissao) VALUES (%s,%s,%s,%s)"
insert_records = [('10', 'Cientista de Dados', '10200', '0.1'),
                  ('20', 'Especialista em Business Intelligence', '7000', '0.08'),
                  ('30', 'Desenvolvedor Mobile Sênior', '6700', '0.07'),
                  ('31', 'Desenvolvedor Mobile Pleno', '3550', '0.06'),
                  ('32', 'Desenvolvedor Júnior', '3000', '0.03'),
                  ('50', 'Gerente de Projeto', '8900', '0.08')]

cursor.executemany(insert_query, insert_records)
cnx.commit()

cursor.close()
cnx.close()
