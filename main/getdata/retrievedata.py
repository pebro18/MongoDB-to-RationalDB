from pymongo import MongoClient
all_col = ['products', 'sessions', 'visitors']
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["huwebshop"]
mycol = mydb[all_col[0]]



class getdata(object):

    """
    Deze class is gemaakt voor het ophalen van data
    geef een uitleg van elke functie in de vorm van een comment
    """

    def __init__(self):
        global all_col
        all_col = ['products', 'sessions', 'visitors']
        global myclient
        myclient = MongoClient("mongodb://localhost:27017/")
        global mydb
        mydb = myclient["huwebshop"]
        global mycol
        mycol = mydb[all_col[0]]

    def first_name_price(self):
        # Geef de naam en de prijs van het eerste product in de lijst
        return mycol.find_one({},{"_id": 0, "name": 1, "price.selling_price": 1})

    def name_startR(self):
        # Geef het eerste product terug, waar de naam begint met R
        for i in mycol.find({}, {"_id": 0, "name": 1}):
            var = i['name']
            if 'R' == var[0]:
                return var

    def average_price(self):
        totalprice = 0
        totalitems = 0

        for i in mycol.find({}, {"_id": 0, "price.selling_price": 1}):
            if i == {}:
                pass
            else:

                var = i["price"]
                newvar = var["selling_price"]
                totalprice += newvar
                totalitems += 1

        return (totalprice / totalitems)



