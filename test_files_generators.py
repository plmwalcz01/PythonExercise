import random
import os
import string


def generate_random_words(size):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randrange(1, size)))


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


def test_file_gen(test_files_path, test_file_type, number_of_tests,
                  max_number_of_words, max_word_size, uppercase):
    counter = 0
    while counter < number_of_tests:
        words = []
        for i in range(random.randrange(1, max_number_of_words)):
            if uppercase:
                words.append(generate_random_words(max_word_size).title())
            else:
                words.append(generate_random_words(max_word_size))

        filename = test_files_path + test_file_type + str(counter)
        create_test_file(words, filename)
        yield filename
        counter += 1
        delete_file(filename)
