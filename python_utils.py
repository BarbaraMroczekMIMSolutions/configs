import os
import signal
from contextlib import contextmanager
from pathlib import Path
import numpy as np


@contextmanager
def cwd(path: Path):
    """ Temporary change working directory.
         After migration to Python 3.11+ it can be replaced by:
        https://docs.python.org/3/library/contextlib.html#contextlib.chdir

        Implementation copied from:
        https://stackoverflow.com/questions/299446/how-do-i-change-directory-back-to-my-original-working-directory-with-python/37996581#37996581
        Usage:

        os.chdir('/tmp') # for testing purposes, be in a known directory
        print(f'before context manager: {os.getcwd()}')
        with cwd('/'):
            # code inside this block, and only inside this block, is in the new directory
            print(f'inside context manager: {os.getcwd()}')
        print(f'after context manager: {os.getcwd()}')
    """
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


@contextmanager
def timeout(duration: float):
    """A context manager that raises a
    :class:`TimeoutError` after a specified time.

    Modified from [#timeout]_.
    Implementation copied from https://github.com/DeepPSP/torch_ecg/blob/master/torch_ecg/utils/misc.py#L1211

    Parameters
    ----------
    duration : float
        The time duration in seconds,
        should be non-negative, 0 for no timeout.

    References
    ----------
    .. [#timeout] https://stackoverflow.com/questions/492519/timeout-on-a-function-call

    """
    if np.isinf(duration):
        duration = 0
    elif duration < 0:
        raise ValueError("`duration` must be non-negative")
    elif duration > 0:  # granularity is 1 second, so round up
        duration = max(1, int(duration))

    def timeout_handler(signum, frame):
        raise TimeoutError(f"block timedout after `{duration}` seconds")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(int(duration))
    yield
    signal.alarm(0)
