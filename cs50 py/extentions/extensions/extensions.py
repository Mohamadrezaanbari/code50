#give a file name by user
user_input = input("enter your file name")

if '.gif' in user_input:
    print("image/gif")
elif '.jpeg' in user_input or '.jpg' in user_input:
    print("image/jpeg")
elif '.png' in user_input:
    print("image/png")
elif '.PDF' in user_input or 'pdf' in user_input:
    print("application/pdf")
elif '.txt' in user_input:
    print("text/plain")
elif '.zip' in user_input:
    print("application/zip")
else:
    print("application/octet-stream")

