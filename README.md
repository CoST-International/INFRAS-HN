<img src="https://infras-hn.org/images/logoB.png" height="114" width="338"></p>



# [SISOCS APP - OCDS](https://infras-hn.org)

[English documentation](README_en.MD)

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

INFRAS es una herramienta....

## Guía del usuario


### Arquitectura 

Dimensión Ambiental
<p align="center"><img src="https://infras-hn.org/images/Arquitectura%20Ambiental.png"></p>
Dimensión Social,Institucional y Económica 
<p align="center"><img src="https://infras-hn.org/images/Arquitectura%20Institucional%20Social%20Economica.png"></p>

### Uso del sistema

#### Acceso
Existen dos formas para ingresar al sistema, en la primera debe de buscar en su navegador de confianza SISOCS APP y la segunda forma consiste en ingresar por medio de un enlace (https://infras-hn.org/) que lo llevará automáticamente al sitio.

#### Página de inicio

#### A) Barra de menú

La barra de menú contiene las siguientes opciones:

<p align="center"><img src="https://infras-hn.org/images/infras/infras-menu.PNG"></p>

1.	Dimensión Ambiental.
2.	Dimensión Institucional.
3.	Dimensión Social.
4.	Dimensión Económica. 


#### B) Dimensión Ambiental 
#### C) Dimensión Institucional 
#### D) Dimensión Social
#### E) Dimensión Económica 

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
