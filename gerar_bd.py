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

criar_tabelas = """
CREATE SCHEMA IF NOT EXISTS `codewars2` DEFAULT CHARACTER SET utf8mb3 ;
USE `codewars2` ;

CREATE TABLE IF NOT EXISTS `codewars2`.`cargos` (
  `codigo` CHAR(2) NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  `salario_base` VARCHAR(15) NOT NULL,
  `comissao` VARCHAR(5) NULL DEFAULT '0',
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

CREATE TABLE IF NOT EXISTS `codewars2`.`funcionarios` (
  `matricula` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `cpf` CHAR(11) NOT NULL,
  `data_admissao` CHAR(10) NOT NULL,
  `cargo` CHAR(2) NOT NULL,
  `comissao` TINYINT NOT NULL DEFAULT '0',
  PRIMARY KEY (`matricula`))
ENGINE = InnoDB
AUTO_INCREMENT=100000
DEFAULT CHARACTER SET = utf8mb3;
"""

cursor.execute(criar_tabelas)
cursor.close()
cnx.close()
