import csv

# csv Column
CsvColumn = [
    ["ID", "Type", "data"],
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


def save_code_to_csv(code_type, data):
    with open("codes.csv", mode="a", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["1", code_type, data])


# Création du fichier CSV
create_csv_file(CsvColumn)


while True:
    # calling fonction to scan code
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
            # caling save code function and giving code type and the code as an argument 
            save_code_to_csv(code_type, ScannedCode)
            break
        elif SaveCode == "n":
            break
