import type { ClientOptions } from "./client-options.js";
import type { ServerBase, UrlTemplate } from "./core/api-request.js";
import { ConfigurationError } from "./core/errors.js";
import { resolveBaseUrl } from "./core/url.js";
import * as s from "./core/validation/index.js";

export const ServerEnvironment = {
  Us: "us",
  Eu: "eu",
} as const;
export type ServerEnvironment = (typeof ServerEnvironment)[keyof typeof ServerEnvironment];

export type Servers = {
  production: <Path extends string>(subPath: Path) => UrlTemplate<Path>;
  ebb: <Path extends string>(subPath: Path) => UrlTemplate<Path>;
};

const usSchemas = {
  production: {
    baseUrl: s.of(s.defaulted(s.string(), "https://{site}.chargify.com")),
    site: s.of(s.defaulted(s.string(), "subdomain")),
  },
  ebb: {
    baseUrl: s.of(s.defaulted(s.string(), "https://events.chargify.com/{site}")),
    site: s.of(s.defaulted(s.string(), "subdomain")),
  },
};

const euSchemas = {
  production: {
    baseUrl: s.of(s.defaulted(s.string(), "https://{site}.ebilling.maxio.com")),
    site: s.of(s.defaulted(s.string(), "subdomain")),
  },
  ebb: {
    baseUrl: s.of(s.defaulted(s.string(), "https://events.chargify.com/{site}")),
    site: s.of(s.defaulted(s.string(), "subdomain")),
  },
};

export function buildServers(options: ClientOptions): Servers {
  const base = {
    production: resolveBaseUrl(productionServer(options)),
    ebb: resolveBaseUrl(ebbServer(options)),
  };
  return {
    production: (subPath) => ({ baseUrl: base.production, subPath }),
    ebb: (subPath) => ({ baseUrl: base.ebb, subPath }),
  };
}

function productionServer(options: ClientOptions): ServerBase {
  const environment = options.serverEnvironment;
  switch (environment) {
    case ServerEnvironment.Us:
    case undefined:
      return {
        baseUrl: usSchemas.production.baseUrl.decode(options.serverOptions?.production?.baseUrl),
        variables: { site: usSchemas.production.site.decode(options.serverOptions?.production?.site) },
      };
    case ServerEnvironment.Eu:
      return {
        baseUrl: euSchemas.production.baseUrl.decode(options.serverOptions?.production?.baseUrl),
        variables: { site: euSchemas.production.site.decode(options.serverOptions?.production?.site) },
      };
    default:
      unknownEnvironment(environment);
  }
}

function ebbServer(options: ClientOptions): ServerBase {
  const environment = options.serverEnvironment;
  switch (environment) {
    case ServerEnvironment.Us:
    case undefined:
      return {
        baseUrl: usSchemas.ebb.baseUrl.decode(options.serverOptions?.ebb?.baseUrl),
        variables: { site: usSchemas.ebb.site.decode(options.serverOptions?.ebb?.site) },
      };
    case ServerEnvironment.Eu:
      return {
        baseUrl: euSchemas.ebb.baseUrl.decode(options.serverOptions?.ebb?.baseUrl),
        variables: { site: euSchemas.ebb.site.decode(options.serverOptions?.ebb?.site) },
      };
    default:
      unknownEnvironment(environment);
  }
}

function unknownEnvironment(environment: never): never {
  throw new ConfigurationError(`Unknown server environment: ${String(environment)}`);
}
