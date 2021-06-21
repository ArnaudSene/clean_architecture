"""Script to test antidote lib for dependency injection."""

import typing as _t

import applications.nas_open_share_exception as _a_nose
import domains.nas_open_share_exception as _d_nose
import providers.nas_open_share_exception


def main():
    """Main function."""
    result: _t.List[_d_nose.NASOpenShareException] = _a_nose.ReadNASOpenShareException()()
    print(result)


if __name__ == "__main__":
    main()


