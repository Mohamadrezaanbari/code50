import sys
import csv

def main():
    check_correct_args()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
                print(row)
    except FileNotFoundError:
        sys.exit("Couldn't read CSV file")

    output = []
    for row in data:
        dynasty = select_Geographical_region(row["dynasty"])
        height = select_height(row["Height"])
        output.append({
            "Name": row["Name"],
              "Geographical_region": dynasty ,
              "Height": height})
        print(output)

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Geographical_region", "Height"] )
        writer.writerow({"Name": "Name", "Geographical_region":"Geographical_region", "Height": "Height"})
        for row in output:
            writer.writerow({"Name": row["Name"],"Geographical_region": row["Geographical_region"],"Height": row["Height"]})



def check_correct_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV files")


def select_Geographical_region(dynasty):
    if dynasty in ["Stark","Mormont","Greyjoy","Bolton","free people",]:
        return "North"
    elif dynasty in ["Targaryen","Lannister","Martell","Baratheon"]:
        return "South"
    else:
        return "None"

def select_height(Height):
    height = float(Height) * 3.28
    height_1 = round(height,1)
    return height_1

if __name__ == "__main__":
    main()
