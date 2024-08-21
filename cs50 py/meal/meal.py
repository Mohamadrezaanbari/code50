def main():
    awnser = input("what's time is it??")
    time = convert(awnser)
    if time >= 7 and time <= 8:
        print('breakfast time')
    if time >= 12 and time <= 13:
        print('lunch time')
    if time >= 18 and time <= 19:
        print('dinner time')

def convert(time):
    hours , mintues = time.split(':')
    new_mintues = float(mintues) / 60
    return float(hours) + new_mintues

if __name__ == "__main__":
    main()
