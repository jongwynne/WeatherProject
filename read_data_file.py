import sys
import csv

pathtocsv = sys.argv[1]
if len(sys.argv)<2 :
    with open(pathtocsv, "r") as readfile:
    r = csv.reader(readfile)
    for row in r:
        print row
