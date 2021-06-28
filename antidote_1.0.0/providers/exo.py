"""This is the provider for exo."""
import typing as _t

import antidote as _antidote

import domains.exo as _d_exo
import interfaces.exo as _i_exo


class Exo(_i_exo.Exo, _antidote.ABCService):
    """"""

    def read(
            self,
            name: _t.Optional[str] = None,
            description: _t.Optional[str] = None
    ) -> _t.List[_d_exo.Exo]:
        """"""
        return [_d_exo.Exo(
            name=f'exception_{i}',
            description=f'this is a description {i}'
        ) for i in range(5)]

