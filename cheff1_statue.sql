-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cheff1
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `statue`
--

DROP TABLE IF EXISTS `statue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `statue` (
  `statusId` int(11) NOT NULL,
  `statu` varchar(18) NOT NULL,
  PRIMARY KEY (`statusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statue`
--

LOCK TABLES `statue` WRITE;
/*!40000 ALTER TABLE `statue` DISABLE KEYS */;
INSERT INTO `statue` VALUES (1,'Finished'),(2,'Disqualified'),(3,'Accident'),(4,'Collision'),(5,'Engine'),(6,'Gearbox'),(7,'Transmission'),(8,'Clutch'),(9,'Hydraulics'),(10,'Electrical'),(11,'+1 Lap'),(12,'+2 Laps'),(13,'+3 Laps'),(14,'+4 Laps'),(15,'+5 Laps'),(16,'+6 Laps'),(17,'+7 Laps'),(18,'+8 Laps'),(19,'+9 Laps'),(20,'Spun off'),(21,'Radiator'),(22,'Suspension'),(23,'Brakes'),(24,'Differential'),(25,'Overheating'),(26,'Mechanical'),(27,'Tyre'),(28,'Driver Seat'),(29,'Puncture'),(30,'Driveshaft'),(31,'Retired'),(32,'Fuel pressure'),(33,'Front wing'),(34,'Water pressure'),(35,'Refuelling'),(36,'Wheel'),(37,'Throttle'),(38,'Steering'),(39,'Technical'),(40,'Electronics'),(41,'Broken wing'),(42,'Heat shield fire'),(43,'Exhaust'),(44,'Oil leak'),(45,'+11 Laps'),(46,'Wheel rim'),(47,'Water leak'),(48,'Fuel pump'),(49,'Track rod'),(50,'+17 Laps'),(51,'Oil pressure'),(53,'+13 Laps'),(54,'Withdrew'),(55,'+12 Laps'),(56,'Engine fire'),(58,'+26 Laps'),(59,'Tyre puncture'),(60,'Out of fuel'),(61,'Wheel nut'),(62,'Not classified'),(63,'Pneumatics'),(64,'Handling'),(65,'Rear wing'),(66,'Fire'),(67,'Wheel bearing'),(68,'Physical'),(69,'Fuel system'),(70,'Oil line'),(71,'Fuel rig'),(72,'Launch control'),(73,'Injured'),(74,'Fuel'),(75,'Power loss'),(76,'Vibrations'),(77,'107% Rule'),(78,'Safety'),(79,'Drivetrain'),(80,'Ignition'),(81,'Did not qualify'),(82,'Injury'),(83,'Chassis'),(84,'Battery'),(85,'Stalled'),(86,'Halfshaft'),(87,'Crankshaft'),(88,'+10 Laps'),(89,'Safety concerns'),(90,'Not restarted'),(91,'Alternator'),(92,'Underweight'),(93,'Safety belt'),(94,'Oil pump'),(95,'Fuel leak'),(96,'Excluded'),(97,'Did not prequalify'),(98,'Injection'),(99,'Distributor'),(100,'Driver unwell'),(101,'Turbo'),(102,'CV joint'),(103,'Water pump'),(104,'Fatal accident'),(105,'Spark plugs'),(106,'Fuel pipe'),(107,'Eye injury'),(108,'Oil pipe'),(109,'Axle'),(110,'Water pipe'),(111,'+14 Laps'),(112,'+15 Laps'),(113,'+25 Laps'),(114,'+18 Laps'),(115,'+22 Laps'),(116,'+16 Laps'),(117,'+24 Laps'),(118,'+29 Laps'),(119,'+23 Laps'),(120,'+21 Laps'),(121,'Magneto'),(122,'+44 Laps'),(123,'+30 Laps'),(124,'+19 Laps'),(125,'+46 Laps'),(126,'Supercharger'),(127,'+20 Laps'),(128,'+42 Laps'),(129,'Engine misfire'),(130,'Collision damage'),(131,'Power Unit'),(132,'ERS'),(133,'+49 Laps'),(134,'+38 Laps'),(135,'Brake duct'),(136,'Seat');
/*!40000 ALTER TABLE `statue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-18 11:03:13
