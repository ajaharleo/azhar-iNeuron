use banking;
create table salaries(depname varchar(30), empno int, salary int);
insert into salaries values('develop',11,5200),
('develop',7,4300),
('develop',9,4500),('develop',8,6000),('develop',10,5200),
('personal',5,3500),('personal',2,3900),
('sales',3,4800),('sales',1,5000),('sales',4,4800);
select empno from salaries order by salary desc limit 1;