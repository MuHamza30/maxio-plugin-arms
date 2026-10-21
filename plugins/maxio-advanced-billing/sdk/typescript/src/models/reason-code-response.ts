import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { reasonCodeSchema, type ReasonCode } from "./reason-code.js";

export type ReasonCodeResponse = {
  reasonCode: ReasonCode;
};

export const reasonCodeResponseSchema: Schema<ReasonCodeResponse> = s.object<ReasonCodeResponse>({
  reasonCode: reasonCodeSchema,
  _keysMap: {
    reasonCode: "reason_code",
  },
});
