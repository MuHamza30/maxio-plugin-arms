import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { listPublicKeysMetaSchema, type ListPublicKeysMeta } from "./list-public-keys-meta.js";
import { publicKeySchema, type PublicKey } from "./public-key.js";

export type ListPublicKeysResponse = {
  chargifyJsKeys?: PublicKey[];
  meta?: ListPublicKeysMeta;
};

export const listPublicKeysResponseSchema: Schema<ListPublicKeysResponse> = s.object<ListPublicKeysResponse>({
  chargifyJsKeys: s.optional(s.array(s.lazy(() => publicKeySchema))),
  meta: s.optional(s.lazy(() => listPublicKeysMetaSchema)),
  _keysMap: {
    chargifyJsKeys: "chargify_js_keys",
  },
});
