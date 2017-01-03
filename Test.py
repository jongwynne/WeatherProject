# x = '   kUbrick-grouPings               ...        '
# y = 'r'
# z = 'PC1234-LON-2016'
# print x[::2]
# print x.strip(' ''.')
# print x.join(y)
# print x.split('-', 1)
# print x.lower()
# print x.capitalize()
# print x.find(y)
# print x.replace('k', 'z')
# print x.strip(' ''.').replace('k', 'z').lower().capitalize()
# z = z.split('-', 2)
# a = z[0][2:7]
# z[0] = z[0][0:2]
# print z[1]
# print a
# print z[2]
# print z[0]
# st0 = ' 124-BMG.2016#10#23.FOX HOLLIES '
# st1 = '   9872347-    LON. 2016#08#14.  WAPPING    '
# st2 = '  7657-CAR.2015#03#02.LLANDAFF        '
# st3 = '     36-BMG.   2016#02#29.LEE BANK'
# # st4 = ' 876264-LON.2016  #03#24.CROYDON    '
# st0clean = st0.split('.')
# st0clean[0] = st0clean[0].strip()
# st0clean[1] = st0clean[1].strip()
# st0clean[2] = st0clean[2].strip()
# st0clean[1] = st0clean[1].replace('#', '-')
# st0clean[0] = st0clean[0].split('-')
# st0clean[1] = st0clean[1].split('-')
# st0clean[2] = st0clean[0][1] + '-' + st0clean[2]
# st0clean[0] = st0clean[0][0]
# st0clean[1] = st0clean[1][1] + '-' + st0clean[1][2] + '-' + st0clean[1][0]
# st0clean[0] = st0clean[0].strip()
# st0clean[1] = st0clean[1].strip()
# st0clean[2] = st0clean[2].strip()
# print st0clean
# st1clean = st1.split('.')
# st1clean[0] = st1clean[0].strip()
# st1clean[1] = st1clean[1].strip()
# st1clean[2] = st1clean[2].strip()
# st1clean[1] = st1clean[1].replace('#', '-')
# st1clean[0] = st1clean[0].split('-')
# st1clean[1] = st1clean[1].split('-')
# st1clean[2] = st1clean[0][1] + '-' + st1clean[2]
# st1clean[0] = st1clean[0][0]
# st1clean[1] = st1clean[1][1] + '-' + st1clean[1][2] + '-' + st1clean[1][0]
# st1clean[0] = st1clean[0].strip()
# st1clean[1] = st1clean[1].strip()
# st1clean[2] = st1clean[2].strip()
# print st1clean
# st2clean = st2.split('.')
# st2clean[0] = st2clean[0].strip()
# st2clean[1] = st2clean[1].strip()
# st2clean[2] = st2clean[2].strip()
# st2clean[1] = st2clean[1].replace('#', '-')
# st2clean[0] = st2clean[0].split('-')
# st2clean[1] = st2clean[1].split('-')
# st2clean[2] = st2clean[0][1] + '-' + st2clean[2]
# st2clean[0] = st2clean[0][0]
# st2clean[1] = st2clean[1][1] + '-' + st2clean[1][2] + '-' + st2clean[1][0]
# st2clean[0] = st2clean[0].strip()
# st2clean[1] = st2clean[1].strip()
# st2clean[2] = st2clean[2].strip()
# print st2clean
# st3clean = st3.split('.')
# st3clean = [i.strip() for i in st3clean]
# st3clean[1] = st3clean[1].replace('#', '-')
# st3clean[0] = st3clean[0].split('-')
# st3clean[1] = st3clean[1].split('-')
# st3clean[2] = st3clean[0][1] + '-' + st3clean[2]
# st3clean[0] = st3clean[0][0]
# st3clean[1] = st3clean[1][1] + '-' + st3clean[1][2] + '-' + st3clean[1][0]
# st3clean[0] = st3clean[0].strip()
# st3clean[1] = st3clean[1].strip()
# st3clean[2] = st3clean[2].strip()
# print st3clean

# index notation
# name = 'jon'
# course = 'python'
# msg = 'hi {0} you are on the {1} course'.format(name, course)
# print msg

