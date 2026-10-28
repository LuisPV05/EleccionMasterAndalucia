from collections.abc import Mapping
from dataclasses import dataclass
from decimal import Decimal

@dataclass(eq=False)
class Solicitante:
    titulacion: str
    nota_media: Decimal
    idiomas: Mapping[str, str]

    def __post_init__(self) -> None:
        if not isinstance(self.titulacion, str) or not self.titulacion.strip():
            raise ValueError("La titulación del solicitante no puede estar vacía.")
        if not isinstance(self.nota_media, Decimal):
            raise ValueError("La nota media debe ser Decimal.")
        if not Decimal("0") <= self.nota_media <= Decimal("10"):
            raise ValueError("La nota media debe estar entre 0 y 10.")
        if not isinstance(self.idiomas, Mapping):
            raise ValueError("Los idiomas deben asociarse a sus niveles.")
        for idioma, nivel in self.idiomas.items():
            if not isinstance(idioma, str) or not idioma.strip():
                raise ValueError("El nombre del idioma no puede estar vacío.")
            if not isinstance(nivel, str) or not nivel.strip():
                raise ValueError("El nivel del idioma no puede estar vacío.")
