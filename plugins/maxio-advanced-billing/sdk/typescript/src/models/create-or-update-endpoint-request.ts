import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createOrUpdateEndpointSchema, type CreateOrUpdateEndpoint } from "./create-or-update-endpoint.js";

/** Used to Create or Update Endpoint. */
export type CreateOrUpdateEndpointRequest = {
  /** Used to Create or Update Endpoint. */
  endpoint: CreateOrUpdateEndpoint;
};

export const createOrUpdateEndpointRequestSchema: Schema<CreateOrUpdateEndpointRequest> =
  s.object<CreateOrUpdateEndpointRequest>({
    endpoint: createOrUpdateEndpointSchema,
  });
