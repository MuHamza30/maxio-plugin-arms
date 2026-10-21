import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type OfferSignupPage = {
  id?: number;
  nickname?: string;
  enabled?: boolean;
  returnUrl?: string;
  returnParams?: string;
  url?: string;
};

export const offerSignupPageSchema: Schema<OfferSignupPage> = s.object<OfferSignupPage>({
  id: s.optional(s.int()),
  nickname: s.optional(s.string()),
  enabled: s.optional(s.boolean()),
  returnUrl: s.optional(s.string()),
  returnParams: s.optional(s.string()),
  url: s.optional(s.string()),
  _keysMap: {
    returnUrl: "return_url",
    returnParams: "return_params",
  },
});
