import pickle


life = 99.00
pouch = ['green potion', '10 gold coins']

with open('./varlife', 'wb') as p1:
    pickle.dump(life, p1)
with open('./varpouch', 'wb') as p2:
    pickle.dump(pouch, p2)
