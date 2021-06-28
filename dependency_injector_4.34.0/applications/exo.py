"""This is the application (use case} for exo."""

import typing as _t

import domains.exo as _d_exo
import interfaces.exo as _i_exo


class ReadExo:
    """"""

    def __init__(
        self,
        exo_repo: _i_exo.Exo
    ):
        """"""
        self.exo_repo = exo_repo

    def __call__(
        self,
        name: _t.Optional[str] = None,
        description: _t.Optional[str] = None
    ) -> _t.List[_d_exo.Exo]:
        """"""
        return self.exo_repo.read(
            name=name,
            description=description
        )
