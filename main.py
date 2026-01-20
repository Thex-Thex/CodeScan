import csv

# csv Column
CsvColumn = [
    ["ID", "Type", "data"],
    ["0", "Barcode", "123456"],
]


def create_csv_file(Column):
    with open("codes.csv", mode="w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerows(Column)
    print("info : CSV file created successfully")


# function that wait an input of code scan or manual
def scan_code():
    code = input("Scan a code or enter it manually : ")
    return code


def save_code(code_type, data):
    with open("codes.csv", mode="a", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["1", code_type, data])


# Création du fichier CSV
create_csv_file(CsvColumn)

# calling fonction to save code
ScannedCode = scan_code()
print(ScannedCode)

####################
# test variable
code_type = "barcode"
####################

# asking to save code while reply not good : yes or no
while True:
    SaveCode = input("Save code y or n : ")
    if SaveCode == "y":
        save_code(code_type, ScannedCode)
        break
    elif SaveCode == "n":
        break
