CREATE TABLE customers (
    customer_id   INT AUTO_INCREMENT PRIMARY KEY,
    first_name    VARCHAR(100) NOT NULL,
    last_name     VARCHAR(100) NOT NULL,
    phone         VARCHAR(20),
    email         VARCHAR(255),
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vehicles (
    vehicle_id    INT AUTO_INCREMENT PRIMARY KEY,
    customer_id   INT NOT NULL,
    make          VARCHAR(100) NOT NULL,
    model         VARCHAR(100) NOT NULL,
    year          INT,
    vin           VARCHAR(50) UNIQUE,
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE service_records (
    service_id    INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id    INT NOT NULL,
    service_date  DATE NOT NULL,
    description   TEXT,
    cost          DECIMAL(10,2),
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
);

-- Insert sample customers
INSERT INTO customers (first_name, last_name, phone, email) VALUES
('Alice', 'Johnson', '555-0101', 'alice.j@example.com'),
('Bob', 'Smith',     '555-0202', 'bob.s@example.com'),
('Carol', 'Nguyen',  '555-0303', 'carol.n@example.com');

-- Insert sample vehicles
INSERT INTO vehicles (customer_id, make, model, year, vin) VALUES
(1, 'Toyota', 'Camry', 2018, 'JTNB11HK0K3000001'),
(1, 'Honda',  'Civic', 2020, '2HGFC2F69LH500002'),
(2, 'Ford',   'F-150', 2015, '1FTFW1E5XJFB00003'),
(3, 'Tesla',  'Model 3',2022, '5YJ3E1EA7JF000004');

-- Insert sample service records
INSERT INTO service_records (vehicle_id, service_date, description, cost) VALUES
(1, CURDATE() - INTERVAL 5 DAY,  'Oil change; tire rotation',    89.99),
(2, CURDATE() - INTERVAL 15 DAY, 'Brake pad replacement',       320.00),
(3, CURDATE() - INTERVAL 45 DAY, 'Transmission service',        1200.00),
(4, CURDATE() - INTERVAL 2 DAY,  'Software update; inspection', 0.00),
(1, CURDATE() - INTERVAL 60 DAY, 'Battery replacement',         180.00);

-- Query: find all vehicles serviced in the last 30 days
SELECT
  v.vehicle_id,
  v.make,
  v.model,
  v.year,
  v.vin,
  c.customer_id,
  c.first_name,
  c.last_name,
  s.service_id,
  s.service_date,
  s.description,
  s.cost
FROM service_records s
JOIN vehicles v ON s.vehicle_id = v.vehicle_id
JOIN customers c ON v.customer_id = c.customer_id
WHERE s.service_date >= CURDATE() - INTERVAL 30 DAY
ORDER BY s.service_date DESC;