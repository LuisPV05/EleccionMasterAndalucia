
# Modelado de HU001

## 1. Historia de usuario analizada

**HU001: No sé en qué másteres tengo posibilidades objetivas de entrar.**

Claudia está terminando el Grado en Ingeniería Informática, con mención en Tecnologías de la Información, una nota media de 7,061 y un certificado de inglés B2.

Quiere conocer en qué másteres universitarios de Andalucía tiene posibilidades objetivas de entrar. Para ello, necesita relacionar la información publicada en el Distrito Único Andaluz (DUA):

- El catálogo de másteres y las prioridades de acceso de cada titulación.
- Las notas de corte de la última adjudicación.
- Las fichas de los másteres, donde se describen los criterios de valoración y los requisitos adicionales.

Las tres fuentes comparten un código de seis cifras para identificar cada máster dentro de una convocatoria. La información debe relacionarse sin asumir que dicho código permanece estable entre convocatorias.

## 2. Objetivo del Milestone 0

El objetivo de este hito es analizar el problema de la HU001 y establecer un primer modelo del dominio.

En esta fase se identifican los conceptos necesarios, sus relaciones, las reglas conocidas y los posibles datos inválidos. No se implementa todavía la funcionalidad completa de consulta de datos ni se realiza la extracción automática de información del DUA.

El modelo debe representar el problema planteado por la historia de usuario, no los detalles técnicos de cómo se obtendrán los datos.

## 3. Lenguaje ubicuo

### Convocatoria

Periodo de admisión al que pertenecen los datos de los másteres y las adjudicaciones.

El código de seis cifras permite relacionar las fuentes dentro de una misma convocatoria, pero no se presupone que identifique de forma permanente un máster entre convocatorias distintas.

### Máster

Estudio universitario al que Claudia desea solicitar el acceso.

Para analizar sus posibilidades se necesita conocer su identificación dentro de la convocatoria, las titulaciones admitidas, los requisitos adicionales, los criterios de valoración y, cuando exista, la información de corte de la adjudicación.

### Titulación

Grado universitario que posee o está terminando una estudiante.

La titulación es relevante porque la prioridad de acceso depende de la relación entre una titulación concreta y un máster.

### Prioridad

Orden de preferencia con el que se considera una titulación para acceder a un máster.

Se contemplan los valores alta, media, baja y RESTO. Cuando una titulación no aparece expresamente entre las titulaciones relacionadas con el máster, le corresponde RESTO.

La prioridad no es una propiedad aislada del máster: depende de la titulación desde la que se solicita el acceso.

### Requisito adicional

Condición que puede ser necesaria para acceder a un máster desde una titulación determinada.

Puede estar relacionada, por ejemplo, con el conocimiento de idiomas o con una formación adecuada para el máster. La información publicada puede expresarse como texto libre y no sigue necesariamente una estructura uniforme.

### Criterio de valoración

Aspecto que se utiliza para valorar la solicitud de una estudiante.

Cada máster puede aplicar un sistema diferente. Algunos utilizan únicamente la nota media; otros tienen en cuenta otros méritos o criterios cuya valoración depende de la comisión correspondiente.

### Puntuación

Resultado de aplicar el sistema de valoración de un máster a una solicitud.

No debe confundirse con la nota media del expediente, ya que los sistemas de valoración pueden ser diferentes entre másteres.

### Adjudicación

Proceso en el que se ordenan y admiten solicitudes para el acceso a los másteres.

Para interpretar el resultado es necesario tener en cuenta la prioridad y la puntuación de cada solicitud.

### Corte

Información correspondiente a la prioridad y la puntuación del último estudiante admitido en una adjudicación.

El corte puede no estar publicado todavía. También existen valores especiales que no deben interpretarse como una puntuación ordinaria.

### Posibilidad objetiva

Resultado del análisis que indica si Claudia habría conseguido entrar en un máster en la última adjudicación, de acuerdo con su prioridad y su puntuación.

Cuando no se conoce de antemano la valoración de todos los méritos, deben distinguirse los casos en los que la entrada es segura, depende de la valoración de esos méritos o no sería posible incluso con la valoración máxima considerada.

## 4. Problemas identificados

El análisis de la HU001 permite identificar los siguientes problemas del dominio:

1. Los datos de un mismo máster están distribuidos en varias fuentes.
2. El código del máster permite relacionar las fuentes dentro de una convocatoria, pero no se presupone que sea estable entre convocatorias.
3. La prioridad de acceso depende de la titulación y del máster.
4. Los requisitos adicionales pueden variar según la relación entre titulación y máster.
5. Los criterios de valoración no son iguales para todos los másteres.
6. La puntuación obtenida no equivale necesariamente a la nota media del expediente.
7. No siempre es posible calcular anticipadamente una puntuación exacta porque algunos méritos se valoran posteriormente.
8. La nota de corte incluye una prioridad y una puntuación, por lo que no basta con comparar únicamente valores numéricos.
9. Puede no existir una nota de corte publicada para una adjudicación.
10. Los valores especiales de las fuentes deben conservar su significado y no tratarse como puntuaciones ordinarias.
11. La conclusión debe distinguir entre entrada segura, entrada condicionada a la valoración de méritos e imposibilidad de entrada bajo las condiciones analizadas.

