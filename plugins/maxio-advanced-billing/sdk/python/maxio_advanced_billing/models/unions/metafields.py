from __future__ import annotations

from typing import TypeAlias

from ..create_metafield import CreateMetafield, CreateMetafieldDict

Metafields: TypeAlias = CreateMetafield | list[CreateMetafield]

MetafieldsDict: TypeAlias = CreateMetafieldDict | list[CreateMetafieldDict]
