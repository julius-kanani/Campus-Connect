-- Create or use campus_connect_test_db database
CREATE DATABASE IF NOT EXISTS campus_connect_test_db;

-- Create or update user campus_connect_test
CREATE USER IF NOT EXISTS 'campus_connect_test'@'localhost' IDENTIFIED BY 'campus_connect_test_pwd';

-- Grant privileges to campus_connect_test on campus_connect_test_db
GRANT ALL PRIVILEGES ON campus_connect_test_db.* TO 'campus_connect_test'@'localhost';

-- Grant SELECT privilege on performance_schema to campus_connect_test
GRANT SELECT ON performance_schema.* TO 'campus_connect_test'@'localhost';
