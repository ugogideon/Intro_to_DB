-- This script retrieves the full description of the books table from the specified database

-- Use the database provided as an argument
USE alx_book_store;

-- Query to get the table structure
SELECT 
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Column Type',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_DEFAULT AS 'Default Value',
    COLUMN_KEY AS 'Key',
    EXTRA AS 'Extra'
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_NAME = 'Books'
    AND TABLE_SCHEMA = 'alx_book_store';
