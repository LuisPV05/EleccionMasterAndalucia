"""Máster ofertado en una convocatoria de admisión."""

from dataclasses import dataclass

from .acceso import Acceso
from .criterio import Criterio
from .errores import ErrorDominio


@dataclass(frozen=True)
class Master:
    """Estudio ofertado y condiciones asociadas para valorar solicitudes."""

    codigo: str
    nombre: str
    accesos: tuple[Acceso, ...]
    criterios: tuple[Criterio, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.codigo, str) or not self.codigo.isdigit() or len(self.codigo) != 6:
            raise ErrorDominio("El código del máster debe contener seis cifras.")
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorDominio("El nombre del máster no puede estar vacío.")
        if not isinstance(self.accesos, tuple) or not all(
            isinstance(acceso, Acceso) for acceso in self.accesos
        ):
            raise ErrorDominio("Los accesos deben ser una tupla de accesos válidos.")
        if not isinstance(self.criterios, tuple) or not all(
            isinstance(criterio, Criterio) for criterio in self.criterios
        ):
            raise ErrorDominio(
                "Los criterios deben ser una tupla de criterios válidos."
            )
        nombres_titulaciones = [acceso.titulacion.nombre for acceso in self.accesos]
        if len(nombres_titulaciones) != len(set(nombres_titulaciones)):
            raise ErrorDominio(
                "Un máster no puede repetir la relación de acceso de una titulación."
            )
