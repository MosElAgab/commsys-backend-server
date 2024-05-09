-- \c test_commsys

-- delete data
DELETE FROm counterparty;
DELETE FROM staff;
DELETE FROM department;
DELETE FROM currency;
DELETE FROM payment_type;
DELETE FROM address;
DELETE FROM design;


-- design

ALTER SEQUENCE design_design_id_seq RESTART WITH 1;

INSERT INTO design
    (design_name, file_location, file_name)
VALUES
    ('apple0001', '/design/apple', 'apple0001.csv'),
    ('apple0002', '/design/apple', 'apple0002.csv'),
    ('apple0003', '/design/apple', 'apple0003.csv'),
    ('apple0004', '/design/apple', 'apple0004.csv'),
    ('apple0005', '/design/apple', 'apple0005.csv');

SELECT * FROM design;


-- address

ALTER SEQUENCE address_address_id_seq RESTART WITH 1;

INSERT INTO address
    (first_line, second_line, district, city, postal_code, country, phone)
Values
    ('33 London Rd', 'South London', NULL, 'London', 'LN6 1BS', 'United Kingdom', '01214356900'),
    ('20 Manchester Rd', 'South Liverpool', NULL, 'Liverpool', 'L3 1WS', 'United Kingdom', '01314356911'),
    ('101 King Rd', 'South Manchester', NULL, 'Manchester', 'M23 1FB', 'United Kingdom', '01614356900'),
    ('1 Queens Rd', 'Northh London', NULL, 'London', 'L8 4SZ', 'United Kingdom', '04214356944'),
    ('648 Princess Rd', 'East Leicester', NULL, 'Leicester', 'LE1 1AA', 'United Kingdom', '01714356955');

SELECT * FROM address;


-- payment_type

ALTER SEQUENCE payment_type_payment_type_id_seq RESTART WITH 1;

INSERT INTO payment_type
    (payment_type_name)
Values
    ('Debit Card'),
    ('Cash'),
    ('Credit Card'),
    ('Online'),
    ('Bitcoin');

SELECT * FROM payment_type;


-- currency

ALTER SEQUENCE currency_currency_id_seq RESTART WITH 1;

INSERT INTO currency
    (currency_code)
Values
    ('USD'),
    ('GBP'),
    ('BTC'),
    ('EUR'),
    ('SOL');


SELECT * FROM currency;


-- department

ALTER SEQUENCE department_department_id_seq RESTART WITH 1;


INSERT INTO department
    (department_name, location, manager)
Values
    ('Human Resources', 'Manchester', 'Alex'),
    ('IT', 'London', 'Ali'),
    ('Finance', 'Leicester', 'Ahmed'),
    ('Marketing', 'Liverpool', 'Jhon'),
    ('Production', 'Manchester', 'Mike');


SELECT * FROM department;


-- staff

ALTER SEQUENCE staff_staff_id_seq RESTART WITH 1;

INSERT INTO staff
    (first_name, last_name, department_id, email_address)
Values
    ('Alex', 'Jones', 3, 'alex.jones@commsys.com'),
    ('Ali', 'Alias', 1, 'ali.alias@commsys.com'),
    ('Ahmed', 'Mokhtar', 4, 'ahmed.mokhtar@commsys.com'),
    ('Jhon', 'Stones', 1, 'jhon.stones@commsys.com'),
    ('Mike', 'Tyson', 5, 'mike.tyson@commsys.com');


SELECT * FROM staff;

-- counterparty

ALTER SEQUENCE counterparty_counterparty_id_seq RESTART WITH 1;

INSERT INTO counterparty
    (counterparty_legal_name, legal_address_id, commercial_contact, delivery_contact)
Values
    ('OpSec', 3, 'Alex Becker', 'Orcal Del'),
    ('Firwa N LTD', 1, 'Mario Butter', 'Panda'),
    ('Utorrent', 2, 'Donner kebabs', 'Mercury'),
    ('Zooma', 3, 'Spring Water', 'Tea Cup'),
    ('KeyBoard group', 5, 'Init alppy', 'BiggarPic');


SELECT * FROM staff;