use db;

CREATE TABLE students (
  RegNo VARCHAR(10) PRIMARY KEY,
  Name VARCHAR(255),
  Vaccination_Status VARCHAR(3)
);

INSERT INTO students (RegNo, Name, Vaccination_Status)
VALUES
    ('111111', 'Alice', 'Yes'),
    ('222222', 'Bob', 'No'),
    ('333333', 'Charlie', 'Yes'),
    ('444444', 'David', 'No'),
    ('555555', 'Emma', 'Yes'),
    ('666666', 'Frank', 'No'),
    ('777777', 'Grace', 'Yes'),
    ('888888', 'Henry', 'No'),
    ('999999', 'Isabella', 'Yes'),
    ('100000', 'Jack', 'No');