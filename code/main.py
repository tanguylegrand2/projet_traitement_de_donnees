import matplotlib.pyplot as plt
from agregation_temporelle import Agregation_temporelle
from jointure import Jointure
from normalisation import Normalisation
from table import Table
from moyenne import Moyenne
from pipeline import Pipeline
from boxplot import Boxplot
from centrage import Centrage
from ecart_type import Ecart_type
from variance import Variance
from fenetrage import Fenetrage
from datetime import datetime
from datetime import timedelta
from sort import Sort
from add_rows import Add_rows
from moyenne_glissante import MoyenneGlissante



table_no_import = Table(False, variables=['age', 'taille', 'poids', 'nom', 'bazard'], data={'age': ['mq',100, 9, 7, 54, 0.14, 40, 2, 45]*10, 
                                                                                            'taille' : ['mq', 170, 140, 170, 190, 200, 150, 195, 225]*10,
                                                                                            'poids': ['mq', 'mq', 'mq', 'mq', 'mq', 'mq', 'mq', 'mq', 'mq']*10,
                                                                                            'nom' : ['Laurent', 'Clara','Lucas', 'Laurent', 'Clara','Lucas', 'Laurent', 'Clara','Lucas']*10,
                                                                                            'bazard': [12, 'Tomate', 'mq', 12, 'Tomate', 'mq', 12, 'Tomate', 'mq']*10})


data_elec_2013 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_électricité\\2013-02.json.gz", format_fichier="json.gz", delimiter=";")
data_elec_2014 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_électricité\\2014-02.json.gz", format_fichier="json.gz", delimiter=";")
data_elec_2015 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_électricité\\2015-02.json.gz", format_fichier="json.gz", delimiter=";")
data_elec_2016 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_électricité\\2016-02.json.gz", format_fichier="json.gz", delimiter=";")
data_elec_2017 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_électricité\\2017-02.json.gz", format_fichier="json.gz", delimiter=";")
data_elec_2018 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_électricité\\2018-02.json.gz", format_fichier="json.gz", delimiter=";")

data_meteo_2013 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_météo\\synop.201302.csv.gz", format_fichier='csv.gz')
data_meteo_2014 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_météo\\synop.201402.csv.gz", format_fichier='csv.gz')
data_meteo_2015 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_météo\\synop.201502.csv.gz", format_fichier='csv.gz')
data_meteo_2016 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_météo\\synop.201602.csv.gz", format_fichier='csv.gz')
data_meteo_2017 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_météo\\synop.201702.csv.gz", format_fichier='csv.gz')
data_meteo_2018 = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\données_météo\\synop.201802.csv.gz", format_fichier='csv.gz')

data_station = Table(importe=True, chemin="C:\\Users\\Riyad\\Documents\\GitHub\\Projet_traitement_donn-es\\Donnees\\postesSynopAvecRegions.csv", format_fichier='csv', delimiter=",")


data_meteo_2013.change_type(['ff', 'sw', 'w1', 't'], float)
data_meteo_2014.change_type(['ff', 'sw', 'w1', 't'], float)
data_meteo_2015.change_type(['ff', 'sw', 'w1', 't'], float)
data_meteo_2016.change_type(['ff', 'sw', 'w1', 't'], float)
data_meteo_2017.change_type(['ff', 'sw', 'w1', 't'], float)
data_meteo_2018.change_type(['ff', 'sw', 'w1', 't'], float)

data_meteo_2013.set_date('date', format_date="%Y%m%d%H%M%S")
data_meteo_2014.set_date('date', format_date="%Y%m%d%H%M%S")
data_meteo_2015.set_date('date', format_date="%Y%m%d%H%M%S")
data_meteo_2016.set_date('date', format_date="%Y%m%d%H%M%S")
data_meteo_2017.set_date('date', format_date="%Y%m%d%H%M%S")
data_meteo_2018.set_date('date', format_date="%Y%m%d%H%M%S")

