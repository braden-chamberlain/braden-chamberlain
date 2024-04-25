import pymongo
from queries_copy import GET_CHARACTERS, ITEM_NAMES, WEAPON_NAMES
from sqlite_ex import connect_to_db, execute_q

# credentials:
DBNAME = 'sprint2'
PASSWORD = 'Kacidog2'

def mongo_connect(password=PASSWORD, collection_name='characters'):
    client = pymongo.MongoClient(f'mongodb+srv://braden134:{PASSWORD}@cluster0.hni3akb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client[DBNAME]
    collection = db[collection_name]
    return collection

#how the test will come back from sqlite
test_characters = [(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1),
                   (2, 'Optio dolrem ex a', 0, 0, 10, 1, 1, 1, 1)
                   ]

# how our data will be stored inside of mongodb
character_documents = [
    {
    'character_id': 1,
    'name':'Aliquid iste optio reiciendi',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1
    },
]

if __name__ == '__main__':
    # get data from sqlite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)
    sl_items = execute_q(sl_conn, ITEM_NAMES)
    sl_weapons = execute_q(sl_conn, WEAPON_NAMES)

    item_dict = {}
    weapons_dict = {}

    for char_id, item in sl_items:
        if char_id not in item_dict:
            item_dict[char_id] = []
        item_dict[char_id].append(item)

    for char_id, weapon in sl_weapons:
        if char_id not in weapons_dict:
            weapons_dict[char_id] = []
        weapons_dict[char_id].append(weapon)

    # print(item_dict, weapons_dict)

    # connect to a specifiv mongodb collection
    collection = mongo_connect(collection_name='assignment')

    print(sl_characters)

    for character in sl_characters:
        doc = {'character_id': character[0],
               'name': character[1],
               'level': character[2],
               'exp': character[3],
               'hp': character[4],
               'strength': character[5],
               'intelligence': character[6],
               'dexterity': character[7],
               'wisdom': character[8],
               'items': item_dict.get(character[0], []),
               'weapons': weapons_dict.get(character[0], [])
                }

        collection.insert_one(doc)
