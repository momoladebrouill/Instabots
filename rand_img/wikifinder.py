from urllib.request import urlopen

def extract_text(page):
    byte = urlopen(page).read()   #en octet
    code = byte.decode('utf-8')
    return code

def extract_liens(text):
    i=0
    extr=[]
    ls=[]
    while '<a ' in text[i:] :
        i0 = text.find('<a ',i)
        i1 = text.find('</a>',i)+4
        bloc=text[i0:i1]
        deb=bloc.find('href="')+6
        fin=bloc.find('"',deb)
        bloc=bloc[deb:fin]
        if bloc.startswith('/wiki/') and not ':' in bloc:
            ls.append('https://fr.wikipedia.org'+bloc)
        i = i1
    return ls
def extract_titre(text):
    deb=text.find('<title>')+7
    fin=text.find('</title>')
    titre=text[deb:fin]
    titre=titre[:titre.find(' — Wikipédia')]
    return titre

def extract_titres(page):
    byte = urlopen(page).read()   #en octet
    code = byte.decode('utf-8')
    text=code[:200]
    deb=text.find('<title>')+7
    fin=text.find('</title>')
    return text[deb:fin]

