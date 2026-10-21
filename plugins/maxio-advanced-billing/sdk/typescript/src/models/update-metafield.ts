import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { metafieldInputSchema, type MetafieldInput } from "./metafield-input.js";
import { metafieldScopeSchema, type MetafieldScope } from "./metafield-scope.js";

export type UpdateMetafield = {
  currentName?: string;
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
  /** Only applicable when input_type is radio or dropdown. */
  enum?: string[];
};

export const updateMetafieldSchema: Schema<UpdateMetafield> = s.object<UpdateMetafield>({
  currentName: s.optional(s.string()),
  name: s.optional(s.string()),
  scope: s.optional(s.lazy(() => metafieldScopeSchema)),
  inputType: s.optional(s.lazy(() => metafieldInputSchema)),
  enum: s.optional(s.array(s.string())),
  _keysMap: {
    currentName: "current_name",
    inputType: "input_type",
  },
});
