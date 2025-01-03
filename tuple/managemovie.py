movies = []

while True:
    choice = input("Choose an option:\n1: Add movie\n2: Find movie by title\n3: Remove movie\n4: Find movie by year\n5: Display all movies\n6: Exit\n")

    if choice == '1':
        title = input("Enter Movie Title: ")
        director = input("Enter Director Name: ")
        year = input("Enter Release Year: ")
        movie = (title, director, year)
        movies.append(movie)
        print("Movie added successfully!")

    elif choice == '2':
        search_title = input("Enter Movie Title to search: ")
        found = False
        for movie in movies:
            if movie[0] == search_title:
                print("\nMovie found:")
                print("Title:", movie[0])
                print("Director:", movie[1])
                print("Year:", movie[2])
                found = True
                break
        if not found:
            print("Movie not found!")

    elif choice == '3':
        remove_title = input("Enter Movie Title to remove: ")
        found = False
        for movie in movies:
            if movie[0] == remove_title:
                movies.pop(movies.index(movie))
                print("Movie removed successfully!")
                found = True
                break
        if not found:
            print("Movie not found!")

    elif choice == '4':
        search_year = input("Enter Year to search: ")
        found = False
        print("\nMovies from year", search_year + ":")
        for movie in movies:
            if movie[2] == search_year:
                print("Title:", movie[0])
                print("Director:", movie[1])
                found = True
        if not found:
            print("Movie not found", search_year)

    elif choice == '5':
        if movies:
            print("\nAll Movies:")
            for movie in movies:
                print(f"Title: {movie[0]}, Director: {movie[1]}, Year: {movie[2]}")
        else:
            print("No movies in collection!")

    elif choice == '6':
        print("Exited")
        break

    else:
        print("Invalid choice")