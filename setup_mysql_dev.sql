-- Create or use campus_connect_dev_db database
CREATE DATABASE IF NOT EXISTS campus_connect_dev_db;

-- Create or update user campus_connect_dev
CREATE USER IF NOT EXISTS 'campus_connect_dev'@'localhost' IDENTIFIED BY 'campus_connect_pwd';

-- Grant privileges to campus_connect_dev on campus_connect_dev_db
GRANT ALL PRIVILEGES ON campus_connect_dev_db.* TO 'campus_connect_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to campus_connect_dev
GRANT SELECT ON performance_schema.* TO 'campus_connect_dev'@'localhost';
