# standard library

> [library reference](http://docs.python.org/3/library/)

## `sys` module

>包括了一些针对特定系统的功能

- example: 

    ```bash
    >>> import sys
    >>> sys.version_info
    sys.version_info(major=3, minor=5, micro=1, releaselevel='final', serial=0)
    >>> sys.version_info.major == 3
    True
    ```

## log module

> for debugging or saving some important infomation in some place.

- example:
    [stdlib_logging.py](./stdlib_logging.py)