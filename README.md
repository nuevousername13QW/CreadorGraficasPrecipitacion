# CreadorGraficasPrecipitacion
Visualización de Precipitaciones en Estaciones Meteorológicas
Este proyecto permite la visualización de datos de precipitación registrados en diferentes estaciones meteorológicas en Colombia. Utilizando Tkinter para la interfaz gráfica de usuario y pandas para la manipulación de datos, esta aplicación carga archivos CSV con información sobre precipitaciones, filtra los datos de estaciones específicas, y grafica los valores observados a lo largo del tiempo.

Funcionalidades
Cargar archivos CSV: Permite seleccionar un archivo CSV con datos meteorológicos a través de un cuadro de diálogo.
Filtrado por estaciones: Filtra los datos de precipitación para las estaciones de interés (LAGUNA DE LA PLAZA, MALPELO - DIMAR, y BORAUDO).
Visualización gráfica: Muestra gráficos de los valores de precipitación observados en las estaciones seleccionadas, con una línea de tiempo que facilita el análisis.

Estructura del CSV
El archivo CSV debe contener los siguientes campos:

CodigoEstacion: Código de la estación meteorológica.

CodigoSensor: Código del sensor de medición.

FechaObservacion: Fecha y hora de la observación.

ValorObservado: Valor de precipitación observado (en mm).

NombreEstacion: Nombre de la estación meteorológica.

Departamento: Departamento donde se encuentra la estación.

Municipio: Municipio de la estación.

ZonaHidrografica: Zona hidrográfica.

Latitud: Coordenada de latitud de la estación.

Longitud: Coordenada de longitud de la estación.

DescripcionSensor: Descripción del tipo de sensor.

UnidadMedida: Unidad de medida utilizada (e.g., mm para precipitación).

Requisitos:
Python 3.13.0,
Pandas,
Matplotlib,
Tkinter.
