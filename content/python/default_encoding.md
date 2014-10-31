Title: Výchozí kódování v Pythonu
Date: 2014-04-28 16:47
Category: Blog
Tags: python, I/O
Author: Marek Nožka
Summary: Jak nastavit Python, aby správně tiskl
         řetězce obsahující diakritiku.


Občas se mi stane, že spouštím v Linuxu Python skript vytvořený ve Windows.
Nejčastěji je to nějaká studentská práce, domácí úkol nebo něco podobného.
Většinou není co řešit a program si prostě spustím, ale občas dělá problém
diakritika v unicode řetězcích. Třeba:

    :::python
    cislo = raw_input(u'napiš nějaké číslo')
    .....
    f = open('pokus.txt', 'w')
    f.write('Loď čeří kýlem vodu v úžině')
    .....

Python se snaží v těchto situacích unicode řetězec konvertovat do
příslušné znakové sady. Problém je, že neví, která znaková sada je ta
"příslušná" a proto končí s chybovým hlášením:

    :::pycon
    Traceback (most recent call last):
    File "kodovani.py", line 30, in <module>
        f.write(cestina)
    UnicodeEncodeError: 'ascii' codec can't encode character u'\u010f'
    in position 2: ordinal not in range(128)

Nejdřív to, co problémy nedělá: S tímto kódem problémy nejsou, protože kódování
pro standardní vstup/výstup je nastaveno na `UTF-8`.

    :::python
    import sys

    print "default encoding: ", sys.getdefaultencoding()

    cestina = u'Loď v úžině\n'

    print cestina              # tohle je OK
    sys.stdout.write(cestina)  # tohle taky
    # prototože
    print (sys.stdin.encoding, sys.stdout.encoding)

Pokud je třeba nějak měnit kódování standardního vstupu/výstupu je to možné
udělat jednoduše přes proměnnou prostředí `PYTHONIOENCODING`. Výstup potom
vypadá takto:

    :::console
    $ PYTHONIOENCODING=cp1250 ./kodovani.py
    default encoding:  utf-8
    Loï v úin

    Loï v úinì
    ('cp1250', 'cp1250')

Default encoding zůstalo stejné, změnilo se jen kódování standardního
vstupu/výstupu. Jak tedy nastavit `defaultencoding`?. To se totiž projeví u
otevřených souborů nebo například u vestavěné funkce `raw_input()`.

Nejjednodušší je použít funkci `sys.setdefaultencoding()`. Má to ale jeden malý
háček. Takto funkce je dostupná pouze při spuštění Pythonu. Dále se setkáme s
chybovým hlášením.

    :::pycon
    Traceback (most recent call last):
    File "kodovani.py", line 12, in <module>
        sys.setdefaultencoding("utf-8")
    AttributeError: 'module' object has no attribute 'setdefaultencoding'

První fígl je použít funkci `reload()`:

    :::python
    import sys
    reload(sys)  # to enable `setdefaultencoding` again
    sys.setdefaultencoding("UTF-8")

nebo

    :::python
    reload(sys).setdefaultencoding("UTF-8")

Druhý fígl je spustit Python s parametrem `-S`. Ten zakáže automatický import
modulu `site`, který výchozí znakovou sadu nastavuje a funkci
`setdefaultencoding` poté znepřístupní.

    :::python
    #!/usr/bin/python2.7 -S

    import sys
    sys.setdefaultencoding("utf-8")
    import site

Výše jsem uvedl řešení pro jeden konkrétní zdrojový kód. Pokud požadujeme
**globální nastavení** stačí vytvořit soubor `sitecustomize.py` a umístit ho
někam do `PYTHONPATH` respektive do `sys.path`.

    :::python
    import sys
    sys.setdefaultencoding('UTF-8')

Odkazy:
: <http://stackoverflow.com/questions/11741574/how-to-set-the-default-encoding-to-utf-8-in-python>
: <http://stackoverflow.com/questions/2276200/changing-default-encoding-of-python>
: <http://stackoverflow.com/questions/7105441/how-to-set-default-encoding-in-python-setdefaultencoding-function-does-not-ex>
