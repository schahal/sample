#
# Copyright 2020 Foo Bar, Inc.
#

import sys
from typing import List, Dict, Set


def dummy_func() -> bool:
    """A dummy function.

    Always returns True

    Note:
        will print a warning if you are correctly setting the config but it's currently invalid.

    Args:
        None 

    """
    return True


def main(argv: List[str] = sys.argv[1:], intercept_parser_errors: bool = False) -> int:
    """Entrypoint for the Test CLI.

    Dummy script to test doc generation.

    Args:
        argv: List of string arguments to the CLI.
        intercept_parser_errors: Determines which parser subclass to instantiate.

    Returns:
        int exit code.

    """
    if dummy_func():
        return 0

    return 1


if __name__ == "__main__":
    ret = main()
    sys.exit(0 if ret is None else ret)
