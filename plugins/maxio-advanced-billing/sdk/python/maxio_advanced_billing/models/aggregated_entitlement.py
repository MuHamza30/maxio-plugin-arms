from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .aggregated_entitlement_periodicity import AggregatedEntitlementPeriodicity, AggregatedEntitlementPeriodicityDict
from .enums.feature_kind import FeatureKindOrStr
from .unions.value import Value, ValueDict


class AggregatedEntitlement(SdkBaseModel):
    """One entitlement in a subscriber's aggregated entitlements list. Entries are aggregated per feature key and
    periodicity window, not per feature key alone. A ``usage_limit`` feature granted with two different periodicities
    yields two entries sharing one ``feature_key``. Use ``periodicity_key`` to identify an entry uniquely."""

    feature_key: Optional[str] = UNSET
    """The feature's key, prefixed by kind: ``feature.*`` for ``access_right``, ``usage.*`` for ``usage_limit``,
    ``service.*`` for ``service_right``."""

    periodicity_key: Optional[str] = UNSET
    """Uniquely identifies this aggregated entry: the prefixed feature key, suffixed with ``:{interval}:{unit}`` when
    the entitlement has a periodicity window. Equal to ``feature_key`` when ``periodicity`` is ``null``."""

    name: Optional[str] = UNSET
    type_: Optional[FeatureKindOrStr] = Field(default=UNSET, alias="type")
    """The behavior of a feature:
    - ``access_right``: a boolean entitlement. A subscriber either has access or does not.
    - ``usage_limit``: a quantified allowance measured over a recurring period (for example, "10,000 API calls per
        month").
    - ``service_right``: a free-form value (text, boolean, or number) that isn't a simple access flag or a metered
        limit."""

    value: Optional[Value] = UNSET
    """The aggregated value, coerced according to ``type``: a boolean for ``access_right`` (and boolean
    ``service_right``), a number for ``usage_limit`` (and numeric ``service_right``), or a string for text
    ``service_right``."""

    enabled: Optional[bool] = UNSET
    """``true`` only when the aggregated value is truthy for this feature's kind, and the subscription is in a live
    state (``active``, ``trialing``, ``assessing``, ``past_due``, or ``soft_failure``). ``false`` otherwise, including
    for ``awaiting_signup``, canceled, expired, and on-hold subscriptions. Entitlements deliberately stay enabled
    through dunning."""

    periodicity: OptionalNullable[AggregatedEntitlementPeriodicity] = UNSET
    source_products: Optional[list[str]] = UNSET
    """The names of the products/components contributing to this entitlement. For ``access_right`` features, only
    contributors that granted ``true`` are listed."""


class AggregatedEntitlementDict(TypedDict):
    feature_key: NotRequired[str]
    periodicity_key: NotRequired[str]
    name: NotRequired[str]
    type_: NotRequired[FeatureKindOrStr]
    value: NotRequired[ValueDict]
    enabled: NotRequired[bool]
    periodicity: NotRequired[AggregatedEntitlementPeriodicityDict | None]
    source_products: NotRequired[list[str]]
