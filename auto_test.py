import os, sys
from subprocess import call

def redirect_stdout():
    print("Redirecting stdout")
    sys.stdout.flush() # <--- important when redirecting to files

    # Duplicate stdout (file descriptor 1)
    # to a different file descriptor number
    newstdout = os.dup(1)

    # /dev/null is used just to discard what is being printed
    raport = os.open('build_products/raport', os.O_WRONLY)

    # Duplicate the file descriptor for /dev/null
    # and overwrite the value for stdout (file descriptor 1)
    os.dup2(raport, 1)

    # Close devnull after duplication (no longer needed)
    os.close(raport)

    # Use the original stdout to still be able
    # to print to stdout within python
    sys.stdout = os.fdopen(newstdout, 'w')


if __name__ == '__main__':
    redirect_stdout()
    call(["./build_products/appPE", "test",])
    call(["./build_products/appPE", "test2", ])
    call(["./build_products/appPE", "test3", ])
    print("finished")
