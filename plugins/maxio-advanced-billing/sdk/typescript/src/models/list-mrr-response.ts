import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { listMrrResponseResultSchema, type ListMrrResponseResult } from "./list-mrr-response-result.js";

export type ListMrrResponse = {
  mrr: ListMrrResponseResult;
};

export const listMrrResponseSchema: Schema<ListMrrResponse> = s.object<ListMrrResponse>({
  mrr: listMrrResponseResultSchema,
});
