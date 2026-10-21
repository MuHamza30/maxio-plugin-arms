import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createReasonCodeSchema, type CreateReasonCode } from "./create-reason-code.js";

export type CreateReasonCodeRequest = {
  reasonCode: CreateReasonCode;
};

export const createReasonCodeRequestSchema: Schema<CreateReasonCodeRequest> =
  s.object<CreateReasonCodeRequest>({
    reasonCode: createReasonCodeSchema,
    _keysMap: {
      reasonCode: "reason_code",
    },
  });
