CREATE DATABASE  IF NOT EXISTS `xpto` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `xpto`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: xpto
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cargo`
--

DROP TABLE IF EXISTS `cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cargo` (
  `codigo` varchar(6) NOT NULL,
  `descricao` varchar(40) NOT NULL,
  `salario_base` varchar(10) NOT NULL,
  `comissao` varchar(5) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo`
--

LOCK TABLES `cargo` WRITE;
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT INTO `cargo` VALUES ('10','Cientista de Dados','10200','0.1'),('20','Especialista em Business Intelligence','7000','0.08'),('30','Desenvolvedor Mobile Senior','6700','0.07'),('31','Desenvolvedor Mobile Pleno','3550','0.06'),('32','Desenvolvedor Junior','3000','0.03'),('50','Gerente de Projetos',' 8900','0.08');
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `matricula` char(10) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `cpf` char(20) NOT NULL,
  `data_admissao` datetime(6) NOT NULL,
  `cargo` varchar(40) NOT NULL,
  `comissao` varchar(3) NOT NULL,
  `cargo_codigo` varchar(2) NOT NULL,
  PRIMARY KEY (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
INSERT INTO `funcionario` VALUES ('111111','Ana Maria Silva','11111111100','2019-12-07 00:00:00.000000','Desenvolvedor Junior','Sim','32'),('222222','Bernardo Santos','22222222200','2017-10-16 00:00:00.000000','Especialista em Bussiness Intellignte','Nao','20'),('333333','Diana Santana de Sousa','33333333300','2002-04-16 00:00:00.000000','Desenolvedor Mobile Senior','Sim','30'),('444444','Felipe Cruz','44444444400','2021-06-28 00:00:00.000000','Desenolvedor Mobile Pleno','Sim','31'),('555555','Daniel Ferreira','55555555500','2009-08-14 00:00:00.000000','Desenolvedor Junior','Nao','32'),('666666','Joana Silveira Pacheco','66666666600','2009-08-14 00:00:00.000000','Gerente de Projetos','Sim','50');
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `holerite`
--

DROP TABLE IF EXISTS `holerite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `holerite` (
  `matricula` varchar(6) NOT NULL,
  `salario_base` varchar(15) NOT NULL,
  `comissao` varchar(5) NOT NULL,
  `faltas` varchar(2) NOT NULL,
  `descontos` varchar(9) NOT NULL,
  `salario_bruto` varchar(10) NOT NULL,
  `mes` varchar(2) NOT NULL,
  `ano` varchar(4) NOT NULL,
  `INSS` varchar(5) NOT NULL,
  `IRRF` varchar(5) NOT NULL,
  PRIMARY KEY (`matricula`,`ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holerite`
--

LOCK TABLES `holerite` WRITE;
/*!40000 ALTER TABLE `holerite` DISABLE KEYS */;
INSERT INTO `holerite` VALUES ('111111','3000','0.03','2','537.77','2552.23','4','2022','3','0.075'),('222222','7000','0.08','0','1646.93','5913.07','4','2022','4','0.275'),('333333','6700','0.07','0','1534.41','5634.59','4','2022','4','0.275'),('444444','3550','0.06','0','334.98','3428.02','4','2022','3','0.15'),('555555','3000','0.03','0','337.78','2752.22','4','2022','3','0.075'),('666666','8900','0.08','0','2183,77','7428.23','4','2022','4','0.275');
/*!40000 ALTER TABLE `holerite` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-27 21:43:31
