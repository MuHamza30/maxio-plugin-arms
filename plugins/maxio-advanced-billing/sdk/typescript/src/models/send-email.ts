import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SendEmail = {
  canExecute: boolean;
  url: string;
};

export const sendEmailSchema: Schema<SendEmail> = s.object<SendEmail>({
  canExecute: s.boolean(),
  url: s.string(),
  _keysMap: {
    canExecute: "can_execute",
  },
});
