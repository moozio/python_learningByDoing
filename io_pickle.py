import pickle

# the name of the file where we will store the object
shopListFile = 'shopList.data'
# the list of things to buy
shopList = ['apple', 'mongo', 'carrot']

# open the file needed to write
f = open(shopListFile, 'wb')
# dump转储 the object to the file
pickle.dump(shopList, f)
f.close()

# destroy the shoplist variable
del shopList

# read back from the storage
f = open(shopListFile, 'rb')
# load the object from the file
storedList = pickle.load(f)

print(storedList)