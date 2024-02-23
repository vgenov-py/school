# import csv

# db = [
#     ["id", "description"],
#     ["1", "desc1"],
#     ["2", "desc2"],
#     ["3", "desc 3" ]
# ]

# with open("data.csv", "w", encoding="utf-8") as file:
#     jaime_el_escritor = csv.writer(file, delimiter=";")
#     # for line in db:
#     #     jaime_el_escritor.writerow(line)
#     jaime_el_escritor.writerows(db)

import datetime as dt

new_dt = dt.datetime.now()
new_dt_2 = f"{new_dt.day}/{new_dt.month}/{new_dt.year}"
print(new_dt_2)