-- Script to create table unique_id if it doesn't exist

-- Check if the table unique_id exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- This line ensures that the table will have the two columns and their requirements
