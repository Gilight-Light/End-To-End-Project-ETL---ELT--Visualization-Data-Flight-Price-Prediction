CREATE TABLE IF NOT EXISTS cleandata_flight (
    date DATE,
    airline VARCHAR(50),
    flight VARCHAR(50),
    source_city VARCHAR(100),
    departure_time VARCHAR(50),
    stops VARCHAR(50),
    arrival_time VARCHAR(50),
    destination_city VARCHAR(100),
    class VARCHAR(50),
    duration DECIMAL(5, 2),
    days_left INT,
    price DECIMAL(10, 2)
);