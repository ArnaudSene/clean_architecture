"""
This is the provider for NAS open share exception.

Support:
    abc
"""
import typing as _t

import antidote as _antidote

import antidote_dp.domains.nas_open_share_exception as _d_nose
import antidote_dp.interfaces.nas_open_share_exception as _i_nose


@_antidote.implements(_i_nose.NASOpenShareException)
@_antidote.register
class NASOpenShareException(_i_nose.NASOpenShareException):
    """"""
    
    def read(
            self,
            name: _t.Optional[str] = None,
            description: _t.Optional[str] = None
    ) -> _t.List[_d_nose.NASOpenShareException]:
        """Read all NAS open share exceptions.

        Args:
            name (_t.Optional[str], optional): The exception name. Defaults to None.
            description (_t.Optional[str], optional): The description name. Defaults to None.

        Raises:
            NotImplemented: [description]

        Returns:
            _t.List[_d_nose.NasOpenShareException]: A list of NasOpenShareException DTO.
        """
        return [_d_nose.NASOpenShareException(
            name=f'exception_{i}',
            description=f'this is a description {i}'
        ) for i in range(5)]