# Dictionary notation
# name = 'jon'
# course = 'python'
# msg = 'hi %(n)s you are on the %(c)s course' %{'n': name, 'c': course}
# print msg
# name = 'jon'
# course = 'python'
# msg = 'hi ' + name + 'you are on the ' + course + 'course'
# print msg
# l = ['Halo', 'BoI', 'Super Meat Boy', 'Clash']
# print type(l)
# l.append('Stanley Parable')
# l.extend(['Gow', 'Tf2'])
# l.insert(1,'3')
# print l
# orders = [[10, 'jon', '2016-3-6', 'DHL', [1,2,3,4,5]],
# [11, 'jono', '2016-7-4', 'Fedex', [1]],
# [12, 'johnny', '2016-10-10', 'RoyalMail', [123,25,33,4,5]],
# [13, 'john', '2016-12-12', 'DHL', [1,27,34]],
# [14, 'jonathan', '2016-11-11', 'UPS', [1,2]]]
# dates = []
# delivery = []
# name = []
# products = []
# for i in orders:
#     dates.append(i[2])
#     name.append(i[1])
#     delivery.append(i[3])
#     products.append(i[4])
# print dates
# print delivery
# print products
# name.reverse()
# print name
# st0 = ' 124-BMG.2016#10#23.FOX HOLLIES '
# st1 = '   9872347-    LON. 2016#08#14.  WAPPING    '
# st2 = '  7657-CAR.2015#03#02.LLANDAFF        '
# st3 = '     36-BMG.   2016#02#29.LEE BANK'
# st4 = ' 876264-LON.2016  #03#24.CROYDON    '
# st = []
# st.append(st0)
# st.append(st1)
# st.append(st2)
# st.append(st3)
# st.append(st4)
# cities = []
# for s in st:
#     st0clean = s.split('.')
#     st0clean[0] = st0clean[0].strip()
#     st0clean[1] = st0clean[1].strip()
#     st0clean[2] = st0clean[2].strip()
#     st0clean[1] = st0clean[1].replace('#', '-')
#     st0clean[0] = st0clean[0].split('-')
#     st0clean[1] = st0clean[1].split('-')
#     st0clean[2] = st0clean[0][1] + '-' + st0clean[2]
#     st0clean[0] = st0clean[0][0]
#     st0clean[1] = st0clean[1][1] + '-' + st0clean[1][2] + '-' + st0clean[1][0]
#     st0clean[0] = st0clean[0].strip()
#     st0clean[1] = st0clean[1].strip()
#     st0clean[2] = st0clean[2].strip()
#     cities.append(st0clean[2])
# print cities
# import csv
# dates = []
# customers = []
# delivery = []
# products = []
# with open(r"C:\data\data.txt", "r") as orders:
#     oreader = csv.reader(orders, delimiter=",", quotechar="#", skipinitialspace=True)
#     for o in oreader:
#         dates.append(o[2])
#         customers.append(o[1])
#         delivery.append(o[3])
#         products.append(o[4])
# print dates
# print customers
# print delivery
# print products
# import csv
# casenumber = []
# date = []
# type = []
# with open(r"C:\Users\Student22\Desktop\attacks.csv", "r") as attacks:
#      Areader = csv.reader(attacks, delimiter=",", skipinitialspace=True)
#      Areader.next()
#      for a in Areader:
#          casenumber.append(a[0])
#          date.append(a[1])
#          type.append(a[3])
# casenumber = [c[0:9]for c in casenumber]
# print date
# print type
# print casenumber
# l = [1,2,3]
# print l.pop(0)
# mylist = [x for x in range(10)]
# print mylist[4]
# mygen = (x for x in range(10))
# print mygen[4]
# orders = [{'ordersid':82, 'customername': 'lawrence','instructions':'neighbour' ,'delivery': 'DHL', 'basket': {51: 5, 87: 2}}, {'ordersid': 15, 'customername': 'jo', 'delivery': 'UPS','basket': {54: 7, 17: 9}}]
# for o in orders:
#   print o['basket']
# print orders
# print type(orders)
# for order in orders:
#     print order.get('instructions','N\A')
# basket = {'raptormouse': 1}
# basket['raptormouse'] +=1
# basket['xb1'] = 1

# if 'n64' in basket.keys():
#    basket['n64'] += 1
# else:
#   basket['n64'] = 1
# print basket

# import csv
# fieldnms = ["Case Number" ,"Date", "Year", "Type", "Country", "Area",	"Location",	"Activity"	,"Name", "Sex", "Age", "Injury", "Fatal (Y/N)", "Time", "Species", "Investigator or Source"
# ]
# with open(r"C:\Users\Student22\Desktop\attacks.csv", "r") as attacks:
#      Areader = csv.DictReader(attacks, delimiter=",", skipinitialspace=True, fieldnames=fieldnms)
#      for n in Areader:
#          print n["Case Number"] +" "+ n["Name"]
# import json
# with open(r"c:\data\reddit.json", "r") as j:
#     data = json.load(j)
# print type(data)
# print data['data']['children']['created_utc']
# import datetime as dt
# n = dt.datetime.now()
# print n.strftime("%A %Y %B %d")
# n2 = dt.datetime(2016, 11, 25)
# print n2
# print n2.year
# print n2.month
# print n2.day
# import datetime as dt
#
# i = raw_input('Enter a date (dd-mm-yyyy): ')
# i2 = raw_input('Enter another date (dd-mm-yyyy): ')
# d = dt.datetime.strptime(i, '%d-%m-%Y')
# d2 = dt.datetime.strptime(i2, '%d-%m-%Y')
# print 'These dates differ by',str(d2-d)
# addyear = dt.timedelta(days=365)
# print d + addyear
# import datetime as dt
# w = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# i = raw_input('Enter a date (dd-mm-yyyy): ')
# l = raw_input('When was last(Ddd):')
# d = dt.datetime.strptime(i, '%d-%m-%Y')
# da = d.strftime('%a')
# days_diff = (7 + w.index(da) - w.index(l)) %8
# print days_diff
# def writetofile(filepath,content):
#     try:
#         f = open(filepath, 'r+')
#     except IOError:
#         f = open(filepath, 'w')
#         f.close()
#         f = open(filepath, 'r+')
#     f.write(content)
#     f.close()
# writetofile('c:\\data\\accountdata.txt','test content')
l1 = [7,8,9]
l2 = [1,2,3]
basket = zip(l1, l2)
av = [ av[1] / av[0] for av in basket]
print av

