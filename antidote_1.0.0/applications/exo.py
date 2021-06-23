"""This is the application (use case} for exo."""

import typing as _t

import antidote as _antidote

import domains.exo as _d_exo
import interfaces.exo as _i_exo


class ReadExo:
    """"""

    @_antidote.inject
    def __init__(
        self,
        exo_repo: _antidote.Provide[_i_exo.Exo]

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
