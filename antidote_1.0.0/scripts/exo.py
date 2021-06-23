"""Script to test antidote 1.0.0 lib for dependency injection."""

import typing as _t

import applications.exo as _a_exo
import domains.exo as _d_exo
import providers.exo


def main():
    """Main function."""

    result: _t.List[_d_exo.Exo] = _a_exo.ReadExo()()
    # result: _t.List[_d_exo.Exo] = _a_exo.ReadExo(exo_repo=_p_exo.Exo())()
    print(result)
    # print(_antidote.world.get[_p_exo.Exo]())


if __name__ == "__main__":
    main()
