import type { BasicAuthCredentials } from "./core/auth/credentials.js";
import type { CoreClientOptions } from "./core/client-options.js";
import { ServerEnvironment } from "./servers.js";

export type ClientOptions = SdkClientOptions & CoreClientOptions;

type SdkClientOptions = ServerOptions & {
  /** The `username` is a Maxio Chargify API key. The `password` is `x`. */
  readonly basicAuth?: BasicAuthCredentials | undefined;
};

type ServerOptions =
  | {
      readonly serverEnvironment?: typeof ServerEnvironment.Us;
      readonly serverOptions?: {
        /**
         * Default Advanced Billing environment hosted in US. Valid for the majority of our
         * customers.
         */
        production?: {
          baseUrl?: string;
          /** The subdomain for your Advanced Billing site. @default "subdomain" */
          site?: string;
        };
        /**
         * Default Advanced Billing environment hosted in US. Valid for the majority of our
         * customers.
         */
        ebb?: {
          baseUrl?: string;
          /** The subdomain for your Advanced Billing site. @default "subdomain" */
          site?: string;
        };
      };
    }
  | {
      readonly serverEnvironment: typeof ServerEnvironment.Eu;
      readonly serverOptions?: {
        /**
         * Default Advanced Billing environment hosted in US. Valid for the majority of our
         * customers.
         */
        production?: {
          baseUrl?: string;
          /** The subdomain for your Advanced Billing site. @default "subdomain" */
          site?: string;
        };
        /**
         * Default Advanced Billing environment hosted in US. Valid for the majority of our
         * customers.
         */
        ebb?: {
          baseUrl?: string;
          /** The subdomain for your Advanced Billing site. @default "subdomain" */
          site?: string;
        };
      };
    };
