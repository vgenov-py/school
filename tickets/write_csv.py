import csv

db = [
    ["id", "description"],
    ["1", "desc1"],
    ["2", "desc2"],
    ["3", "desc 3" ]
]

with open("data.csv", "w", encoding="utf-8") as file:
    csv_writer = csv.writer(file, delimiter=";")
    # for line in db:
    #     csv_writer.writerow(line)
    csv_writer.writerows(db)