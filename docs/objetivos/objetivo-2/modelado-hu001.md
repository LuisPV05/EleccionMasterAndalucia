# Modelo de dominio de HU001

## Historia y alcance

**HU001: No sé en qué másteres tengo posibilidades objetivas de entrar.** Claudia está terminando Ingeniería Informática, mención en Tecnologías de la Información, tiene una nota media de 7,061 y acredita inglés B2. Necesita valorar sus posibilidades de acceso a másteres públicos de Andalucía usando tres fuentes del Distrito Único Andaluz (DUA): catálogo, notas de corte de la última adjudicación y fichas de los másteres.

El Milestone 0 entrega el modelo del dominio, sin scraping, interfaz ni lógica que calcule las posibilidades finales. Las decisiones de modelado deben corresponderse con los issues de HU001.

## Lenguaje ubicuo y decisiones

- **Convocatoria:** contexto de admisión al que pertenecen los datos. El código de seis cifras del máster solo se considera único dentro de una convocatoria; no se asume que sea estable entre convocatorias.
- **Máster:** estudio ofertado. Tiene código y nombre, los accesos admitidos y los criterios de valoración.
- **Titulación:** grado universitario desde el que se solicita el acceso.
- **Acceso:** relación entre una titulación y un máster. La prioridad y el requisito adicional pertenecen a esta relación, no al máster en abstracto. Si la titulación no aparece expresamente en la fuente, su prioridad es `RESTO`.
- **Prioridad:** `ALTA`, `MEDIA`, `BAJA` o `RESTO`.
- **Requisito adicional:** condición descrita en la ficha del máster. Se conserva la descripción publicada y se distingue si es obligatoria o informativa cuando esa distinción esté respaldada por la fuente.
- **Criterio:** aspecto usado para valorar la solicitud. La ponderación puede ser desconocida; desconocida no significa cero.
- **Nota media:** dato académico de Claudia, en la escala de 0 a 10 descrita en el problema.
- **Puntuación:** resultado del sistema de valoración de un máster; no es intercambiable con la nota media.
- **Adjudicación:** información de admisión correspondiente a un máster y una convocatoria.
- **Corte:** prioridad y puntuación del último estudiante admitido, o un estado especial publicado por la fuente.
- **Posibilidad objetiva:** conclusión posterior sobre entrada segura, condicionada a méritos cuya valoración se desconoce o imposible bajo la valoración máxima considerada. Calcularla queda fuera de este milestone.

## Decisiones de modelado

- `Master` y `Adjudicacion` se representan como entidades porque se refieren a estudios ofertados y a un resultado de admisión dentro de su contexto.
- `Titulacion`, `Prioridad`, `Acceso`, `Requisito`, `Criterio`, `NotaMedia`, `Puntuacion` y `Corte` representan valores del dominio, no identidades independientes.
- `Acceso` agrupa titulación, prioridad y requisito para evitar asignar al máster una prioridad que cambia según la titulación.
- Los datos inmutables se representan con objetos de valor congelados. Las validaciones solo deben codificar reglas apoyadas por la HU, las fuentes o los issues.

## Reglas e invariantes conocidas

- El código de seis cifras relaciona las fuentes dentro de una convocatoria; no debe tratarse como identidad permanente entre convocatorias.
- Una titulación tiene una prioridad dentro de cada relación de acceso a un máster.
- Un mismo máster no debe repetir una relación de acceso para la misma titulación.
- La nota media está entre 0 y 10; una puntuación ordinaria no puede ser negativa ni no finita.
- La ponderación no publicada se representa como desconocida (`None`), no como cero.
- Un corte numérico necesita prioridad y puntuación.
- `** 0,01` significa que entraron todas las personas de prioridad `RESTO` o superior; se representa como estado especial conservando `RESTO`, no como puntuación ordinaria 0,01.
- `AÚN SIN ADJ.` significa que aún no hay adjudicación publicada y no equivale a un corte de cero.
- Los requisitos publicados como texto libre se conservan sin inferir estructura que la fuente no proporcione.

## Fuera de alcance

No se implementan la extracción automática de páginas del DUA, la interfaz, el cálculo completo de puntuaciones ni la clasificación final de posibilidades. Tampoco se inventan ponderaciones ni reglas para requisitos ambiguos.

## Correspondencia con el código

- `master.py`: máster y sus accesos y criterios.
- `acceso.py`: relación entre titulación, prioridad y requisito.
- `adjudicacion.py`: contexto de adjudicación y corte.
- `corte.py`: corte numérico y estados especiales.
- `criterio.py`, `prioridad.py`, `puntuacion.py`, `nota_media.py`, `titulacion.py` y `requisito.py`: valores del dominio.
- `errores.py`: excepción común para datos incompatibles con las reglas del dominio.

La correspondencia definitiva entre cada elemento y su issue debe comprobarse en GitHub antes de cerrar el PR. Este documento resume las decisiones de dominio; no sustituye los issues ni debe duplicar su discusión completa.
