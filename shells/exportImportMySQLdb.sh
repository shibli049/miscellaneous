#To export database:
mysqldump -u user -p db_name > db_name.sql

#To import database:
#create a database db_name
mysql -u user -p db_name < db_name.sql