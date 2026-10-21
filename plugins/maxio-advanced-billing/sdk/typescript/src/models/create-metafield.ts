import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { metafieldInputSchema, type MetafieldInput } from "./metafield-input.js";
import { metafieldScopeSchema, type MetafieldScope } from "./metafield-scope.js";

export type CreateMetafield = {
  name?: string;
  /**
   * Warning: When updating a metafield's scope attribute, all scope attributes must be passed.
   * Partially complete scope attributes will override the existing settings.
   */
  scope?: MetafieldScope;
  /**
   * Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio
   * metafields have a set of values that can be selected. Defaults to 'text'.
   */
  inputType?: MetafieldInput;
  /** Only applicable when input_type is radio or dropdown. Empty strings will not be submitted. */
  enum?: string[];
};

export const createMetafieldSchema: Schema<CreateMetafield> = s.object<CreateMetafield>({
  name: s.optional(s.string()),
  scope: s.optional(s.lazy(() => metafieldScopeSchema)),
  inputType: s.optional(s.lazy(() => metafieldInputSchema)),
  enum: s.optional(s.array(s.string())),
  _keysMap: {
    inputType: "input_type",
  },
});
