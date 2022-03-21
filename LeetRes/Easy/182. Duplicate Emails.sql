# Write your MySQL query statement below
select Email 
from Person
GROUP BY Email 
HAVING COUNT(*)> 1;