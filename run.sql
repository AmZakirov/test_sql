WITH AGE_TABLE AS (
	SELECT 
		user_id as "ID",
		DATE_PART('Year', age(birth_date)) as "Age"
	FROM 
		Users
)
SELECT 
	count(1) as "sum"
FROM 
	Users u
INNER JOIN
	AGE_TABLE a
	ON
	u.user_id = a."ID"
WHERE 
	(a."Age" >= 30)
	AND
	(u.residence = 'Kazan')
	AND
	(u.job != 'Kazan')
;
