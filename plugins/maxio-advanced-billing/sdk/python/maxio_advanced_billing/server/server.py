from __future__ import annotations

from dataclasses import dataclass

from ..core import UrlTemplate
from .environment import Environment
from .server_config import ServerConfig


@dataclass(frozen=True, slots=True)
class Server:
    environment: Environment
    config: ServerConfig

    def production(self, path: str) -> UrlTemplate:
        return self.config.production.resolve(self.environment, path)

    def ebb(self, path: str) -> UrlTemplate:
        return self.config.ebb.resolve(self.environment, path)
