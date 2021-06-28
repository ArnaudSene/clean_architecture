"""Script to test antidote lib for dependency injection."""

import typing as _t

import applications.exo as _a_exo
import domains.exo as _d_exo
import providers.exo as _p_exo


def main():
    """Main function."""
    # result: _t.List[_d_exo.Exo] = _a_exo.ReadExo()()
    exo_repo = _p_exo.Exo()
    result: _t.List[_d_exo.Exo] = _a_exo.ReadExo(exo_repo=exo_repo)()
    print(result)


if __name__ == "__main__":
    main()
