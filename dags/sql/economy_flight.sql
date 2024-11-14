CREATE TABLE IF NOT EXISTS economic_flight (
    date DATE,
    airline VARCHAR(50),
    ch_code VARCHAR(10),
    num_code INTEGER,
    dep_time TIME,
    "from" VARCHAR(50),
    time_taken VARCHAR(10),
    stop VARCHAR(10),
    arr_time TIME,
    "to" VARCHAR(50),
    price INTEGER,
    class VARCHAR(10)
);
