import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type AutoResume = {
  automaticallyResumeAt?: Date | null;
};

export const autoResumeSchema: Schema<AutoResume> = s.object<AutoResume>({
  automaticallyResumeAt: s.optionalNullable(s.dateTime()),
  _keysMap: {
    automaticallyResumeAt: "automatically_resume_at",
  },
});
