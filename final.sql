use cheff1;

USE cheff1;

ALTER TABLE circuits CHANGE circuitId Id INT(11) PRIMARY KEY;
ALTER TABLE pilote CHANGE FIELD1 Id INT(11);
ALTER TABLE qualif CHANGE FIELD1 Id INT(11);
ALTER TABLE control CHANGE FIELD1 Id INT(11);
ALTER TABLE standing CHANGE FIELD1 Id INT(11);
ALTER TABLE statue CHANGE statusId Id INT(11);
ALTER TABLE resultats CHANGE driverId piloteId INT(11);
ALTER TABLE pilote CHANGE number number_id INT(11);


#Agrémentation 

ALTER TABLE pilote
ADD FOREIGN KEY (Id) REFERENCES resultats(piloteId);



MERGE INTO standing USING control
ON driverStandingsId WHEN MATCHED THEN
UPDATE SET standing.driverStandingId = control.constructorResultsId
DELETE control;


SELECT * FROM pilote, circuits, resultats;

ALTER TABLE resultats
ADD FOREIGN KEY resultats(raceId) REFERENCES pilote(Id);
