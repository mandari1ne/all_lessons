def close_file(func):
    def wrapper(file_name):
        f = func(file_name)

        f.close()

    return wrapper

@close_file
def write_file(f_name):
    f = open(f_name, 'w')

    f.write('Hello')
    return f

write_file('f.txt')
