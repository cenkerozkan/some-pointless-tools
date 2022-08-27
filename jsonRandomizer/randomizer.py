# Required libraries
import random
import json

"""
I Needed to set up a database for my own business.

However, since I did not have the necessary data for
the test, I felt the need to write a tool that would
generate random data in my own format.

It generates the amount of random data I want and
saves it in JSON format.
"""


def main():
    # IMEI      (int)(15-digits)--------------------(Random)
    # Plate     (Str)-------------------------------(Will be specific, but I'll assign random numbers for testing)
    # Location  (float,float)(lat/lon)--------------(Random)
    # Helmet    (bool)------------------------------(Random)
    # Engine    (bool)------------------------------(Random)
    # avgSpeed  (float)-----------------------------(Random)
    # personId  (int)(8-digits)---------------------(Specific, 6 different)
    # brandId   (int)(8-digits)---------------------(Specific, 6 different)


    # Specific variables
    i_amount = 0
    person_list = [19850084,69251830,85103713,33475258,33711308,36422555]
    brand_list = [75101412,95188925,64854896,42548472,43918341,95715343]


    # Vehicle dictionary (Will be saved as JSON file at the end)
    vehicle = {}

    i_amount = int(input("How many fake data would you like to generate:"))
    for i in range(i_amount):
       swp_vehicle = {
           f'{random.randint(100000000000000,999999999999999)}':{
               "plate":random.randint(100000,999999),
               "location":{"lat":random.randint(10,25),"lon":random.randint(15,25)},
               "helmet":random.randint(0,1),
               "engine":random.randint(0,1),
               "avgSpeed":random.uniform(20,100),
               "personId":person_list[random.randint(0,5)],
               "brandId":brand_list[random.randint(0,5)]
           }
       }
       vehicle.update(swp_vehicle)


    # File
    s_file_name = input("Enter file name:")
    with open(f'{s_file_name}.json','w') as file:
        json.dump(vehicle,file,indent=6)
    file.close()


if __name__ == "__main__":
    main()
