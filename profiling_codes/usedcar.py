import csv
# fieldnms = ["count", "km", "Year", "powerPS", "minPrice", "maxPrice", "avgPrice", "sdPrice"
# ]
# , fieldnames=fieldnms
with open(r"C:\Users\Student22\Desktop\usedcars.csv", "r") as usedcar:
    carsales = csv.DictReader(usedcar, delimiter=",", skipinitialspace=True)
    cs = {}
    for c in carsales:
        yr = int(c["year"])
        pr = float(c["avgPrice"])
        if cs.get(yr, 0)<> 0:
            cs.setdefault(yr, list()).append(pr)
        else:
            cs.setdefault(yr, list()).append(pr)
sales = {yr: sum(prices)} #not finished
    #for i in cs:
    #    print cs.keys()
    #    print cs.values()[i]/cs.keys().__len__()[i]
