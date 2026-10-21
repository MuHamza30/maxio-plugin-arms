from __future__ import annotations

from typing import TypeAlias

SegmentUids: TypeAlias = list[str] | str
"""An array of segment uids to refund or the string 'all' to indicate that all segments should be refunded"""

SegmentUidsDict: TypeAlias = list[str] | str
