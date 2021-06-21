"""
This is the abstract class and method definition for NAS open share exception.

Support:
    For any issue with <project>, contact: hagen@devops.com.
"""
import abc as _abc
import typing as _t

import domains.nas_open_share_exception as _d_nose


class NASOpenShareException(_abc.ABC):
    """"""

    @_abc.abstractmethod
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
        raise NotImplemented
