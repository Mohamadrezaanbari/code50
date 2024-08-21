import sys

#check if valid command line args
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")


#check if valid file
if ".py" not in sys.argv[1]:
    sys.exit("Not a python file")

#try opening the file, if the file doesn't exist, close the program
try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")


#iterate over the lines and track how many there are
total_lines: int = 0

#iterate over the lines
for _ in file.read().splitlines():
    if len(_.strip()) == 0:
        continue

    if not _.strip().startswith("#"):
        total_lines += 1


print(total_lines)
