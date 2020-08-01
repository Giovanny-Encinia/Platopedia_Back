import pandas as pd
from conection.conection import conect_mysql

"""
Creates the Platopedia DataBase
"""

comands = {}
# Create database called PLATOPEDIA
comands["create_database"] = "CREATE DATABASE IF NOT EXISTS PLATOPEDIA;"

# Create Table named GroupFood
comands[
    "GroupFood"
] = """
    USE PLATOPEDIA;
    CREATE TABLE IF NOT EXISTS GroupFood(

    idGroup INT AUTO_INCREMENT NOT NULL,
    NameGroup VARCHAR(45),
    CONSTRAINT pk_idgroup
    PRIMARY KEY(idGroup)

    )ENGINE=InnoDB"""

# Create table named Food
comands[
    "Food"
] = """USE PLATOPEDIA;
    CREATE TABLE IF NOT EXISTS Food(

    idFood INT AUTO_INCREMENT NOT NULL,
    NameFood VARCHAR(45) NOT NULL,
    Group_idGroup INT,
    CONSTRAINT pk_Food
    PRIMARY KEY(idFood),
    CONSTRAINT fk_group_idgroup
    FOREIGN KEY(Group_idGroup) REFERENCES GroupFood(idGroup) ON DELETE CASCADE

    )ENGINE=InnoDB"""

# Create table named Vitamins
comands[
    "Vitamins"
] = """USE PLATOPEDIA;
    CREATE TABLE IF NOT EXISTS Vitamins(

    idVitamins INT AUTO_INCREMENT NOT NULL,
    NameVitamin VARCHAR(45),
    CONSTRAINT pk_idvitamins
    PRIMARY KEY(idVitamins)

    )ENGINE=InnoDB"""

# Create table Food_has_Vitamins

comands[
    "Food_has_Vitamins"
] = """USE PLATOPEDIA;
    CREATE TABLE IF NOT EXISTS Food_has_Vitamins(

    Food_idFood INT,
    Vitamins_idVitamins INT,
    Value FLOAT,
    CONSTRAINT fk_food_idfood FOREIGN KEY(Food_idFood) REFERENCES Food(idFood) ON DELETE CASCADE,
    CONSTRAINT fk_vitamins_idvitamins
    FOREIGN KEY(Vitamins_idVitamins) REFERENCES Vitamins(idVitamins) ON DELETE CASCADE

    )ENGINE=InnoDB"""

# create table Minerals

comands[
    "Minerals"
] = """ USE PLATOPEDIA;
    CREATE TABLE IF NOT EXISTS Minerals(

    idMinerals INT AUTO_INCREMENT NOT NULL,
    NameMineral INT,
    CONSTRAINT pk_idminerals
    PRIMARY KEY(idMinerals)

    )ENGINE=InnoDB"""

comands[
    "Food_has_Minerals"
] = """USE PLATOPEDIA;
    CREATE TABLE IF NOT EXISTS Food_has_Minerals(

    Food_idFood INT,
    Minerals_idMinerals INT,
    Value FLOAT,
    CONSTRAINT fk_food_idfood_m
    FOREIGN KEY(Food_idFood) REFERENCES Food(idFood) ON DELETE CASCADE,
    CONSTRAINT fk_minerals_idminerals
    FOREIGN KEY(Minerals_idMinerals) REFERENCES Minerals(idMinerals) ON DELETE CASCADE

    )ENGINE=InnoDB"""

# create table PrincipalNutriments
comands[
    "PrincipalNutriments"
] = """USE PLATOPEDIA;
    CREATE TABLE IF NOT EXISTS PrincipalNutriments(

    idPrincipalNutriments INT AUTO_INCREMENT NOT NULL,
    NamePrincipalNutriments VARCHAR(45),
    CONSTRAINT pk_idprincipalnutriments
    PRIMARY KEY(idPrincipalNutriments) 

    )ENGINE=InnoDB"""

comands[
    "Food_has_PrincipalNutriments"
] = """USE PLATOPEDIA;
    CREATE TABLE IF NOT EXISTS Food_has_Principal_Nutriments(
    Food_idFood INT,
    PrincipalNutriments_idPrincipalNutriments INT,
    Value FLOAT,
    CONSTRAINT fk_food_idfood_pn
    FOREIGN KEY(Food_idFood) REFERENCES Food(idFood) ON DELETE CASCADE,
    CONSTRAINT fk_principalnutriments_idprincipalnutriments
    FOREIGN KEY(PrincipalNutriments_idPrincipalNutriments) 
    REFERENCES PrincipalNutriments(idPrincipalNutriments) ON DELETE CASCADE
    )ENGINE=InnoDB"""

for comand in comands:
    order = comands[comand]
    database, cursor = conect_mysql()
    cursor.execute(order)
    cursor.close()
    database.close()

