from __future__ import annotations

from typing import TypeAlias

from ..resume_options import ResumeOptions, ResumeOptionsDict

Resume: TypeAlias = bool | ResumeOptions
"""If ``true``, Advanced Billing will attempt to resume the subscription's billing period. If not resumable, the
subscription will be reactivated with a new billing period. If ``false`` or omitted, Advanced Billing will only attempt
to reactivate the subscription with a new billing period, regardless of whether or not the subscription is resumable."""

ResumeDict: TypeAlias = bool | ResumeOptionsDict
