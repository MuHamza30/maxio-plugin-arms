from __future__ import annotations

from typing import TypeAlias

Amount7: TypeAlias = str | int
"""Signed: positive adds units to the grant, negative removes them. Bounded below by the grant's ``posted_remaining`` (a
correction can't drive it negative) and above by the grant's ``original`` (a correction can't credit past what was
originally granted). An out-of-bounds value is rejected rather than clamped. Zero is rejected. Without a ``grant_id``
(an overdraft correction), the amount must be positive, can't exceed the usage the overdraft entry still records, and
can't exceed the overdraft the wallet still owes. Encoded as a decimal string with at most 8 fractional digits. Send
fractional values as strings: a JSON number with a decimal point is rejected with ``422``, because a double-precision
float may already have lost precision before the request arrives."""

Amount7Dict: TypeAlias = str | int
