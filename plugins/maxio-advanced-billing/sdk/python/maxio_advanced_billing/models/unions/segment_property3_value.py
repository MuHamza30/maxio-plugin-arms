from __future__ import annotations

from typing import TypeAlias

SegmentProperty3Value: TypeAlias = str | float | int | bool
"""A value that will occur in your events that you want to bill upon. The type of the value depends on the property type
in the related event based billing metric."""

SegmentProperty3ValueDict: TypeAlias = str | float | int | bool
