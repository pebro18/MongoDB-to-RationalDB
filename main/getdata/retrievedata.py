from pymongo import MongoClient
all_col = ['products', 'sessions', 'visitors']
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["huwebshop"]
mycol = mydb[all_col[0]]

for i in mycol.find({'brand': "8x4"}, {"_id": 0, "brand": 1}):
    print(i)

    #test


class getdata(object):


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
        return mycol.find_one({},{"_id": 0, "name": 1, "price.selling_price": 1})

    def name_startR(self):
        return



