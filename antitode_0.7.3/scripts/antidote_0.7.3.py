"""Script to test antidote lib for dependency injection."""

import typing as _t

import antidote_dp.applications.nas_open_share_exception as _a_nose
import antidote_dp.domains.nas_open_share_exception as _d_nose


def main():
    """Main function."""
    result: _t.List[_d_nose.NASOpenShareException] = _a_nose.ReadNASOpenShareException()()
    print(result)


if __name__ == "__main__":
    main()


