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

#Answering questions:

#1.In the Northwind database, what is the type of
# relationship between the Employee and Territory tables?

#It looks to be a many to many relationship. There is a 
# separate table that links them together, and that is the 
# EmployeeTerritory table. You can join Employee and EmployeeTerritory
# on the EmployeeId, and also link EmployeeTerritory with Territory
# on TerritoryId.

#2. What is a situation where a document store (like MongoDB) is 
# appropriate, and what is a situation where it is not appropriate?

#MongoDB is widely used for NoSQL (not only SQL) data. NoSQL is 
# unstructured data, unlike Relational Databases. You can add or 
# delete fields as needed. It also has a large amount of space to 
# load large datasets into.

#MongoDB is NOT appropriate when working with Relational Databases. 
#. I believe it's missing the ACID component of Relational 
# databases. 

#3. What is "NewSQL", and what is it trying to achieve?
# NewSQL is a new approach of SQL using Relational Database 
# Management Systems (RDMS), by combining NoSQL to it for it's 
# scalability, all while maintaining ACID guarantees.

#ACID is Atomicity, Consistency, Isolation, Durability.
#"Ensures consistent, safe and robust database modification
# when saved"