def file_handeling():
    my_file = open('python/example.txt', 'r')

    one_line = my_file.readline()
    multiple_lines = my_file.readlines() 

    print(one_line)
    print("\n-============\n")
    print(multiple_lines)
    my_file.close
file_handeling() 