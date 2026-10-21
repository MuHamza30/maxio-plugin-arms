import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const CreateInvoiceStatus = {
  Draft: "draft",
  Open: "open",
} as const;
export type CreateInvoiceStatus =
  | (typeof CreateInvoiceStatus)[keyof typeof CreateInvoiceStatus]
  | (string & {});

export const createInvoiceStatusSchema: EnumSchema<CreateInvoiceStatus> =
  s.enumOf<CreateInvoiceStatus>(CreateInvoiceStatus);
