def write_file(file_name, file_content):
    extension= ".txt"
    string =f"{file_name}{extension}"
    with open(string, mode="w", encoding="utf-8") as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
     extension= ".txt"
     string =f"{file_name}{extension}"
     with open(string, mode="a", encoding="utf-8") as text_file:
         text_file.write(append_content)

def read_file(file_name):
     extension= ".txt"
     string =f"{file_name}{extension}"
     with open(string,mode="r",encoding="utf-8") as text_file:
         return text_file.read()
