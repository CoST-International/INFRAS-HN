<p align="left"><img src="https://infras-hn.org/images/logoB.png" height="114" width="338"></p>



# [InfraS](https://infras-hn.org)


- [Descripción y contexto](#descripción-y-contexto)
- [Guía del usuario](#guía-del-usuario)
    - [Arquitectura](#arquitectura)
    - [Uso del sistema](#uso-del-sistema)
    - [Guía de instalación](#Guía-de-instalación)
      - [Instalación del frontend](#instalación-del-frontend)
      - [Instalación del componenete OCDS](#Instalación-del-componenete-OCDS)
       - [Agregar información al esquema de MongoDB](#Agregar-información-al-esquema-de-MongoDB)
       - [Archivo config.json para el módulo SISOCS](#Archivo-configjson-para-el-módulo-SISOCS)
       - [Archivo config.json para el servidor](#Archivo-configjson-para-el-servidor)
- [Cómo contribuir](#Cómo-contribuir)
    - [Atribuciones](#atribuciones)
- [Código de conducta](#código-de-conducta)
    - [Nuestro compromiso](#our-pledge)
    - [Nuestras normas](#nuestras-normas)
    - [Nuestras responsabilidades](#nuestras-responsabilidades)
    - [Ámbito de aplicación](#ámbito-de-aplicación)
    - [Aplicación de este código](#aplicación-de-este-código)
    - [Atribución](#atribución)
- [Autores](#autores)
- [Información adicional](#información-adicional)
- [Licencia](#licencia)
- [Limitación de responsabilidades](#Limitación-de-responsabilidades)


## Descripción y contexto

InfraS es una plataforma diseñada por la Iniciativa de Transparencia en Infraestructura -CoST Honduras- con el objetivo de promover que la infraestructura pública se planee y conserve adecuadamente apostando a su sostenibilidad ambiental, social, institucional y económica.

[CoST Honduras](https://costhonduras.hn/) espera contribuir al logro de los [Objetivos de Desarrollo Sostenible (ODS)](https://www.un.org/sustainabledevelopment/es/objetivos-de-desarrollo-sostenible/) en el país al abordar los riesgos ambientales de los proyectos, analizar los recursos financieros para construir y mantener la infraestructura durante su vida útil, identificar afectación de las obras en grupos de población y entender la dinámica institucional sobre el manejo de las contrataciones públicas, identificando, a la vez, oportunidades de mejora para el desarrollo de infraestructura sostenible.


InfraS usa diversos datos oficiales entre los que destacan los publicados en el [Sistema de Información y Seguimiento a Obras y Contratos de Supervisión- SISOCS](https://sisocs.org/) y en el [Portal de Contrataciones Abiertas de Honduras](http://www.contratacionesabiertas.gob.hn/), los cuales cumplen con reconocidos estándares internacionales. InfraS presentará análisis por cada una de las áreas que componen la infraestructura sostenible, en el marco de compromisos de la [Alianza para el Gobierno Abierto de Honduras](http://www.gobiernoabiertohonduras.org/).

La herramienta está compuesta por cuatro componentes correspondientes a las dimensiones de la infraestructura sostenible. En cada dimensión se miden indicadores relevantes construidos a partir de los datos disponibles sobre los proyectos de infraestructura pública en Honduras. 
 
<p align="center"><img src="https://infras-hn.org/images/infras/dimensiones_infras.png" height="375" width="636"></p>

## Guía del usuario


### Arquitectura 

#### Dimensión Ambiental
<p align="center"><img src="https://infras-hn.org/images/infras/arquitectura_ambiental.png" height="414" width="710"></p>

#### Dimensión Institucional 

<p align="center"><img src="https://infras-hn.org/images/infras/arquitectura_institucional.png" height="405" width="710"></p>

#### Dimensión Social y Económica
<p align="center"><img src="https://infras-hn.org/images/infras/arquitectura_socialyeconomica.png" height="451" width="710"></p>


### Uso del sistema

#### Acceso
Los usuarios pueden ingresar al sitio por medio del enlace https://infras-hn.org/

#### Página de inicio

#### A) Barra de menú

La barra de menú contiene las siguientes opciones:

<p align="center"><img src="https://infras-hn.org/images/infras/infras-menu.PNG"></p>

1.	Dimensión Ambiental: enlace directo a los indicadores relacionados con la sostenibilidad ambiental.
2.	Dimensión Institucional: enlace directo a los indicadores relacionados con la sostenibilidad institucional.
3.	Dimensión Social: enlace directo a los indicadores relacionados con la sostenibilidad social.
4.	Dimensión Económica: es un enlace directo a los indicadores relacionados con la sostenibilidad económica.  


#### B) Dimensión Ambiental 
En este componente se presentan visualizaciones asociadas al licenciamiento ambiental, la ubicación de los proyectos en zonas ambientalmente sensitivas y en zonas prioritarias para la gestión de riesgos y de desastres de los proyectos de infraestructura pública. 

#### C) Dimensión Institucional 
En este componente se presenta un tablero de análisis sobre la eficiencia, apertura y transparencia en los procesos de contratación asociados a proyectos de infraestructura pública. 

#### D) Dimensión Social
Este componente presenta un tablero de análisis sobre los proyectos que han tenido algún impacto en reasentamientos. 

#### E) Dimensión Económica 
En este componente se presenta la distribución de la inversión actual en infraestructura por institución, sector y regiones del país. 

## Guía de instalación

### Instalación del frontend

##### Requerimientos:
* Python 2.7 o superior
* Django 1.6
* SQLite 3
* Pillow 1.8
* API Google Maps

#### Indicaciones:

La dimensión ambiental está desarrollada en Django 1.6, con base de datos en SQLite 3, la misma con el API Javascript de gooogle maps, para las dimensiones Institucional, Social y Económica se utiliza un objeto html iframe apuntando al su correspondiente informe de power bi:

* [Dimensión Institucional](https://app.powerbi.com/view?r=eyJrIjoiYjEwMzZjNGYtZjYzMS00MzVhLWJjOTItNmQ0Mjk4NDc1ZDQzIiwidCI6Ijg5NDQzNTY4LWJlZWMtNDFkMi04Yzc3LWU2MDFmYWIxNTVjYiJ9&pageName=ReportSection30219edae0097ec3abb8)
* [Dimensión Social](https://app.powerbi.com/view?r=eyJrIjoiYjEwMzZjNGYtZjYzMS00MzVhLWJjOTItNmQ0Mjk4NDc1ZDQzIiwidCI6Ijg5NDQzNTY4LWJlZWMtNDFkMi04Yzc3LWU2MDFmYWIxNTVjYiJ9&pageName=ReportSection30219edae0097ec3abb8)
* [Dimensión Económica](https://app.powerbi.com/view?r=eyJrIjoiMGIyNzQwZGYtNWZhZi00NDdmLWI5ZGItZjYyMTM5NTUxMGI4IiwidCI6Ijg5NDQzNTY4LWJlZWMtNDFkMi04Yzc3LWU2MDFmYWIxNTVjYiJ9)


## Cómo contribuir

La plataforma de divulgación para datos de infraestructura es un esfuerso de [CoST -la Iniciativa de Transparencia en Infraestructura](https://infrastructuretransparency.org/https://infrastructuretransparency.org/)- que tiene como objetivo apoyar y guiar a los miembros y socios de CoST para contribuir, explorar y reutilizar herramientas digitales de código abierto publicadas en nuestro [Repositorio de GitHub](https://github.com/infrastructure-transparency). Estas herramientas se pueden utilizar en el diseño e implementación de procesos de divulgación con el objetivo de mejorar la transparencia y la rendición de cuentas en el sector de infraestructura en todo el mundo.

CoST cree que los códigos fuentes abiertos desarrollados por nuestros miembros y socios deben estar a disposición del público para ayudarnos a contribuir a proporcionar infraestructuras de calidad, fortalecer las economías y mejorar vidas. 
Por ello, CoST anima a quienes contribuyen a la mejora de estas herramientas digitales a que compartan sus aportes con nosotros. 

Si al reutilizar esta herramienta digital, consideras que
* Has añadido alguna funcionalidad nueva con la que aportas valor para que más personas la reutilicen,
* Has hecho la herramienta más versátil para respaldar nuevas actualizaciones,
* Has corregido algunos errores existentes,
* O simplemente has mejorado la interfaz de usuario o la documentación de la misma.

Te invitamos a que devuelvas los progresos realizados al repositorio. Sigue estos pasos para contribuir a la herramienta:

1.	Haz una división del repositorio. 
2.	Desarrolla la nueva funcionalidad o realiza los cambios que crees que añaden valor a la herramienta.
3.	Haz una “solicitud de eliminar” documentando en detalle los cambios propuestos en el repositorio.
4.	En ese caso, tu nombre quedará registrado en la lista de atribuciones.

Si no has contribuido al repositorio, pero la herramienta te ha resultado útil, nos encantaría conocer tu experiencia. Cuéntanos tu experiencia en un “Issue” o por correo electrónico a opencode@infrastructuretransparency.org


### Atribuciones
Al enviar una solicitud de adhesión de nuevo código (“pull requests”), puedes compartirnos tu nombre de usuario y organización para añadirlo a la lista de contribuciones en el Readme.md.

## Código de conducta

### Nuestro compromiso
En aras de fomentar un entorno abierto y amigable, nosotros, como equipo de colaboradores y a cargo del mantenimiento de este repositorio, nos comprometemos a hacer de la participación en nuestro portal y en nuestra comunidad una experiencia libre de acoso para todos, independientemente de la edad, discapacidad, nacionalidad, origen étnico, nivel de experiencia, apariencia personal, raza, religión, identidad, género y/o orientación sexual. 

### Nuestras normas
Algunos ejemplos de comportamientos que contribuyen a crear un entorno positivo son:
* Utilizar un lenguaje de bienvenida e inclusivo.
* Ser respetuoso con los diferentes puntos de vista y experiencias.
* Aceptar con gentileza las críticas constructivas.
* Centrarse en lo que es mejor para la comunidad.
* Mostrar empatía hacia otros miembros de la comunidad.

Ejemplos de comportamiento inaceptable por parte de los participantes son:
* El uso de lenguaje o imágenes sexualizadas, atenciones e insinuaciones sexuales no deseadas.
*	Ofensas, comentarios insultantes/despectivos y ataques personales o políticos.
*	Acoso público o privado.
*	Publicar información privada de otros, como una dirección física o electrónica, sin permiso explícito.
*	Otras conductas que puedan considerarse razonablemente inapropiadas en un entorno profesional.

### Nuestras responsabilidades

Los que dan mantenimiento y colaboradores del proyecto son responsables de aclarar las normas de comportamiento aceptable y se espera que tomen medidas correctivas adecuadas y justas en respuesta a cualquier caso de comportamiento inaceptable.
Los responsables del mantenimiento de las Plataformas de Divulgación de datos sobre Infraestructura, tienen el derecho y la responsabilidad de eliminar, editar o rechazar comentarios, confirmaciones, códigos, ediciones wiki, cuestiones y otras contribuciones que no se ajusten a este Código de Conducta, o prohibir temporal o permanentemente a cualquier colaborador por otros comportamientos que consideren inapropiados, amenazantes, ofensivos o perjudiciales.

### Ámbito de aplicación

Este Código de Conducta se aplica tanto en los espacios de la Plataforma de Transparencia en Infraestructura como en los espacios públicos cuando una persona representa a CoST o a su comunidad. Ejemplos de representación de CoST o de la comunidad incluyen el uso de una dirección de correo electrónico oficial, la publicación a través de una cuenta oficial en las redes sociales o la actuación como representante designado en un evento en línea o fuera de línea. La representación de un CoST puede ser definida y aclarada por los responsables de la Plataforma de Transparencia en Infraestructura.

### Aplicación de este código

Los casos de comportamiento abusivo, acosador o inaceptable pueden denunciarse poniéndose en contacto con el responsable de este repositorio o en opencode@infrastructuretransparency.org.
Todas las denuncias serán revisadas e investigadas y darán lugar a una respuesta que se considere necesaria y adecuada a las circunstancias. El equipo de CoST está obligado a mantener la confidencialidad sobre el denunciante de un incidente.
Los encargados del mantenimiento de las Plataformas de Divulgación de datos sobre Infraestructura que no sigan o hagan cumplir el Código de Conducta pueden enfrentarse a repercusiones temporales o permanentes según lo determine CoST.

### Atribución

Este Código de Conducta es una adaptación del [Pacto de Colaboradores](https://www.contributor-covenant.org/), versión 1.4, disponible en http://contributor-covenant.org/version/1/4.


## Autores
La Iniciativa CoST Honduras es el autor originales de [InfraS](https://infras-hn.org).

## Información adicional

* [Acerca de CoST Honduras](https://infrastructuretransparency.org/where-we-work/cost-honduras/)

## Licencia
GNU GPLv3
Los permisos de esta licencia copyleft están condicionados a poner a disposición el código fuente completo de los trabajos con licencia y las modificaciones, que incluyen trabajos mayores que utilizan una obra con licencia, bajo la misma licencia. Las notificaciones de derechos de autor y de licencia deben conservarse. Los colaboradores proporcionan una concesión expresa de derechos de patente.

## Limitación de responsabilidades
CoST no se hace responsable, bajo ninguna circunstancia, de los daños e indemnizaciones, morales o patrimoniales; directos o indirectos; secundarios o especiales; o por vía de consecuencia prevista o imprevista que pudieran surgir:

* Bajo ningún concepto de propiedad intelectual, negligencia o en detrimento de otra parte de la teoría.
* Como consecuencia del uso de esta herramienta digital, incluyendo, pero sin limitarse a los defectos de la herramienta digital, o la pérdida o inexactitud de datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o mal funcionamiento de los ordenadores vinculados al uso de esta herramienta digital.
