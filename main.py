import csv

# csv Column
CsvColumn = [
    ["ID", "data"],
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


def save_code_to_csv(id, data):
    with open("codes.csv", mode="a", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow([id, data])


# Création du fichier CSV
create_csv_file(CsvColumn)

CodeId = 0

while True:
    # calling fonction to scan code
    ScannedCode = scan_code()
    print(ScannedCode)

    # asking to save code while reply not good : yes or no
    while True:
        SaveCode = input("Save code y or n : ")
        if SaveCode == "y":
            # calling save code function and giving code type and the code as an argument 
            CodeId += 1
            save_code_to_csv(CodeId, ScannedCode)
            break
        elif SaveCode == "n":
            break
