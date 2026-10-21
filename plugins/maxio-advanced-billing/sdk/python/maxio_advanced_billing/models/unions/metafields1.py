from __future__ import annotations

from typing import TypeAlias

from ..update_metafield import UpdateMetafield, UpdateMetafieldDict

Metafields1: TypeAlias = UpdateMetafield | list[UpdateMetafield]

Metafields1Dict: TypeAlias = UpdateMetafieldDict | list[UpdateMetafieldDict]
