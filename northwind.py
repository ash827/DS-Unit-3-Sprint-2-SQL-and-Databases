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

#Part 3 - didn't EXACTLY get the stretch on this one,
#but I got close!

#/*What are the 10 most expensive items and their suppliers?*/
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier
	ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;

#/*What is the largest category(by # of unique prods in it)?*/
SELECT CategoryName, COUNT(DISTINCT ProductName) as prod_count
FROM Category
JOIN Product
	ON Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY prod_count DESC;

#/*Who is the employee with the most territory?*/
SELECT TerritoryId, EmployeeId
FROM Employee
JOIN EmployeeTerritory
	ON Employee.Id = EmployeeTerritory.EmployeeId
ORDER BY EmployeeId;