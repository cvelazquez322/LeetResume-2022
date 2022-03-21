# Write your MySQL query statement below
select a.name as "Employee"
From Employee a
Where a.salary > (select b.salary
                from employee b
                where a.managerID = b.Id);