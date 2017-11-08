import inspect
import sys


def assert_warn(arg1, arg2):
    if not eval("{}{}".format(arg1, arg2)):
        fn, ln = '', 0
        found = False
        txt = ''
        for item in inspect.stack():
            if found:
                fn = item.function
                ln = item.lineno
                break
            # Old python support
            if sys.version_info >= (3, 5):
                found = item.function == 'assert_warn'
            else:
                found = True

        if found:
            txt = 'function: [{}] line: {}'.format(fn, ln)
        print('\nWarning: {}\nNOT {}{}'.format(txt, arg1, arg2))
