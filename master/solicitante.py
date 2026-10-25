from collections.abc import Mapping
from decimal import Decimal

class Solicitante:
    def __init__(self, titulacion: str, nota_media: Decimal, idiomas: Mapping[str, str]) -> None:
        if not isinstance(titulacion, str) or not titulacion.strip():
            raise ValueError("La titulación del solicitante no puede estar vacía.")
        self._titulacion = titulacion
        self.actualizar_nota_media(nota_media)
        self.actualizar_idiomas(idiomas)

    def actualizar_nota_media(self, nota_media: Decimal) -> None:
        if not isinstance(nota_media, Decimal):
            raise ValueError("La nota media debe ser Decimal.")
        if not Decimal("0") <= nota_media <= Decimal("10"):
            raise ValueError("La nota media debe estar entre 0 y 10.")
        self._nota_media = nota_media

    def actualizar_idiomas(self, idiomas: Mapping[str, str]) -> None:
        if not isinstance(idiomas, Mapping):
            raise ValueError("Los idiomas deben asociarse a sus niveles.")
        for idioma, nivel in idiomas.items():
            if not isinstance(idioma, str) or not idioma.strip():
                raise ValueError("El nombre del idioma no puede estar vacío.")
            if not isinstance(nivel, str) or not nivel.strip():
                raise ValueError("El nivel del idioma no puede estar vacío.")
        self._idiomas = idiomas
