import random
import os
import string


def generate_random_words(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randrange(1, size)))


def create_test_file(words, filename):
    try:
        test_file = open(filename, 'w')
    except (OSError, IOError) as e:
        print("Error:", e)

    test_file.writelines("%s\n" % word for word in words)
    test_file.close()
    print("Yielding: ", filename)


def delete_file(filename):
    try:
        if os.path.isfile(filename):
            os.unlink(filename)
    except Exception as e:
        print(e)


def correct_test_file_gen(number_of_tests, test_files_path):
    counter = 0
    while counter < number_of_tests:
        words = []
        for i in range(random.randrange(1, 10)):
            words.append(generate_random_words(15).title())
        filename = test_files_path + "correct_test_file" + str(counter)
        create_test_file(words, filename)
        yield filename
        counter += 1
        delete_file(filename)