## 5. Consolidación del modelo de dominio

Los conceptos identificados se organizan para evitar mezclar datos que tienen significados diferentes.

La información académica de la estudiante se diferencia de los criterios de valoración de cada máster. La prioridad se representa en la relación entre una titulación y un máster, y el corte se relaciona con la adjudicación correspondiente.

La posibilidad objetiva no se obtiene a partir de la nota media por sí sola. Se determina comparando la prioridad y la puntuación que corresponden a la solicitud con las condiciones de acceso reflejadas en el corte.

## 6. Entidades

Una entidad se caracteriza por tener identidad dentro del contexto del dominio.

### Máster

Representa un estudio universitario. Su identificación debe interpretarse dentro del ámbito en el que el código está confirmado como único: la convocatoria.

No se debe asumir que el código de seis cifras es una identidad permanente entre convocatorias sin disponer de información que lo confirme.

### Adjudicación

Representa el resultado del proceso de admisión para una convocatoria y el máster correspondiente.

Se distingue de la información del máster porque el corte pertenece a una adjudicación concreta y puede cambiar entre convocatorias o adjudicaciones.

La identidad definitiva de estas entidades deberá mantenerse coherente con la estructura de datos que se decida implementar.

## 7. Objetos de valor

Los objetos de valor representan conceptos cuyo significado depende de sus datos y no de una identidad propia.

### Titulación

Representa una titulación universitaria. Su nombre identifica el concepto utilizado para relacionar a la estudiante con los másteres.

### Prioridad

Representa uno de los valores de prioridad admitidos: alta, media, baja o RESTO.

### Requisito

Representa una condición adicional expresada mediante una descripción textual.

### Criterio

Representa un aspecto que participa en la valoración de una solicitud. Su ponderación puede ser desconocida cuando la fuente no publica información suficiente para determinarla.

### Nota media

Representa la media del expediente académico de la estudiante. Es un dato distinto de la puntuación calculada por el sistema de admisión.

### Puntuación

Representa un valor numérico obtenido mediante un sistema de valoración. Su significado debe interpretarse dentro del sistema del máster correspondiente.

### Corte

Representa la prioridad y la puntuación del último estudiante admitido. No debe reducirse a un número sin conservar la prioridad asociada.

## 8. Relaciones entre conceptos

Las relaciones principales del dominio son:

- Una convocatoria contiene la oferta de másteres y los datos de admisión que corresponden a ella.
- Un máster puede estar relacionado con varias titulaciones.
- Cada relación entre un máster y una titulación determina una prioridad y puede incluir un requisito adicional.
- Cada máster dispone de sus propios criterios de valoración.
- Una adjudicación corresponde a un máster dentro de un contexto de admisión determinado.
- Una adjudicación puede disponer de un corte publicado o carecer de él.
- La puntuación de una solicitud depende de los criterios del máster y de los méritos de la estudiante.
- La posibilidad objetiva depende de la prioridad, la puntuación y la información de corte disponible.

## 9. Datos almacenados

Para analizar la HU001 se necesitan, como mínimo, los siguientes datos:

### Datos de la estudiante

- Titulación.
- Nota media del expediente.
- Certificados de idiomas y otros méritos relevantes.

### Datos del máster

- Código dentro de la convocatoria.
- Nombre del máster.
- Titulaciones relacionadas.
- Prioridad de cada titulación.
- Requisitos adicionales.
- Criterios de valoración y ponderaciones cuando estén publicadas.

### Datos de la adjudicación

- Convocatoria a la que pertenece.
- Prioridad del último estudiante admitido.
- Puntuación de corte, cuando exista.
- Estado o significado especial de la información publicada cuando no sea una puntuación ordinaria.

## 10. Valores calculados

El sistema deberá poder razonar sobre la puntuación que Claudia podría obtener según el sistema de valoración del máster.

Cuando todos los datos necesarios sean conocidos, podrá compararse esa puntuación con el corte correspondiente y teniendo en cuenta la prioridad.

Cuando existan méritos cuya valoración no se conozca de antemano, el análisis debe considerar los resultados posibles en lugar de inventar una puntuación exacta.

La clasificación final distingue entre:

- **Entrada segura:** Claudia cumpliría las condiciones de acceso incluso sin obtener puntuación adicional por los méritos cuya valoración se desconoce.
- **Entrada condicionada:** la entrada depende de cómo se valoren los méritos desconocidos.
- **Entrada imposible:** ni siquiera con la valoración máxima considerada alcanzaría las condiciones de acceso.

Estas conclusiones solo podrán calcularse cuando los datos disponibles permitan aplicar las reglas correspondientes.

## 11. Reglas e invariantes

