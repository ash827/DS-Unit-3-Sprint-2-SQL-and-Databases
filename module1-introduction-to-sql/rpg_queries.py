import sqlite3

/* #1 Total Characters */
SELECT SUM(character_id) AS TotalCharacters
FROM charactercreator_character
/* #2 How many of each subclass */
SELECT SUM(character_ptr_id) AS TotalCleric
FROM charactercreator_cleric
SELECT SUM(character_ptr_id) AS TotalFighter
FROM charactercreator_fighter
SELECT SUM(character_ptr_id) AS TotalMage
FROM charactercreator_mage
SELECT SUM(mage_ptr_id) AS TotalNecromancer
FROM charactercreator_necromancer
SELECT SUM(character_ptr_id) AS TotalThief
FROM charactercreator_thief
/* #3 How many total Items? */
SELECT SUM(item_id) AS TotalItems
FROM charactercreator_character_inventory
SELECT SUM(item_id) AS TotalArmory
FROM armory_item
SELECT SUM(item_ptr_id) AS TotalWeapon
FROM armory_weapon
/* #4 How many Items does each character have? (Return first 20 rows) */
SELECT character_id, item_id, 
SUM (item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
/*#5 How many Weapons does each character have? (Return first 20 rows) */
SELECT character_id, item_id
FROM charactercreator_character_inventory
WHERE item_id >= 138
GROUP BY character_id
LIMIT 20
/*#6 On average, how many Items does each Character have? */
SELECT AVG(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
/* #7 On average, how many Weapons does each character have? */
SELECT AVG(item_id)
FROM charactercreator_character_inventory
WHERE item_id >= 138
GROUP BY character_id
