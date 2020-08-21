import sys
from subprocess import Popen
from subprocess import PIPE
import tempfile


def execute(cmd, exit=False, timeout=300):
    print(cmd)
    p = Popen(
        cmd,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    )
    try:
        outs, errs = p.communicate(timeout=timeout)
    except TimoutExpired:
        print(f'Timeout reached {timeout} - killing process')
        p.kill()
        outs, errs = p.communicate()
    rt = p.returncode
    if (errs or rt != 0) and exit:
        if errs:
            print(f'Error occur during command execution (return code {rt})')
            print(outs)
            print(errs)
        sys.exit(1)
    print(outs)
    print(errs)
