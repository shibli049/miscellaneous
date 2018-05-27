# create user with connect to localhost by a password 
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'user_password';

# grant all permission on newdatabase to user newuser
GRANT ALL ON newdatabase.* to 'newuser'@'localhost';
