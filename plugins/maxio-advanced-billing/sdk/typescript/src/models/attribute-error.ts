import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type AttributeError = {
  attribute: string[];
};

export const attributeErrorSchema: Schema<AttributeError> = s.object<AttributeError>({
  attribute: s.array(s.string()),
});
