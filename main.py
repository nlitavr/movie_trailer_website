from movie import Movie
from fresh_tomatoes import open_movies_page

# Application class that runs the program until the user quits
class MainApp():
    # Method that gets user input one line at a time
    # Returns the user_input as a string
    def user_input():
        usr_input = raw_input()
        if usr_input == "":
            print "Exiting program.."
            exit(1)
        return (usr_input)

    # Method to initialize each movie object based on the Movie class
    # returns the movie object
    def initialize_movie(m):
        movie = Movie(m[0], m[1], m[2])
        return movie

    # A list of possible prompts to cycle through in a loop
    prompts = ['Please enter a movie title:',
        'Please enter the url for movie poster for your movie',
        'Please enter the url for a movie trailer for your movie']

    # An empty array/list that will hold movie objects
    movie_list = list()

    # The main prompt for when the program starts
    print "Please enter Movie information into the prompt."
    print "(to exit the program, enter a blank line)"
    # The program will run until the user enters a blank ""
    while True:
        # An array/list that gets re-initialized on every iteration
        # of the while loop, stores each Movies (title,poster,trailer)
        movie_raw = list()

        # Cycling through each prompt to gather data for a movie object
        for p in prompts:
            print p
            usr_input = user_input()
            movie_raw.append(usr_input)

        # Initializing movie object with the raw user data
        # movie_raw array will always have 3 of some kind of values
        movie = initialize_movie(movie_raw)
        # Adding the movie object to a list of movies
        movie_list.append(movie)

        # Poll user to find out if they want to add more movies,
        # or generate a webpage from the existing content.
        print "Generate webpage from the content entered? Y/n"
        print "(to exit the program, enter a blank line)"

        usr_input = user_input()

        # If the user enters y or Y for yes, a movie page will be generated
        if usr_input.lower() == 'y':
            print "Opening movie webpage.. "
            open_movies_page(movie_list)
            print "Exiting program.."
            exit(1)
        # If the user enters n or N, the program will continue to
        # run until the user enters yes or quits
        elif usr_input.lower() == 'n':
            continue
        # If the user enters an unknown choice the program will
        # quit, letting the user known why
        else:
            print 'Choice does not match available options! "'+usr_input+'"'
            print "Please start over!"
            print "Exiting program.."
            exit(1)

# Will run the
if __name__ == 'main':
    MainApp().run()
