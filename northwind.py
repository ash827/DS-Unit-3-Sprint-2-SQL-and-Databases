#/*What are the 10 most expensice items (per unit price)*/

SELECT ProductName,UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;

#/*What is the Average age of an employee at
the time of hiring?*/ 
SELECT Avg(HireAge) 
FROM (
	SELECT LastName, (HireDate - BirthDate) as HireAge 
	FROM Employee);

#/*How does the average age vary by city?*/
SELECT *
FROM (
	SELECT LastName, (HireDate - BirthDate) as HireAge, City
	FROM Employee)
	ORDER BY City;

#So excited because everything worked when I tried it out 
#In TablePlus!!!! 