- La prioridad debe interpretarse en relación con una titulación y un máster.
- Si una titulación no figura entre las titulaciones relacionadas con un máster, se considera RESTO.
- La puntuación debe interpretarse según el sistema de valoración del máster correspondiente.
- La nota media y la puntuación de admisión son conceptos diferentes.
- El corte debe conservar tanto la prioridad como la puntuación.
- La ausencia de corte no equivale a un corte numérico igual a cero.
- El código de seis cifras solo se considera identificador dentro del ámbito confirmado por las fuentes.
- Los requisitos adicionales deben conservar su descripción sin asumir que todos siguen el mismo formato.
- No se deben inventar ponderaciones que no estén publicadas.
- Los valores especiales de las fuentes deben interpretarse según su significado y no como números ordinarios.

## 12. Datos inválidos y errores

El modelo debe contemplar datos que no permitan representar correctamente un concepto del dominio.

Entre los casos que deben revisarse se encuentran:

- Una titulación o un máster sin la información necesaria para identificarlos.
- Una prioridad que no corresponda a ninguno de los valores conocidos.
- Una nota media fuera de la escala académica prevista.
- Una puntuación negativa o no numérica cuando se espera una puntuación ordinaria.
- Una ponderación que no respete la escala definida por el criterio de valoración.
- Una relación entre datos de fuentes que no pertenezcan a la misma convocatoria.
- Una nota de corte interpretada como ordinaria cuando la fuente indica un estado especial.

Los errores deben distinguir entre datos inválidos y situaciones válidas en las que simplemente no se dispone de información, como la ausencia de una nota de corte publicada.

## 13. Identidad e inmutabilidad

Los objetos de valor, como la prioridad, la nota media y la puntuación, no necesitan identidad independiente: su significado se determina por su valor.

Las entidades requieren una identidad coherente con su contexto. En particular, no debe asumirse que el código de un máster se mantiene estable entre convocatorias.

Los datos que describen un valor de dominio no deberían cambiar de forma inesperada después de su creación. La implementación deberá aplicar esta decisión de forma coherente con las reglas de cada concepto.

## 14. Estructura de módulos

Los archivos del dominio se organizan en el paquete `Master`:

- `master.py`: representación del máster.
- `adjudicacion.py`: representación de una adjudicación.
- `corte.py`: prioridad y puntuación del último estudiante admitido.
- `criterio.py`: criterios utilizados para valorar las solicitudes.
- `prioridad.py`: valores de prioridad.
- `puntuacion.py`: puntuación de admisión.
- `nota_media.py`: nota media del expediente.
- `titulacion.py`: titulación universitaria.
- `requisito.py`: requisitos adicionales.
- `errores.py`: errores del dominio.
- `__init__.py`: definición del paquete.

La estructura deberá revisarse si durante la implementación se observa que una relación entre conceptos está representada como un atributo del objeto equivocado.

## 15. Correspondencia entre dominio y código

Los archivos del paquete `Master` deben reflejar los conceptos identificados en este documento.

La correspondencia no significa que cada término del lenguaje ubicuo tenga que convertirse obligatoriamente en una clase independiente. La decisión depende de su significado, sus reglas y sus relaciones.

En particular, debe comprobarse que:

- La prioridad no se modele como una propiedad general del máster independiente de la titulación.
- La puntuación de admisión no se confunda con la nota media.
- El corte conserve la prioridad asociada.
- Una adjudicación sin corte se distinga de una adjudicación cuyo corte tenga un valor especial.
- Los criterios no reciban ponderaciones inventadas cuando las fuentes no las especifican.

## 16. Fuera de alcance

En este hito no se pretende:

- Descargar automáticamente las páginas del DUA.
- Implementar el análisis completo de las páginas web.
- Construir una interfaz de usuario.
- Garantizar una predicción de admisión cuando las fuentes no contienen información suficiente.
- Suponer que todos los másteres aplican el mismo sistema de valoración.
- Resolver mediante reglas inventadas los requisitos ambiguos publicados por las universidades.

El objetivo es establecer un modelo inicial correcto del problema antes de desarrollar estas funcionalidades.

## 17. Producto mínimamente viable

El primer producto mínimamente viable debe centrarse en un concepto independiente que permita comprobar las reglas del dominio sin requerir todavía el sistema completo.

La selección definitiva debe acordarse a partir de los issues del Milestone 0 y comprobarse con el responsable del producto antes de ampliar la implementación.

## 18. Entorno de desarrollo

El proyecto utiliza:

- Python 3.14.8.
- uv 0.12.23 para la gestión del entorno y las dependencias.
- mise 2026.9.18 para gestionar las versiones de las herramientas.

Las versiones y la configuración deben mantenerse coherentes con los archivos de configuración del repositorio.

## 19. Comprobaciones disponibles

Las comprobaciones deben incorporarse de forma gradual conforme se implementen las reglas del dominio.

Como mínimo, deberán verificarse las reglas que ya estén implementadas y comprobarse que los módulos se puedan importar correctamente.

Las comprobaciones concretas deben documentarse cuando estén configuradas; no se debe afirmar que existen pruebas, análisis estático o integración continua si todavía no se han añadido.
