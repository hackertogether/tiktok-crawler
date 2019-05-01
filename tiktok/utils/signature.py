from Naked.toolshed.shell import muterun_js
import os


def generate_signature(value):
    root_dir = os.path.dirname(os.path.abspath(__file__))

    response = muterun_js(root_dir + '/scripts/byted-acrawler.js', value)
    if response.exitcode == 0:
        # the command was successful, handle the standard output
        result = response.stdout.rstrip()
    else:
        # the command failed or the executable was not present, handle the standard error
        standard_err = response.stderr
        exit_code = response.exitcode
        print('Exit Status ' + exit_code + ': ' + standard_err)
        result = None
    return result
