author = {"php": "Rasmus Lerdorf",
          "perl": "Larry Wall",
          "tcl": "John Ousterhout",
          "awk": "Brian Kernighan",
          "java": "James Gosling",
          "parrot": "Simon Cozens",
          "python": "Guido van Rossum"}
print((sorted(author.items())))
print((sorted(author.items(), key=lambda x: (x[1], x[0]))))
