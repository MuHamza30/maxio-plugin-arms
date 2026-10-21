import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { metafieldInputSchema, type MetafieldInput } from "./metafield-input.js";
import { metafieldScopeSchema, type MetafieldScope } from "./metafield-scope.js";
import { enumSchema, type Enum } from "./unions/enum.js";

export type Metafield = {
  id?: number;
  name?: string;
  /**
   * Warning: When updating a metafield's scope attribute, all scope attributes must be passed.
   * Partially complete scope attributes will override the existing settings.
   */
  scope?: MetafieldScope;
  /** The amount of subscriptions this metafield has been applied to in Advanced Billing. */
  dataCount?: number;
  /**
   * Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio
   * metafields have a set of values that can be selected. Defaults to 'text'.
   */
  inputType?: MetafieldInput;
  enum?: Enum | null;
};

export const metafieldSchema: Schema<Metafield> = s.object<Metafield>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  scope: s.optional(s.lazy(() => metafieldScopeSchema)),
  dataCount: s.optional(s.int()),
  inputType: s.optional(s.lazy(() => metafieldInputSchema)),
  enum: s.optionalNullable(s.lazy(() => enumSchema)),
  _keysMap: {
    dataCount: "data_count",
    inputType: "input_type",
  },
});
