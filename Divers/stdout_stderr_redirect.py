import sys
import traceback

stdout_filename = 'result.out'
stderr_filename = 'result.err'
stdout_file = None
stderr_file = None
standard_stdout = sys.stdout
standard_stderr = sys.stderr

try:
    stdout_file = open(stdout_filename,"w")
    stderr_file = open(stderr_filename,"w")

    sys.stdout = stdout_file
    sys.stderr = stderr_file

    print 'test the std out 2fd'

    b = 5 / 0;
except:
    traceback.print_exc(file=sys.stderr)
    traceback.print_exc(file=standard_stderr) # just to see error on standard err output
finally:
    sys.stdout = standard_stdout


    if stdout_file:
        stdout_file.close()

    sys.stderr = standard_stderr

    if stderr_file:
        stderr_file.close()


