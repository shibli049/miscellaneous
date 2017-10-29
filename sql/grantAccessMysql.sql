#grant all privilieges to root from local host
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;

#grant all privilieges to root from a specific ip 192.168.100.254
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.100.254' WITH GRANT OPTION;

#grant all privilieges to root from any host
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

#Exit MySQL
exit