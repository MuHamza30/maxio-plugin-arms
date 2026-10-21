import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { dunnerDataSchema, type DunnerData } from "./dunner-data.js";
import { dunningStepDataSchema, type DunningStepData } from "./dunning-step-data.js";

export type DunningStepReached = {
  dunner: DunnerData;
  currentStep: DunningStepData;
  nextStep: DunningStepData;
};

export const dunningStepReachedSchema: Schema<DunningStepReached> = s.object<DunningStepReached>({
  dunner: dunnerDataSchema,
  currentStep: dunningStepDataSchema,
  nextStep: dunningStepDataSchema,
  _keysMap: {
    currentStep: "current_step",
    nextStep: "next_step",
  },
});
