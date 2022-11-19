import pprint   ## To print the output in a better format
import json

# An old habit from C.
def main():
    # Required variables
    dct_movies = {}     # Going to be saved as JSON file later.
    c_flag = 'y'        # While loop flag.

    # Building the JSON file.
    while (c_flag == 'y'):
        s_name = str.lower(input("Enter the name of the movie: "))
        i_year = int(input("Year of the movie: "))
        arr_cast = []
        s_type = str.lower(input("Type of the movie: "))
        s_director = str.lower(input("Director of the movie: "))
        f_imdb_score = float(input("IMDB Score: "))

        ## Appends the cast members to the 'arr_cast'.
        while(True):
            cast_name = str.lower(input("Enter the name (Type q to end): "))
            if(cast_name == 'q'):
                break
            arr_cast.append(cast_name)

        swp_movie = {
            s_name: {
                "year": i_year,
                "cast": arr_cast,
                "type": s_type,
                "director": s_director,
                "IMDB score": f_imdb_score,
            }
        }
        dct_movies.update(swp_movie)
        pprint.pprint(dct_movies)
        c_flag = input("Continue (y/n):")


    # File ops.
    s_file_name = input("Enter name of the file: ")
    with open(f'{s_file_name}.json','w') as file:
        json.dump(dct_movies,file,indent=6)
    file.close()


if __name__ == "__main__":
    main()
