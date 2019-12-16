import pymysql
import os


#____________________________________________________________________#
host='localhost'
user='root'
password='shadow72'
#______________________________________________________________________#


em_csv = r"C:\\Users\\user\\Desktop\\program\\F1chef\\csv\\export"

print("Exportation des csvs, let's go !! ")

con = pymysql.connect(host=host,
                       password=password,
                       user=user,
                       autocommit=True,
                       local_infile=1)
print("Connection BDD {}".format(host))

cursor=con.cursor()

print("Attributs des droits")
load_sql='SET GLOBAL local_infile=1'
cursor.execute(load_sql)

#_________________________________________________________________________#

load_sql ="DROP DATABASE IF EXISTS BDD_PYTHON;"
cursor.execute(load_sql)

print("Creation de la base de donnée !!, BDD_PYTHON")

load_sql = "CREATE DATABASE BDD_PYTHON"
cursor.execute(load_sql)

print('base de donnée créée')

load_sql='USE BDD_PYTHON'
cursor.execute(load_sql)

print('Création de la table : resultats')

load_sql="""CREATE TABLE resultats(
   raceId               VARCHAR(45)
  ,piloteId             VARCHAR(45)
  ,numb                 VARCHAR(45)
  ,grid                 VARCHAR(45)
  ,post                 VARCHAR(45)
  ,positionText         VARCHAR(45)
  ,positionOrder        VARCHAR(45)
  ,points               VARCHAR(45)
  ,laps                 VARCHAR(45)
  ,temps                VARCHAR(45)
  ,fastestLap           VARCHAR(45)
  ,level                VARCHAR(45)
  ,fastestLapTime       VARCHAR(45)
  ,fastestLapSpeed      VARCHAR(45)
  ,statusId             VARCHAR(45)
  ,constructorResultsId VARCHAR(45)
  ,qualifyId            VARCHAR(45)
  ,statsId              VARCHAR(45));"""


cursor.execute(load_sql)

#____________________________________________________________________#

print("Intégrations des données ")

phrase=str(em_csv)+"/resultatslFinal.csv"
load_sql="LOAD DATA LOCAL INFILE'"+str(phrase)+"' INTO TABLE resultats FIELDS TERMINATED BY '\t'"
cursor.execute(load_sql)


#_______________________________________________________________________#______#

print('Création de la table : pilote')

load_sql=""" CREATE TABLE pilote (
  `Id` VARCHAR(45),
  `piloteId` VARCHAR(45) PRIMARY KEY,
  `driverRef` VARCHAR(45),
  `number_id` VARCHAR(45),
  `code` VARCHAR(45),
  `forename` VARCHAR(45),
  `surname` VARCHAR(45),
  `dob` VARCHAR(45),
  `nationality` VARCHAR(45),
  `id_statues` VARCHAR(45)); """

cursor.execute(load_sql)

#______________________________________________________________________________#
print("Intégrations des données ")

phrase=str(em_csv)+"/pilotefinal2.csv"
load_sql="LOAD DATA LOCAL INFILE'"+str(phrase)+"' INTO TABLE pilote FIELDS TERMINATED BY ';' IGNORE 1 ROWS"
cursor.execute(load_sql)

#_____________________________________________________________________________#

print('Création de la table : qualif')

load_sql=""" CREATE TABLE qualif(
   Id            VARCHAR(45) PRIMARY KEY
  ,raceId        VARCHAR(45)
  ,driverId      VARCHAR(45)
  ,constructorId VARCHAR(45)
  ,number        VARCHAR(45)
  ,position      VARCHAR(45)
  ,q1            VARCHAR(45)
  ,q2            VARCHAR(45)
  ,q3            VARCHAR(45)
); """

cursor.execute(load_sql)

#________________________________________________________________________________#


print("Intégrations des données ")

phrase=str(em_csv)+"/QUALIFfinal.csv"
load_sql="LOAD DATA LOCAL INFILE'"+str(phrase)+"' INTO TABLE qualif FIELDS TERMINATED BY '\t' IGNORE 1 ROWS"
cursor.execute(load_sql)


#___________________________________________________________________________________#

print('Création de la table : control')

load_sql=""" CREATE TABLE control(
   Id                   VARCHAR(45) PRIMARY KEY
  ,constructorResultsId VARCHAR(45)
  ,raceId               VARCHAR(45)
  ,constructorId        VARCHAR(45)
  ,points               VARCHAR(45)
); """

cursor.execute(load_sql)

#_______________________________________________________________________________#

print("Intégrations des données ")

phrase=str(em_csv)+"/controlFinal.csv"
load_sql="LOAD DATA LOCAL INFILE'"+str(phrase)+"' INTO TABLE control FIELDS TERMINATED BY ';' IGNORE 1 ROWS"
cursor.execute(load_sql)

#______________________________________________________________________________#

print('Création de la table : standing')

load_sql=""" CREATE TABLE standing(
   Id           VARCHAR(45) PRIMARY KEY
  ,raceId       VARCHAR(45)
  ,driverId     VARCHAR(45)
  ,points       NUMERIC(5,2)
  ,position     VARCHAR(45)
  ,positionText VARCHAR(45)
  ,wins         VARCHAR(45)
); """

cursor.execute(load_sql)


#______________________________________________________________________________#

print("Intégrations des données ")

phrase=str(em_csv)+"/standingfinal.csv"
load_sql="LOAD DATA LOCAL INFILE'"+str(phrase)+"' INTO TABLE standing FIELDS TERMINATED BY '\t' IGNORE 1 ROWS"
cursor.execute(load_sql)


#______________________________________________________________________________#

print('Création de la table : circuits')

load_sql="""CREATE TABLE IF NOT EXISTS circuits (
    `circuitId` VARCHAR(45),
    `circuitRef` VARCHAR(45),
    `name` VARCHAR(45),
    `location` VARCHAR(45),
    `country` VARCHAR(45),
    `lat` NUMERIC(7, 5),
    `lng` NUMERIC(9, 6),
    `alt` VARCHAR(45),
    `url` VARCHAR(45)
); """

cursor.execute(load_sql)
#_______________________________________________________________________________#



print("Intégrations des données ")
phrase=str(em_csv)+"/circuitfinal.csv"
load_sql="LOAD DATA LOCAL INFILE'"+str(phrase)+"' INTO TABLE circuits FIELDS TERMINATED BY ';' IGNORE 1 ROWS"
cursor.execute(load_sql)


#______________________________________________________________________________#

print("Début de la connexion entre les table")

load_sqls="""ALTER TABLE pilote
            ADD FOREIGN KEY (piloteId) REFERENCES resultats(piloteId);"""
cursor_execute(load_sqls)

print("Connected : pilote")

load_sqls="""ALTER TABLE qualif
            ADD FOREIGN KEY (Id) REFERENCES resultats(qualifyId);"""

cursor_execute(load_sqls)

print("Connected : qualif")

load_sqls="""ALTER TABLE standing
            ADD FOREIGN KEY (Id) REFERENCES resultats(statsId);"""

cursor_execute(load_sqls)

print("Connected : standing")

load_sqls="""ALTER TABLE control
            ADD FOREIGN KEY (constructorResultsId) REFERENCES resultats(constructorResultsId);"""

cursor_execute(load_sqls)

print("Connected : control")


load_sqls="""ALTER TABLE circuits
            ADD FOREIGN KEY (raceId) REFERENCES resultats(raceId);"""

cursor_execute(load_sqls)

print("Connected : circuits")

#_________________________________________________________________________________________#