data_elec_2013.set_date('date_heure', format_date="%Y-%m-%dT%H:%M:%S%z")
data_elec_2014.set_date('date_heure', format_date="%Y-%m-%dT%H:%M:%S%z")
data_elec_2015.set_date('date_heure', format_date="%Y-%m-%dT%H:%M:%S%z")
data_elec_2016.set_date('date_heure', format_date="%Y-%m-%dT%H:%M:%S%z")
data_elec_2017.set_date('date_heure', format_date="%Y-%m-%dT%H:%M:%S%z")
data_elec_2018.set_date('date_heure', format_date="%Y-%m-%dT%H:%M:%S%z")
data_elec = [data_elec_2013.data['consommation_brute_electricite_rte'], data_elec_2014.data['consommation_brute_electricite_rte'], data_elec_2015.data['consommation_brute_electricite_rte'], data_elec_2016.data['consommation_brute_electricite_rte'], data_elec_2017.data['consommation_brute_electricite_rte'], data_elec_2018.data['consommation_brute_electricite_rte']]
X = [2013, 2014, 2015, 2016, 2017, 2018]

fig, ax = plt.subplots()

ax.boxplot(data_elec)
plt.show()


pip_meteo = Pipeline()


pip_meteo.add_operation(Add_rows(data_meteo_2014))
pip_meteo.add_operation(Add_rows(data_meteo_2015))
pip_meteo.add_operation(Add_rows(data_meteo_2016))
pip_meteo.add_operation(Add_rows(data_meteo_2017))
pip_meteo.add_operation(Add_rows(data_meteo_2018))
result_meteo = pip_meteo.process(data_meteo_2013)

pip_elec = Pipeline()
pip_elec.add_operation(Add_rows(data_elec_2014))
pip_elec.add_operation(Add_rows(data_elec_2015))
pip_elec.add_operation(Add_rows(data_elec_2016))
pip_elec.add_operation(Add_rows(data_elec_2017))
pip_elec.add_operation(Add_rows(data_elec_2018))
pip_elec.add_operation(Sort(data_elec_2013.var_date))
pip_elec.add_operation(MoyenneGlissante(timedelta(days=150, seconds=0, microseconds=0), ['consommation_brute_electricite_rte']))

result_elec = pip_elec.process(data_elec_2013)
fig, ax = plt.subplots()

ax.boxplot(result_elec[-1].data['temps_fenetrage'], result_elec[-1].data['moyenne_glissante_consommation_brute_electricite_rte'])
plt.show()


pip_json = Pipeline()
pip_json.add_operation(Add_rows(data_elec_2014))
pip_json.add_operation(Add_rows(data_elec_2015))
pip_json.add_operation(Agregation_temporelle(timedelta(days=1, seconds=0, microseconds=0), ['consommation_brute_electricite_rte']))
result_json = pip_json.process(data_elec_2013)

pip_csv = Pipeline()
#pip_csv.add_operation(Fenetrage(datetime.strptime('20130501030000', "%Y%m%d%H%M%S"), datetime.strptime('20130501150000', "%Y%m%d%H%M%S")))
pip_csv.add_operation(Add_rows(data_meteo_2014))
pip_csv.add_operation(Add_rows(data_meteo_2015))

pip_csv.add_operation(Agregation_temporelle(timedelta(days=1, seconds=0, microseconds=0), ['t']))
pip_csv.add_operation(Jointure(result_json[-1].var_date, result_json[-1]))
pip_csv.add_operation(Sort('temps_fenetrage'))
pip_csv.add_operation(MoyenneGlissante(timedelta(days=14, seconds=0, microseconds=0), ['t', 'consommation_brute_electricite_rte']))
result_csv = pip_csv.process(data_meteo_2013)

fig, axs = plt.subplots(2)

axs[0].plot(result_csv[-1].data['temps_fenetrage'], result_csv[-1].data['moyenne_glissante_consommation_brute_electricite_rte'])
axs[1].plot(result_csv[-1].data['temps_fenetrage'], result_csv[-1].data['moyenne_glissante_t'])
plt.show()


#table_mois = Agregation_temporelle(timedelta(days=1, seconds=0, microseconds=0)).run(data_meteo_2013)
#table_mois2 = Agregation_temporelle(timedelta(days=1, seconds=0, microseconds=0)).run(data_elec_2013)


#table_join = Jointure(table_mois.var_date).full_join(table_mois, table_mois2)