import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PublicSignupPage = {
  /** The id of the signup page (public_signup_pages only) */
  id?: number;
  /**
   * The url to which a customer will be returned after a successful signup (public_signup_pages
   * only).
   */
  returnUrl?: string | null;
  /** The params to be appended to the return_url (public_signup_pages only) */
  returnParams?: string | null;
  /** The url where the signup page can be viewed (public_signup_pages only). */
  url?: string;
};

export const publicSignupPageSchema: Schema<PublicSignupPage> = s.object<PublicSignupPage>({
  id: s.optional(s.int()),
  returnUrl: s.optionalNullable(s.string()),
  returnParams: s.optionalNullable(s.string()),
  url: s.optional(s.string()),
  _keysMap: {
    returnUrl: "return_url",
    returnParams: "return_params",
  },
});
