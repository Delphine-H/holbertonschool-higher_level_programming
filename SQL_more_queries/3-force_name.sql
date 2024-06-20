-- Script to create table force_name if it doesn't exist

-- Check if the table force_name exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

-- This line ensures that the table will have the two columns and their requirements
