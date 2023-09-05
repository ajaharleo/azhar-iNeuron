use banking;
CREATE TABLE user_activity(user_id int, activity_date date, activity_type varchar(20));

INSERT INTO user_activity VALUES(3,'2022-08-15','click'),
(2,'2022-08-14','click'),(3,'2022-08-15','login'),(2,'2022-08-14','login'),
(3,'2022-08-15','click'),(1,'2022-08-13',''),(3,'2022-08-16','purchase'),
(2,'2022-08-13','click'),(3,'2022-08-14',''),(2,'2022-08-14','purchase');

SELECT
    activity_date,
    ROUND(
        (COUNT(DISTINCT CASE WHEN activity_type 
        IN ('click', 'login', 'purchase') THEN user_id END) / COUNT(DISTINCT user_id)) * 100,2) 
        AS engagement_rate
FROM user_activity GROUP BY activity_date ORDER BY activity_date;

SELECT * FROM user_activity;
