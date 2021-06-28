"""This is the interface (abstract) for exo."""

import abc as _abc
import typing as _t

import domains.exo as _d_exo


class Exo(_abc.ABC):
    """"""

    @_abc.abstractmethod
    def read(
            self,
            name: _t.Optional[str] = None,
            description: _t.Optional[str] = None
    ) -> _t.List[_d_exo.Exo]:
        """"""
        raise NotImplemented
