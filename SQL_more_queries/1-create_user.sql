-- This script creates the MySQL server user user_0d_1 with all privileges
-- and sets the password to user_0d_1_pwd. If the user already exists,
-- the script will not fail.

-- Create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to ensure that all changes are applied
FLUSH PRIVILEGES;
