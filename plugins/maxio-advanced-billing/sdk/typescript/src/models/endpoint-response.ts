import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { endpointSchema, type Endpoint } from "./endpoint.js";

export type EndpointResponse = {
  endpoint?: Endpoint;
};

export const endpointResponseSchema: Schema<EndpointResponse> = s.object<EndpointResponse>({
  endpoint: s.optional(s.lazy(() => endpointSchema)),
});
