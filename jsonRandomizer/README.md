# About
- I Needed to set up a database for my own business.
However, since I did not have the necessary data for
the test, I felt the need to write a tool that would
generate random data in my own format.
It generates the amount of random data I want and
saves it in JSON format.
- Written with **Python 3.10.4**.
- I created a json for testing purposes, you can view the format there, but also:
  - IMEI (int)(15-digits)--------------------(Random)
    - Plate     (Str)-------------------------------(Will be specific, but I'll assign random numbers for testing)
    - Location  (float,float)(lat/lon)-----------(Random)
    - Helmet    (bool)---------------------------(Random)
    - Engine    (bool)---------------------------(Random)
    - avgSpeed  (float)------------------------(Random)
    - personId  (int)(8-digits)-----------------(Specific, 6 different)
    - brandId   (int)(8-digits)------------------(Specific, 6 different)
    
    
- Sample run:
  - ![resim](https://user-images.githubusercontent.com/68559468/187005454-00b4cc72-7364-467e-8a38-1c32534692c1.png)
  - ![resim](https://user-images.githubusercontent.com/68559468/187005472-c3dd2a40-9be6-4e0a-ac4c-932f4745edd1.png)
