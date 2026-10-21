import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { includeOptionSchema, type IncludeOption } from "./include-option.js";

/**
 * Warning: When updating a metafield's scope attribute, all scope attributes must be passed.
 * Partially complete scope attributes will override the existing settings.
 */
export type MetafieldScope = {
  /** Include (1) or exclude (0) metafields from the csv export. */
  csv?: IncludeOption;
  /** Include (1) or exclude (0) metafields from invoices. */
  invoices?: IncludeOption;
  /** Include (1) or exclude (0) metafields from statements. */
  statements?: IncludeOption;
  /** Include (1) or exclude (0) metafields from the portal. */
  portal?: IncludeOption;
  /**
   * Include (1) or exclude (0) metafields used in [Embeddable
   * Components](page:development-tools/embeddable-components/overview) from being viewable by your
   * ecosystem.
   */
  publicShow?: IncludeOption;
  /**
   * Include (1) or exclude (0) metafields used in [Embeddable
   * Components](page:development-tools/embeddable-components/overview) from being editable by your
   * ecosystem.
   */
  publicEdit?: IncludeOption;
  hosted?: string[];
};

export const metafieldScopeSchema: Schema<MetafieldScope> = s.object<MetafieldScope>({
  csv: s.optional(s.lazy(() => includeOptionSchema)),
  invoices: s.optional(s.lazy(() => includeOptionSchema)),
  statements: s.optional(s.lazy(() => includeOptionSchema)),
  portal: s.optional(s.lazy(() => includeOptionSchema)),
  publicShow: s.optional(s.lazy(() => includeOptionSchema)),
  publicEdit: s.optional(s.lazy(() => includeOptionSchema)),
  hosted: s.optional(s.array(s.string())),
  _keysMap: {
    publicShow: "public_show",
    publicEdit: "public_edit",
  },
});
