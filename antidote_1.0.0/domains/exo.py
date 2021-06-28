"""This is the domain (entity, DTO} for exo."""

import dataclasses as _dtc


@_dtc.dataclass
class Exo:
    """Exo DTO."""

    name: str
    description: str
