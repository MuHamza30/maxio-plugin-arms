import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateReasonCodeSchema, type UpdateReasonCode } from "./update-reason-code.js";

export type UpdateReasonCodeRequest = {
  reasonCode: UpdateReasonCode;
};

export const updateReasonCodeRequestSchema: Schema<UpdateReasonCodeRequest> =
  s.object<UpdateReasonCodeRequest>({
    reasonCode: updateReasonCodeSchema,
    _keysMap: {
      reasonCode: "reason_code",
    },
  });
