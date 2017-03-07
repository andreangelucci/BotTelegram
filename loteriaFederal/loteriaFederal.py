import string
import os
import urllib2
import sys
import sendgrid
from sendgrid.helpers.mail import *
from Resultado import Resultado
from bs4 import BeautifulSoup
from cookielib import CookieJar

reload(sys)
sys.setdefaultencoding('utf-8')

urlLoteria = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/federal"
    
def crawler():
    #busca o resultado da loteria federal.

    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    request = opener.open(urlLoteria)
    resultadoUrl = BeautifulSoup(request, "html.parser")    

    if (resultadoUrl is None):
        return

    concurso = resultadoUrl.find(attrs={"class", "title-bar"})    
    classResultado = resultadoUrl.find(attrs={"class":"resultado-loteria"})    
    strConcurso = concurso.h2.span.text
    strResultados = concurso.h2.span.text+ "\n\n"
    ganhador = resultadoUrl.find(attrs={"class", "feedback feedback-warning no-margin milli"})
    strResultados = strResultados+ ganhador.p.text+ "\n\n"    
    for resultados in classResultado.tbody.findAll('tr'):
        objResultado = Resultado()
        objResultado.premio = resultados.contents[1].text
        objResultado.set_resultado(resultados.contents[3].text)
        objResultado.valor = resultados.contents[5].text 
        strResultados = strResultados + objResultado.printar()

    return strResultados

