import csv


def create_csv_file():
    with open("codes.csv", mode="w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerows(["Code"])
    print("info : CSV file created successfully")

# function that wait an input of code scan or manual
def scan_code():
    code = input("Scan a code or enter it manually : ")
    return code

def save_code(codedata):
    print("code saved")

# Création du fichier CSV
create_csv_file()

# calling fonction to save code
ScannedCode = scan_code()
print(ScannedCode)

# asking to save code while reply not good : yes or no
while True: 
    savecode = input("Save code y or n : ")
    if savecode == "y":
        print("save")
        break
    elif savecode == "n":
        break
