import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  changeChargebackStatusEventDataSchema,
  type ChangeChargebackStatusEventData,
} from "./change-chargeback-status-event-data.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type ChangeChargebackStatusEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.ChangeChargebackStatus */
  eventType?: InvoiceEventType;
  /** Example schema for an `change_chargeback_status` event */
  eventData: ChangeChargebackStatusEventData;
};

export const changeChargebackStatusEventSchema: Schema<ChangeChargebackStatusEvent> =
  s.object<ChangeChargebackStatusEvent>({
    id: s.int(),
    timestamp: s.dateTime(),
    invoice: invoiceSchema,
    eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.ChangeChargebackStatus),
    eventData: changeChargebackStatusEventDataSchema,
    _keysMap: {
      eventType: "event_type",
      eventData: "event_data",
    },
  });
