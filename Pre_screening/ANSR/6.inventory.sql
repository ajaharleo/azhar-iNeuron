use banking;
CREATE TABLE inventory(product_id int, warehouse_id int, date_ date, quantity int);

INSERT INTO inventory 
values(1,11,'2023-08-21',123),
(1,12,'2023-08-21',220),(1,13,'2023-08-21',50),(1,14,'2023-08-21',320),(1,12,'2023-08-22',290),
(2,12,'2023-08-21',20),(2,11,'2023-08-21',160),(2,14,'2023-08-21',220),(2,13,'2023-08-22',500),
(3,12,'2023-08-21',470),(3,13,'2023-08-21',40),(3,14,'2023-08-21',720),(3,12,'2023-08-22',330),
(2,12,'2023-08-22',440),(1,13,'2023-08-22',690),(1,14,'2023-08-22',350),(2,12,'2023-08-22',310),
(3,11,'2023-08-21',220),(2,14,'2023-08-22',50),(3,14,'2023-08-21',320),(3,12,'2023-08-22',290);

SELECT * FROM inventory;

SELECT product_id, warehouse_id, SUM(quantity) AS total_quantity FROM inventory inven JOIN
(SELECT product_id, warehouse_id, MAX(date) AS latest_date FROM inventory
     GROUP BY product_id, warehouse_id) latest
     ON inven.product_id = latest.product_id
     AND inven.warehouse_id = latest.product_id
     AND inven.date_ = latest.latest_date
     GROUP BY product_id, warehouse_id;
SELECT * FROM inventory;