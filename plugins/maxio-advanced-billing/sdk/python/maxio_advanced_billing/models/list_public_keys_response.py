from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_public_keys_meta import ListPublicKeysMeta, ListPublicKeysMetaDict
from .public_key import PublicKey, PublicKeyDict


class ListPublicKeysResponse(SdkBaseModel):
    chargify_js_keys: Optional[list[PublicKey]] = UNSET
    meta: Optional[ListPublicKeysMeta] = UNSET


class ListPublicKeysResponseDict(TypedDict):
    chargify_js_keys: NotRequired[list[PublicKeyDict]]
    meta: NotRequired[ListPublicKeysMetaDict]
