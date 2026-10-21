from __future__ import annotations

from typing import TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UrlTemplate, param
from .environment import Environment


class ProductionUsConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://{site}.chargify.com"
    site: str = "subdomain"


class ProductionUsConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class ProductionEuConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://{site}.ebilling.maxio.com"
    site: str = "subdomain"


class ProductionEuConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    us: ProductionUsConfig = Field(default_factory=ProductionUsConfig)
    eu: ProductionEuConfig = Field(default_factory=ProductionEuConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "us":
            us = self.us
            return UrlTemplate(base_url=us.base_url, path=path, variables=[param[str]("site", us.site)])
        eu = self.eu
        return UrlTemplate(base_url=eu.base_url, path=path, variables=[param[str]("site", eu.site)])


class ProductionConfigDict(TypedDict):
    us: NotRequired[ProductionUsConfigDict]
    eu: NotRequired[ProductionEuConfigDict]


class EbbUsConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://events.chargify.com/{site}"
    site: str = "subdomain"


class EbbUsConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class EbbEuConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://events.chargify.com/{site}"
    site: str = "subdomain"


class EbbEuConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class EbbConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    us: EbbUsConfig = Field(default_factory=EbbUsConfig)
    eu: EbbEuConfig = Field(default_factory=EbbEuConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "us":
            us = self.us
            return UrlTemplate(base_url=us.base_url, path=path, variables=[param[str]("site", us.site)])
        eu = self.eu
        return UrlTemplate(base_url=eu.base_url, path=path, variables=[param[str]("site", eu.site)])


class EbbConfigDict(TypedDict):
    us: NotRequired[EbbUsConfigDict]
    eu: NotRequired[EbbEuConfigDict]


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ProductionConfig = Field(default_factory=ProductionConfig)
    ebb: EbbConfig = Field(default_factory=EbbConfig)

    @classmethod
    def coerce(cls, value: ServerConfigOrDict | None) -> ServerConfig:
        if isinstance(value, cls):
            return value
        return cls.model_validate(value if value is not None else {})


class ServerConfigDict(TypedDict):
    production: NotRequired[ProductionConfigDict]
    ebb: NotRequired[EbbConfigDict]


ServerConfigOrDict: TypeAlias = ServerConfig | ServerConfigDict
