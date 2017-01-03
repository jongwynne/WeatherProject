import pickle


with open('./varlife', 'rb') as p1:
    life = pickle.load(p1)
with open('./varpouch', 'rb') as p2:
    pouch = pickle.load(p2)
print 'my life is', str(life)
print 'my pouch contents are', pouch
