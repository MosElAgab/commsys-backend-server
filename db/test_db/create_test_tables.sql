\c test_commsys

-- design
DROP TABLE IF EXISTS design;
CREATE TABLE design (
	design_id SERIAL PRIMARY KEY,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	design_name VARCHAR(40) NOT NULL,
	file_location VARCHAR(40) NOT NULL,
	file_name VARCHAR(40) NOT NULL
);
SELECT * FROM design;

-- address
DROP TABLE IF EXISTS address;
CREATE TABLE address (
	address_id SERIAL PRIMARY KEY,
	first_line VARCHAR(40) NOT NULL,
	second_line VARCHAR(40),
	district VARCHAR(40),
	city VARCHAR(40) NOT NULL,
	postal_code VARCHAR(10) NOT NULL,
	country VARCHAR(40) NOT NULL,
	phone VARCHAR(40) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
;
SELECT * FROM address;

-- payment_type
DROP TABLE IF EXISTS payment_type;
CREATE TABLE payment_type (
	payment_type_id SERIAL PRIMARY KEY,
	payment_type_name VARCHAR(40) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
;
SELECT * FROM payment_type;

-- currency
DROP TABLE IF EXISTS currency;
CREATE TABLE currency (
	currency_id SERIAL PRIMARY KEY,
	currency_code VARCHAR(10) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
	
)
;
SELECT * FROM currency;

-- department
DROP TABLE IF EXISTS department;

CREATE TABLE department (
	department_id SERIAL PRIMARY KEY,
	department_name VARCHAR(40) NOT NULL,
	"location" VARCHAR(40),
	manager VARCHAR(40),
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
;
SELECT * FROM department;

-- staff
DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
	staff_id SERIAL PRIMARY KEY,
	first_name VARCHAR(40) NOT NULL,
	last_name VARCHAR(40) NOT NULL,
	department_id INT REFERENCES department(department_id),
	email_address VARCHAR(40) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
;
SELECT * FROM staff;

-- counterparty
DROP TABLE IF EXISTS counterparty;

CREATE TABLE counterparty (
	counterparty_id SERIAL PRIMARY KEY,
	counterparty_legal_name VARCHAR(40) NOT NULL,
	legal_address_id INT REFERENCES address(address_id),
	commercial_contact VARCHAR(40),
	delivery_contact VARCHAR(40),
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP	
)
;
SELECT * FROM counterparty;

-- purchase_order
DROP TABLE IF EXISTS purchase_order;

CREATE TABLE purchase_order (
	purchase_order_id SERIAL PRIMARY KEY,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	staff_id INT REFERENCES staff(staff_id),
	counterparty_id INT REFERENCES counterparty(counterparty_id),
	item_code VARCHAR(40) NOT NULL,
	item_quantity INT NOT NULL,
	item_unit_price FLOAT8 NOT NULL,
	currency_id INT REFERENCES currency(currency_id),
	agreed_delivery_date VARCHAR(40) NOT NULL,
	agreed_payment_date VARCHAR(40) NOT NULL,
	agreed_delivery_location_id INT REFERENCES address(address_id)
)
;
SELECT * FROM purchase_order;

-- sales_order
DROP TABLE IF EXISTS sales_order;
CREATE TABLE sales_order (
	sales_order_id SERIAL PRIMARY KEY,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	design_id INT REFERENCES design(design_id),
	staff_id INT REFERENCES staff(staff_id),
	counterparty_id INT REFERENCES counterparty(counterparty_id),
	unit_sold INT NOT NULL,
	unit_price FLOAT8 NOT NULL,
	currency_id INT REFERENCES currency(currency_id),
	agreed_delivery_date VARCHAR(40) NOT NULL,
	agreed_payment_date VARCHAR(40) NOT NULL,
	agreed_delivery_location_id INT REFERENCES address(address_id)
)
;
SELECT * FROM sales_order;

-- transaction
DROP TABLE IF EXISTS "transaction";
CREATE TABLE "transaction" (
	transaction_id SERIAL PRIMARY KEY,
	transaction_type VARCHAR(40),
	sales_order_id INT REFERENCES sales_order(sales_order_id),
	purchase_order_id INT REFERENCES purchase_order(purchase_order_id),
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
;
SELECT * FROM "transaction";

-- payment
DROP TABLE IF EXISTS payment;

CREATE TABLE payment (
	payment_id SERIAL PRIMARY KEY,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	transaction_id INT REFERENCES transaction(transaction_id),
	counterparty_id INT REFERENCES counterparty(counterparty_id),
	payment_amount NUMERIC NOT NULL,
	currency_id INT REFERENCES currency(currency_id),
	payment_type_id INT REFERENCES payment_type(payment_type_id),
	paid BOOL NOT NULL,
	payment_date VARCHAR NOT NULL,
	company_ac_number INT NOT NULL,
	counter_party_ac_number INT NOT NULL
)
;
SELECT * FROM payment;
