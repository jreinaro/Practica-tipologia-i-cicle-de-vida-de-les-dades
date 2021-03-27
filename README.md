# Repositori propietat de Núria Aguilera Sánchez i Joan Antoni Reina i Romero

## Màster Universitari en Ciència de Dades (Universitat Oberta de Catalunya, UOC).

### Assignatura:  M2.951.Tipologia i cicle de vida de les dades. Aula 1.
### Practica 1: *Web scraping*.


***EQUIP DE TREBALL:***

L'equip ha estat format per Núria Aguilera i Joan Antoni Reina. Ambdós cursant el màster en Ciència de Dades a la Universitat Oberta de Catalunya (UOC) i amb llargues trajectòries profesionals en el món de la consultoria tecnològica i l'empresa.

***DESCRIPCIÓ DE LA PRÀCTICA:***

Per la realització d'aquesta pràctica de *Web scraping* s'ha escollit la temàtica de les criptomonedes, un àmbit on la tecnologia i les finances conflueixen, de màxima actualitat i amb un evident desenvolupament futur. On l'objectiu ha estat l'elaboració d'un *dataset* mitjançant *Python* que conté informació al voltant de la cotització al tancament del darrer dia, de les cent criptomonedes més importants per capitalització. De forma que resulta de gran utilitat analítica per als potencials inversors. 

***CONTINGUTS:***

* Document en format pdf amb la resolució de la pràctica: PRA1_Criptomonedes_NA_JAR_Web_Scraping.pdf
* Arxiu Jupyter Notebook amb el codi Python: Criptomonedes_Historical_Data.py
* *Dataset*: Criptomonedes_Historical_Data_20210327.csv

***REQUERIMENTS TECNICS***

Per l'execució de l'script es necessari la instal·lació de les seguents llibreries:
pip install pandas
pip install request
pip install beautifulsoup
pip install Selenium

Es necessari instal·lar cromedriver, per això cal:
- Descarregar a:  https://sites.google.com/a/chromium.org/chromedriver/home
- Descomprimir i guardar a la C:/

El fitxer *python* està preparat per executar-se automaticament per exemple a partir d'una tasca programada de windows, on cada dia executaria el codi *python* i crearia un fitxer amb la informació obtinguda.

***DOI:*** (https://zenodo.org/record/4641835#.YF8ap69KiUl)
