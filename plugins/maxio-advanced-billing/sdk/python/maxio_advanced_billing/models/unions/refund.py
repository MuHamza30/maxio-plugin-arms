from __future__ import annotations

from typing import TypeAlias

from ..refund_consolidated_invoice import RefundConsolidatedInvoice, RefundConsolidatedInvoiceDict
from ..refund_invoice import RefundInvoice, RefundInvoiceDict

Refund: TypeAlias = RefundInvoice | RefundConsolidatedInvoice

RefundDict: TypeAlias = RefundInvoiceDict | RefundConsolidatedInvoiceDict
