"""
This is the use case for NAS open share exceptions.

Support:

"""
import typing as _t

import antidote as _antidote

import antidote_dp.domains.nas_open_share_exception as _d_nose
import antidote_dp.interfaces.nas_open_share_exception as _i_node


class ReadNASOpenShareException:
    """"""

    @_antidote.inject
    def __init__(
        self,
        nose_repo: _i_node.NASOpenShareException
    ):
        """"""
        self.nose_repo = nose_repo

    def __call__(
        self,
        name: _t.Optional[str] = None,
        description: _t.Optional[str] = None
    ) -> _t.List[_d_nose.NASOpenShareException]:
        """[summary]

        Args:
            name (_t.Optional[str], optional): [description]. Defaults to None.
            description (_t.Optional[str], optional): [description]. Defaults to None.

        Returns:
            _t.List[_d_nose.NasOpenShareException]: [description]
        """
        return self.nose_repo.read(
            name=name,
            description=description
        )
