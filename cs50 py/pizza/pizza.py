import sys, csv, tabulate


#check if valid commend line args

if len(sys.argv) > 2:
    sys.exit("too many commend-line argument")
elif len(sys.argv) < 2:
    sys.exit("too few commend-line argument")

#check if valid file

if ".csv" not in sys.argv[1]:
    sys.exit("not a CSV file")


#try opening the file, if the file
#doesn't exist, close the program
try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")


#establish reader and collect headers
reader = csv.reader(file, delimiter=',')
headers: any = next(reader)

#convert the reader in tables
tables: list[any] = [r for r in reader]
#create a result string
result: str = tabulate.tabulate(tables, headers, tablefmt="grid")


#print the result table
print(result)
