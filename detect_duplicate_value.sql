select column_name, count(*)
from table_name
group by column_name
having count (*) > 1;