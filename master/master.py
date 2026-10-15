from collections.abc import Mapping
from dataclasses import dataclass
from decimal import Decimal
from types import MappingProxyType
from .acceso import Acceso
from .criterio import Criterio
from .errores import ErrorDominio
from .requisito import Requisito
from .titulacion import Titulacion
@dataclass(frozen=True, eq=False)
class Master:
    codigo: str
    nombre: str
    convocatoria: str
    accesos: Mapping[Titulacion, Acceso]
    criterios: tuple[Criterio, ...]
    requisitos: tuple[Requisito, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.convocatoria, str) or not self.convocatoria.strip():
            raise ErrorDominio("La convocatoria debe ser texto no vacío.")
        if not isinstance(self.codigo, str) or not self.codigo.isdigit() or len(self.codigo) != 6:
            raise ErrorDominio("El código del máster debe contener seis cifras.")
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorDominio("El nombre del máster no puede estar vacío.")
        if not isinstance(self.accesos, Mapping):
            raise ErrorDominio("Los accesos deben estar indexados por titulación.")
        accesos = dict(self.accesos)
        for titulacion, acceso in accesos.items():
            if not isinstance(titulacion, Titulacion) or not isinstance(acceso, Acceso):
                raise ErrorDominio("Cada acceso debe asociarse a una titulación válida.")
            if titulacion != acceso.titulacion:
                raise ErrorDominio("La clave del acceso debe coincidir con su titulación.")
        if not isinstance(self.criterios, tuple) or not all(isinstance(c, Criterio) for c in self.criterios):
            raise ErrorDominio("Los criterios deben ser una tupla de criterios válidos.")
        if self.criterios and sum((c.ponderacion for c in self.criterios), Decimal("0")) != Decimal("100"):
            raise ErrorDominio("Las ponderaciones de los criterios deben sumar 100.")
        if not isinstance(self.requisitos, tuple) or not all(isinstance(r, Requisito) for r in self.requisitos):
            raise ErrorDominio("Los requisitos generales deben ser una tupla válida.")
        object.__setattr__(self, "convocatoria", self.convocatoria.strip())
        object.__setattr__(self, "nombre", self.nombre.strip())
        object.__setattr__(self, "accesos", MappingProxyType(accesos))

    @property
    def identidad(self) -> tuple[str, str]:
        return (self.convocatoria, self.codigo)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Master):
            return NotImplemented
        return self.identidad == other.identidad

    def __hash__(self) -> int:
        return hash(self.identidad)
