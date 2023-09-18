DROP TABLE IF EXISTS Location;
CREATE TABLE Location (
    locationId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS Status;
CREATE TABLE Status (
    statusID INT AUTO_INCREMENT PRIMARY KEY,
    statusCode VARCHAR(255) NOT NULL
);

INSERT INTO Status (statusCode)
VALUES ('FULFILLED');

INSERT INTO Status (statusCode)
VALUES ('PENDING');

INSERT INTO Location (name)
VALUES ('Seattle');

INSERT INTO Location (name)
VALUES ('Kirkland');

DROP TABLE IF EXISTS Equipment;
CREATE TABLE Equipment (
    equipId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    statusId INT NOT NULL,
    locationId INT NOT NULL,
    FOREIGN KEY (statusId) REFERENCES Status(statusId),
    FOREIGN KEY (locationId) REFERENCES Location(locationId)
);

INSERT INTO Equipment (name, description, statusId, locationId)
VALUES ('Masks', 'surgical masks', 1, 1);

INSERT INTO Equipment (name, description, statusId, locationId)
VALUES ('Gloves', 'surgical gloves', 2, 2);

