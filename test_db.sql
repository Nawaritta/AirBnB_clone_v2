-- Create the test_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS test_db;

-- Create the hbnb_dev user if it doesn't exist
CREATE USER IF NOT EXISTS 'hb_tst'@'localhost' IDENTIFIED BY 'hb_pwd';

-- Grant privileges to the hbnb_dev user
GRANT ALL PRIVILEGES ON test_db.* TO 'hb_tst'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hb_tst'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Create the 'states' table
USE test_db;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
