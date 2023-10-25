def user_book_to_movies():
  print("Book ID: ", end='')
  book_id = input()
  print("Number of movies: ", end='')
  movie_count = input()

  res = recommend_movie(book_id, movie_count)
  print("Result")
  print(res)

  return


def user_movie_to_movies():
  print("Movie ID: ", end='')
  movie_id = input()
  print("Number of moveis: ", end='')
  movie_count = input()

  res = recommend_among_movies(movie_id, movie_count)
  print("Result")
  print(res)

  return


def user_book_movie_similarity():
  print("Movie ID: ", end='')
  movie_id = input()
  print("Book ID: ", end='')
  book_id = input()

  show_similarity(book_id, movie_id)

  return


def console():
    print("Enter a command")
    print("1: Book To Movies")
    print("2: Movie To Movies")
    print("3: Book And Movie Similarity")
    print("-1 to exit")

    while True:
        print("Command: ", end='')
        command = int(input())

        if input == -1:
            print("Exit Program")
            break

        elif input == 1:
            user_book_to_movies()
        elif input == 2:
            user_movie_to_movies()
        elif input == 3:
            user_book_movie_similarity()
        else:
            print("Invalid Command")


def console():
    print("Enter a command")
    print("1: Book To Movies")
    print("2: Movie To Movies")
    print("3: Book And Movie Similarity")
    print("-1 to exit")

    while True:
        print("Command: ", end='')
        command = int(input())

        if input == -1:
            print("Exit Program")
            break

        elif input == 1:
            user_book_to_movies()
        elif input == 2:
            user_movie_to_movies()
        elif input == 3:
            user_book_movie_similarity()
        else:
            print("Invalid Command")

    return


console()
