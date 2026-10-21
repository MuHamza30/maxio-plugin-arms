import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { siteSchema, type Site } from "./site.js";

export type SiteResponse = {
  site: Site;
};

export const siteResponseSchema: Schema<SiteResponse> = s.object<SiteResponse>({
  site: siteSchema,
});
