import string
import os
import urllib2
import sys
import sendgrid
from bs4 import BeautifulSoup
from cookielib import CookieJar

reload(sys)
sys.setdefaultencoding('utf-8')

urlLoteria = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina/"
    
def crawler():
    #busca o resultado da loteria federal.

    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    request = opener.open(urlLoteria)
    resultadoUrl = BeautifulSoup(request, "html.parser")    

    if (resultadoUrl is None):
        return

    concurso = resultadoUrl.find(attrs={"class", "title-bar"})
    strConcurso = concurso.h2.span.text
    classResultado = resultadoUrl.find(attrs={"class":"resultado-loteria"})    
    strResultados = "Resultado:"
    for resultados in classResultado.ul.findAll('li'):
        strResultados = strResultados + " "+ resultados.text

    return strResultados    

if (__name__ == "__main__"):
    crawler()

