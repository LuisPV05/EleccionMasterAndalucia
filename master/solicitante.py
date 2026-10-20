from collections.abc import Mapping
from dataclasses import dataclass
from decimal import Decimal
from types import MappingProxyType

from .errores import ErrorDominio
from .titulacion import Titulacion


@dataclass(frozen=True)
class Solicitante:
    titulacion: Titulacion
    nota_media: Decimal
    idiomas: Mapping[str, str]

    def __post_init__(self) -> None:
        if not isinstance(self.titulacion, Titulacion):
            raise ErrorDominio("La titulación del solicitante no es válida.")

        if not isinstance(self.nota_media, Decimal):
            raise ErrorDominio("La nota media debe ser Decimal.")

        if not Decimal("0") <= self.nota_media <= Decimal("10"):
            raise ErrorDominio("La nota media debe estar entre 0 y 10.")

        if not isinstance(self.idiomas, Mapping):
            raise ErrorDominio("Los idiomas deben asociarse a sus niveles.")

        idiomas = dict(self.idiomas)

        for idioma, nivel in idiomas.items():
            if not isinstance(idioma, str) or not idioma.strip():
                raise ErrorDominio("El nombre del idioma no puede estar vacío.")

            if not isinstance(nivel, str) or not nivel.strip():
                raise ErrorDominio("El nivel del idioma no puede estar vacío.")

        object.__setattr__(
            self,
            "idiomas",
            MappingProxyType({
                idioma.strip(): nivel.strip()
                for idioma, nivel in idiomas.items()
            }),
        )
