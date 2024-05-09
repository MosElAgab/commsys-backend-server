-- \c test_commsys


-- design

DELETE FROM design;
ALTER SEQUENCE design_design_id_seq RESTART WITH 1;

INSERT INTO design
    (created_at, last_updated, design_name, file_location, file_name)
VALUES
    ('2024-05-01 12:00:00', '2024-05-01 12:00:00', 'apple0001', '/design/apple', 'apple0001.csv'),
    ('2024-05-02 12:00:00', '2024-05-02 12:00:00', 'apple0002', '/design/apple', 'apple0002.csv'),
    ('2024-05-03 12:00:00', '2024-05-03 12:00:00', 'apple0003', '/design/apple', 'apple0003.csv'),
    ('2024-05-04 12:00:00', '2024-05-04 12:00:00', 'apple0004', '/design/apple', 'apple0004.csv'),
    ('2024-05-05 12:00:00', '2024-05-05 12:00:00', 'apple0005', '/design/apple', 'apple0005.csv');

SELECT * FROM design;


-- address

DELETE FROM address;
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

DELETE FROM payment_type;
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

DELETE FROM currency;
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

DELETE FROM department;
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