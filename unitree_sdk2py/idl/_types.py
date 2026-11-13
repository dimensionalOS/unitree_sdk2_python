"""``cyclonedds.idl.types`` with ``uint8`` resolved to ``byte`` where it exists.

Unitree's IDL declares its 8-bit fields as ``octet`` (XTypes ``TK_BYTE``). The
modules in this package were generated before cyclonedds had ``types.byte``:
they spell ``octet`` as ``types.uint8``, which cyclonedds 0.10 announces as
``TK_BYTE``. cyclonedds 0.11 (released as 11.0) announces ``uint8`` as
``TK_UINT8`` and spells ``octet`` as ``types.byte``, so there the generated
annotations no longer match the robot's types and endpoints never connect.

Generated modules import this as ``types`` in place of ``cyclonedds.idl.types``.
"""

import cyclonedds.idl.types as _types
from cyclonedds.idl.types import *

uint8 = getattr(_types, "byte", _types.uint8)
