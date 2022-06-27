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
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `codewars2` DEFAULT CHARACTER SET utf8mb3 ;
USE `codewars2` ;

CREATE TABLE IF NOT EXISTS `codewars2`.`cargos` (
  `codigo` CHAR(2) NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  `salario_base` FLOAT NOT NULL,
  `comissao` FLOAT NULL DEFAULT '0',
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

CREATE TABLE IF NOT EXISTS `codewars2`.`funcionarios` (
  `matricula` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `cpf` CHAR(11) NOT NULL,
  `data_admissao` DATE NOT NULL,
  `cargos_codigo` CHAR(2) NOT NULL,
  `comissao` TINYINT NOT NULL DEFAULT '0',
  PRIMARY KEY (`matricula`),
  INDEX `fk_funcionarios_cargos_idx` (`cargos_codigo` ASC) VISIBLE,
  CONSTRAINT `fk_funcionarios_cargos`
    FOREIGN KEY (`cargos_codigo`)
    REFERENCES `mydb`.`cargos` (`codigo`))
ENGINE = InnoDB
AUTO_INCREMENT=100000
DEFAULT CHARACTER SET = utf8mb3;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
"""

cursor.execute(criar_tabelas)
cursor.close()
cnx.close()