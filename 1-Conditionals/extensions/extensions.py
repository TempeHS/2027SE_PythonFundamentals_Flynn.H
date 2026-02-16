file = input("please enter your file: ")
if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("document/pdf")
elif file.endswith(".txt"):
    print("text/txt")
elif file.endswith(".zip"):
    print("archive/zip")
else:
    print("application/octet-stream")
