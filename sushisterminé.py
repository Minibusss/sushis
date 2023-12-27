import sushis1 as ma

saumon = 8.3
thon = 8.3
crevette = 8.3
ommelette = 1/6
riz = 15
fromage = 4
concombre = 37.5
avocat = 10
nori = 1/12
vinaigre = 1.1

def fonction1():
    print(ma.intro)
    print(ma.choix_sushis)
    recette = input("choisissez une recette que vous souhaitez manger: ").strip()
    print("lol")
    if recette=='1':
        nombre = int(input("combien de maki souhaiter vous? "))
        saumon1 = round(saumon*nombre)
        nori1 = round(nori*nombre)
        riz1 = round(riz*nombre)
        vinaigre1 = round(vinaigre*nombre)
        print(F"\ningrédient necessaire pour faire vos {nombre} makis au saumon:\n -{saumon1} grammes de saumon\n-{nori1} feuilles de nori\n-{vinaigre1} centilitre de vinaigre a sushis\n-{riz1} grammes de riz a sushis")
        print(ma.cuisson_riz)
        print(ma.tips1)
        print(ma.recette[0])
        print(ma.tips2)

    if recette=='2':
        nombre = int(input("combien de maki souhaiter vous? "))
        crevette1 = round(crevette*nombre)
        nori1 = round(nori*nombre)
        riz1 = round(riz*nombre)
        vinaigre1 = round(vinaigre*nombre)
        print(F"\ningrédient necessaire pour faire vos {nombre} makis à la crevette:\n -{crevette1} grammes de crevette\n-{nori1} feuilles de nori\n-{vinaigre1} centilitre de vinaigre a sushis\n-{riz1} grammes de riz a sushis")
        print(ma.cuisson_riz)
        print(ma.tips1)
        print(ma.recette[1])
        print(ma.tips2)

    if recette=='3':
        nombre = int(input("combien de maki souhaiter vous? "))
        fromage1 = round(fromage*nombre)
        nori1 = round(nori*nombre)
        concombre1 = round(concombre*nombre)
        riz1 = round(riz*nombre)
        vinaigre1 = round(vinaigre*nombre)
        print(F"\ningrédient necessaire pour faire vos {nombre} makis fromage frais concombre:\n -{fromage1} grammes de fromage frais\n-{nori1} feuilles de nori\n-{riz1} grammes de riz a sushis\n-{vinaigre1} centilitre de vinaigre a sushis\n-{concombre1} grammes de concombre")
        print(ma.cuisson_riz)
        print(ma.tips1)
        print(ma.recette[2])
        print(ma.tips2)

    if recette=='4':
        nombre = int(input("combien de maki souhaiter vous? "))
        ommelette1 = round(ommelette*nombre)
        nori1 = round(nori*nombre)
        riz1 = round(riz*nombre)
        vinaigre1 = round(vinaigre*nombre)
        print(F"\ningrédient necessaire pour faire vos {nombre} makis ommelette japonaise:\n -{ommelette1} oeufs\n-{nori1} feuilles de nori\n-{vinaigre1} centilitre de vinaigre a sushis\n-{riz1} grammes de riz a sushis")
        print(ma.cuisson_riz)
        print(ma.tips1)
        print(ma.recette[3])
        print(ma.tips2)

    if recette=='5':
        nombre = int(input("combien de maki souhaiter vous? "))
        avocat1 = round(avocat*nombre)
        nori1 = round(nori*nombre)
        riz1 = round(riz*nombre)
        vinaigre1 = round(vinaigre*nombre)
        print(F"\ningrédient necessaire pour faire vos {nombre} makis a l'avocat:\n -{avocat1} grammes d'avocat\n-{nori1} feuilles de nori\n-{vinaigre1} centilitre de vinaigre a sushis\n-{riz1} grammes de riz a sushis")
        print(ma.cuisson_riz)
        print(ma.tips1)
        print(ma.recette[4])
        print(ma.tips2)

    if recette=='6':
        nombre = int(input("combien de maki souhaiter vous? "))
        thon1 = round(thon*nombre)
        nori1 = round(nori*nombre)
        riz1 = round(riz*nombre)
        vinaigre1 = round(vinaigre*nombre)
        print(F"\ningrédient necessaire pour faire vos {nombre} makis au thon:\n -{thon1} grammes de thon\n-{nori1} feuilles de nori\n-{vinaigre1} centilitre de vinaigre a sushis\n-{riz1} grammes de riz a sushis")
        print(ma.cuisson_riz)
        print(ma.tips1)
        print(ma.recette[5])
        print(ma.tips2)
        return
    



fonction1()
