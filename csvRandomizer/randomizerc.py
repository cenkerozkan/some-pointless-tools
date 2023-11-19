# Required libraries
from dataclasses import field
import random
import csv
from datetime import time
from IPython.display import display

"""
I've been given a task for my job application.

A task is simply building an application which provides
users to track the number of people by counting them with
cameras hour by hour.

In order to do some tests, I need data. So this program creates
csv file with randomized column values, then saves it in CSV format.
"""

def main():
    # id          (int8)-----------------------------------------(Random)
    # hotel_name  (varchar)----------------(Su Apart, Rixos, Ankara Otel)
    # date        (date)---------------------------(YYYY-MM-DD)
    # hour        (time)---------------------------(24HRS)
    # place       (varchar)------------------------(Bar, Reception, Pool)
    # camera1     (int4)---------------------------(Random between 1 - 300)
    # camera2     (int4)---------------------------(Random between 1 - 300)
    # camera3     (int4)---------------------------(Random between 1 - 300)

    # Will be updated
    tableList = []
    fields = ["id","hotel_name","date","hour","place","camera1","camera2","camera3"]
    placeList = ["Bar", "Reception", "Pool"]
    hotelList = ["Su Apart", "Rixos", "Ankara Otel"]
    i_days = int(input("How many days of a month: "))
    i_month = int(input("Which month: "))
    i_year = int(input("What year: "))
    i_hr = 24
    for i in range(i_days):
        print(i)
        for y in range(i_hr):
            for x in range(3):
                swpRow = {"id": random.randint(1,99999999),
                        "hotel_name": hotelList[x],
                        "date": f"{i_month}.{i+1}.{i_year}",
                        "hour": time(y,00,00),
                        "place": placeList[x],
                        "camera1": random.randint(1,300),
                        "camera2": random.randint(1,300),
                        "camera3": random.randint(1,300)}
                tableList.append(swpRow)
                display(swpRow)

    # File.
    strFileName = input("Enter file name:")
    with open(f'{strFileName}.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(tableList)
    csvfile.close()


if __name__ == "__main__":
    main()
    