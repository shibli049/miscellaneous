-- update column with sequential value in oracle
-- update method one 
UPDATE table_name SET column_name = ROWNUM;
-- update method two
UPDATE table_name set column_name = YOUR_SEQUENCE.nextval;