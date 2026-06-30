def main():
    # Prompt user for name of file and Take care of case sensitivity
    file_name = input("File Name: ")
    file_name = file_name.casefold()
    file_type(file_name)

def file_type(file):
    # Output file media type based of suffix
    # Default should be application/octet-stream
    match file:
        case file if file.endswith(".gif"):
            print("image/gif")
        case file if file.endswith(".jpeg") | file.endswith(".jpg"):
            print("image/jpeg")
        case file if file.endswith(".png"):
            print("image/png")
        case file if file.endswith(".pdf"):
            print("application/pdf")
        case file if file.endswith(".txt"):
            print("document/txt")
        case file if file.endswith(".zip"):
            print("application/zip")
        case _:
            print("application/octet-stream")
main()