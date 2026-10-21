import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { serviceCredit1Schema, type ServiceCredit1 } from "./service-credit1.js";

export type ListServiceCreditsResponse = {
  serviceCredits?: ServiceCredit1[];
};

export const listServiceCreditsResponseSchema: Schema<ListServiceCreditsResponse> =
  s.object<ListServiceCreditsResponse>({
    serviceCredits: s.optional(s.array(s.lazy(() => serviceCredit1Schema))),
    _keysMap: {
      serviceCredits: "service_credits",
    },
  });
