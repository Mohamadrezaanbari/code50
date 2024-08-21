def main():
    dollars = dollars_to_float(input("how much was meal?"))
    percent = percent_to_float(input("what percentage would you like to tip?"))
    tip = dollars * percent
    print(f"leave ${tip:.2f}")

def dollars_to_float(d):
    d = d[1:]
    return float(d)

def percent_to_float(p):
    p = p[:-1]
    p = "0." + p[:]
    return float(p)


main()
