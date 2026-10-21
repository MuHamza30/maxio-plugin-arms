import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PaymentCollectionMethodChanged = {
  previousValue: string;
  currentValue: string;
};

export const paymentCollectionMethodChangedSchema: Schema<PaymentCollectionMethodChanged> =
  s.object<PaymentCollectionMethodChanged>({
    previousValue: s.string(),
    currentValue: s.string(),
    _keysMap: {
      previousValue: "previous_value",
      currentValue: "current_value",
    },
  });
