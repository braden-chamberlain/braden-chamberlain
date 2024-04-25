GET_CHARACTERS = '''
    SELECT * FROM charactercreator_character;
    '''

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id
    ORDER BY cc_char.name ASC;
'''

TOTAL_CHARACTERS = '''
    SELECT COUNT(*) AS num_characters 
    FROM charactercreator_character;
'''

TOTAL_SUBCLASS = '''
    SELECT COUNT(*) AS num_necromancer
    FROM charactercreator_necromancer;
'''

TOTAL_ITEMS = '''
    SELECT COUNT(*) AS num_items FROM armory_item;
'''

WEAPONS = '''
    SELECT COUNT(*) AS num_weapons FROM armory_weapon;
'''

NON_WEAPONS = '''
    SELECT COUNT(*) AS num_not_weapon FROM armory_item AS ai
    LEFT JOIN armory_weapon AS aw
    ON item_id = item_ptr_id
    WHERE item_ptr_id IS NULL;
'''

CHARACTER_ITEMS = '''
    SELECT cc_char.name, COUNT(*) AS num_items 
    FROM charactercreator_character_inventory AS char_inv
    JOIN charactercreator_character AS cc_char
    ON cc_char.character_id = char_inv.character_id
    GROUP BY cc_char.character_id
    LIMIT 20;
'''

CHARACTER_WEAPONS = '''
    SELECT cc_char.name, COUNT(ai.item_id) AS num_weapons
    FROM armory_weapon AS aw
    JOIN armory_item AS ai
    ON ai.item_id = aw.item_ptr_id
    JOIN charactercreator_character_inventory AS inv
    ON ai.item_id = inv.item_id
    JOIN charactercreator_character AS cc_char
    ON cc_char.character_id = inv.character_id
    GROUP BY cc_char.character_id
    LIMIT 20;
'''

AVG_CHARACTER_ITEMS = '''
    SELECT AVG(num_items) AS avg_items_per_character
    FROM(
    SELECT cc_char.name, COUNT(*) AS num_items 
    FROM charactercreator_character_inventory AS char_inv
    JOIN charactercreator_character AS cc_char
    ON cc_char.character_id = char_inv.character_id
    GROUP BY cc_char.character_id
    );
'''

AVG_CHARACTER_WEAPONS = '''
    SELECT AVG(num_weapons) AS avg_weapons_per_character
    FROM(
    SELECT cc_char.name, COUNT(*) AS num_weapons
    FROM armory_weapon AS aw
    JOIN armory_item AS ai
    ON ai.item_id = aw.item_ptr_id
    JOIN charactercreator_character_inventory AS inv
    ON ai.item_id = inv.item_id
    JOIN charactercreator_character as cc_char
    ON cc_char.character_id = inv.character_id
    GROUP BY cc_char.character_id
    );
'''

CREATE_TEST_TABLE = '''
    CREATE TABLE test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country" VARCHAR(200) NOT NULL);
'''

INSERT_TEST_TABLE = '''
    INSERT INTO test_table("name", "age", "country")
    VALUES ('Braden Chamberlain', 26, 'USA');
'''

DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS test_table;
'''

CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    (
    "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
'''

INSERT_BRADEN = '''
    INSERT INTO characters("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
    VALUES ('Braden Chamberlain', 50, 100, 100, 1000, 1000, 100, 10)
    '''

DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS characters;
'''

CHARACTER_WEAPONS = '''
    SELECT cc_char.name, cc_char.level, cc_char.exp,
    cc_char.hp, cc_char.strength, cc_char.intelligence,
    cc_char.dexterity, cc_char.wisdom, ai.item_id
    FROM armory_weapon AS aw
    JOIN armory_item AS ai
    ON ai.item_id = aw.item_ptr_id
    JOIN charactercreator_character_inventory AS inv
    ON ai.item_id = inv.item_id
    JOIN charactercreator_character AS cc_char
    ON cc_char.character_id = inv.character_id
--  GROUP BY cc_char.character_id
'''

ITEM_NAMES = '''
    SELECT cc_char.character_id, ai.name
    FROM charactercreator_character_inventory AS inv
    JOIN charactercreator_character AS cc_char
    ON cc_char.character_id = inv.character_id
	JOIN armory_item as ai
	ON ai.item_id = inv.item_id
'''

WEAPON_NAMES = '''
    SELECT cc_char.character_id, ai.name
    FROM charactercreator_character_inventory AS inv
    JOIN charactercreator_character AS cc_char
    ON cc_char.character_id = inv.character_id
	JOIN armory_item AS ai
	ON ai.item_id = inv.item_id
	JOIN armory_weapon AS aw
	ON ai.item_id = aw.item_ptr_id
'''