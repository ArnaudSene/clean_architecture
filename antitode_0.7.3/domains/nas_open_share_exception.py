"""
This is the DTO definition for NAS open share exception.

Support:
    Please contact hagen@devops.com
"""
import dataclasses as _dtc


@_dtc.dataclass
class NASOpenShareException:
    """NasOpenShareException DTO."""

    name: str
    description: str
