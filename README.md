# TextAnalyzator
 
 Popis projektu
ONLINE PYTHON AKADEMIE​/PROJEKT: TEXT ANALYZÁTOR​/ZADÁNÍ PROJEKTU​/POPIS PROJEKTU
Na závěr tě čeká velký projekt, ve kterém si vyzkoušíš všechno, co jsme se v tomto kurzu společně naučili. Tvým cílem bude vytvořit Textový analyzátor - program, který se bude umět prokousat libovolně dlouhým textem a zjistit o něm různé informace. Ještě než začneš, doporučíme ti použít námi předpřipravené texty. Kód se ti pak bude lépe kontrolovat. Tyto texty jsou dostupné zde.

Pojď se podívat, co všechno by tvůj program měl umět:

1. Na začátku přivítá uživatele.
2. Vyžádá si od uživatele přihlašovací jméno a heslo.
3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

Registrováni jsou následující uživatelé:

| USER |   PASSWORD  |
-----------------------
| bob  |     123     |
| ann  |    pass123  |
| mike | password123 |
| liz  |    pass123  |
Pokud se ti tento úkol bude zdát složitý, prověř, jestli zadané údaje jsou mezi registrovanými, ale neřeš spojení uživatel - heslo.

4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS.

5. Pro vybraný text spočítá následující statistiky:
- počet slov,
- počet slov začínajících velkým písmenem,
- počet slov psaných velkými písmeny,
- počet slov psaných malými písmeny,
- počet čísel (ne cifer!).

6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:

- 1 * 1
 - 2 *********** 11
 - 3 *************** 15
 - 4 ********* 9
 - 5 ********** 10

V textu, ze kterého byl vytvořen tento graf, je tedy pouze 1 jednopísmené slovo, 11 slov složených ze dvou písmen, a tak dále.

7. Program spočítá součet všech čísel (ne cifer!) v textu. Výsledkem tohoto součtu v následujícím textu by teby bylo číslo 8500:

"that rises sharply some 1000 feet above
Twin Creek Valley to an elevation of more
than 7500 feet above sea level. The butte
is located just north of US 30N"


