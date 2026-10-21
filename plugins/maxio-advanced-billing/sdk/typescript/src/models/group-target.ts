import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { groupTargetTypeSchema, type GroupTargetType } from "./group-target-type.js";

/**
 * Attributes of the target customer who will be the responsible payer of the created subscription.
 * Required.
 */
export type GroupTarget = {
  /** The type of object indicated by the id attribute. */
  type: GroupTargetType;
  /**
   * The id of the target customer or subscription to group the existing subscription with. Ignored
   * and should not be included if type is "self", "parent", or "eldest".
   */
  id?: number;
};

export const groupTargetSchema: Schema<GroupTarget> = s.object<GroupTarget>({
  type: groupTargetTypeSchema,
  id: s.optional(s.int()),
});
