import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { serviceCreditSchema, type ServiceCredit } from "./service-credit.js";

export type ServiceCreditResponse = {
  serviceCredit: ServiceCredit;
};

export const serviceCreditResponseSchema: Schema<ServiceCreditResponse> = s.object<ServiceCreditResponse>({
  serviceCredit: serviceCreditSchema,
  _keysMap: {
    serviceCredit: "service_credit",
  },
});
