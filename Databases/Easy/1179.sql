SELECT id,
	SUM(CASE WHEN month = 'Jan' THEN REVENUE ELSE null END) AS Jan_Revenue,
	SUM(CASE WHEN month = 'Feb' THEN REVENUE ELSE null END) AS Feb_Revenue,
	SUM(CASE WHEN month = 'Mar' THEN REVENUE ELSE null END) AS Mar_Revenue,
	SUM(CASE WHEN month = 'Apr' THEN REVENUE ELSE null END) AS Apr_Revenue,
	SUM(CASE WHEN month = 'May' THEN REVENUE ELSE null END) AS May_Revenue,
	SUM(CASE WHEN month = 'Jun' THEN REVENUE ELSE null END) AS Jun_Revenue,
	SUM(CASE WHEN month = 'Jul' THEN REVENUE ELSE null END) AS Jul_Revenue,
	SUM(CASE WHEN month = 'Aug' THEN REVENUE ELSE null END) AS Aug_Revenue,
	SUM(CASE WHEN month = 'Sep' THEN REVENUE ELSE null END) AS Sep_Revenue,
	SUM(CASE WHEN month = 'Oct' THEN REVENUE ELSE null END) AS Oct_Revenue,
	SUM(CASE WHEN month = 'Nov' THEN REVENUE ELSE null END) AS Nov_Revenue,
	SUM(CASE WHEN month = 'Dec' THEN REVENUE ELSE null END) AS Dec_Revenue
FROM department
GROUP BY id
ORDER BY id;
