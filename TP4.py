jasd##Fichier d'importation
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
stats_crimesx = pd.read_csv("interventionscitoyendo.csv")
liste_pdq = pd.read_csv("pdq_point.csv")
liste_arr = pd.read_csv("arrondissement_clean.csv")
stats_crimesx['ANNEE']=pd.DatetimeIndex(stats_crimesx['DATE']).year
stats_crimes = stats_crimesx[(stats_crimesx.ANNEE !=2020)]

##Merge de la table intervention et de la table arrondissement
table_merge = pd.merge(stats_crimes,liste_arr,on=["PDQ"])


### Statistique no.1 -- Crime commis -- ###
##Sommation (count() du nombre de crime par années (groupby)
crime_commis = stats_crimes.groupby(["ANNEE"]).count()["DATE"]
print("Crime commis")
print(crime_commis)
##Création d'un graphique a barre
crime_commis.plot(kind = "bar")
plt.show()

### Statistique no.2 --Crime violent commis -- ###
##Sommation (count() du nombre de crime par années (groupby) avec un filtre sur les catégories de crime
data_stats2 = stats_crimes[(stats_crimes.CATEGORIE == "Introduction") |(stats_crimes.CATEGORIE == "Infractions entrainant la mort")]
crime_violent = data_stats2.groupby(["ANNEE"]).count()["DATE"]
print("Crime Violent")
print(crime_violent)
##Création d'un graphique a barre
crime_violent.plot(kind = "bar")
plt.show()

### Statistique no.3 -- Moyenne de crime pour un arrondissement par année -- ###
##Calculé le nombre de département de police
nombre_arrond = stats_crimes["PDQ"].nunique()
##Le nombre de crime commis divisé par le nombre d'arrondissement
crime_moyen_arrondissement = crime_commis/nombre_arrond

print("Nombre de crime moyen pour un arrondissement typique par année")
print(crime_moyen_arrondissement)

### Statistique no.4 -- Moyenne de crime pour un arrondissement pour les 5 dernières années -- ###
##Faire une moyenne 5 ans de la statistique no3.
print("La moyenne annuelle de crime entre 2015 et 2019 pour un arrondissement typique est :",round(crime_moyen_arrondissement.mean()))


### Statistique no.5 --Moyenne de crime 5 dernières années par arrondissement -- ###
nbpdq = table_merge.groupby(["Arrondissement"]).count()["CATEGORIE"]
nombre_annees = stats_crimes["ANNEE"].nunique()
moyenne_par_arrondissement = nbpdq/nombre_annees
print("Moyenne annuelle de crime par arrondissement (5 dernières années)")
print(moyenne_par_arrondissement)





