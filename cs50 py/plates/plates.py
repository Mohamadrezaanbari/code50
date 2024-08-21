import re
def main():
    plate = input("plate: ")
    if is_valid(plate):
        print('Valid')
    else:
        print("Invalid")

def is_valid(s):
    if s[:2].isalpha():
        if len(s) >=2 and len(s) <= 6:
            if " " in s:
                return False
            if "." in s:
                return False
            number_in_s = re.findall(r'\d+', s)
            if number_in_s == []:
                return True
            elif number_in_s[0][0] != '0':
                 if len(number_in_s) == 1 and s[-1].isdigit():
                     return True

main()
