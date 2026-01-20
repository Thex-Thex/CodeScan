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


# Création du fichier CSV
create_csv_file()

ScannedCode = scan_code()
print(ScannedCode)
