import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const AutoInvite = {
  /** Do not send the invitation email. */
  _0: 0,
  /** Automatically send the invitation email. */
  _1: 1,
} as const;
export type AutoInvite = (typeof AutoInvite)[keyof typeof AutoInvite] | (number & {});

export const autoInviteSchema: EnumSchema<AutoInvite> = s.enumOf<AutoInvite>(AutoInvite);
