import pandas as pd
import numpy as np 

# Importation des bases de données 
iran = pd.read_csv("IranCustomerChurn.csv", sep = ",") 
nig = pd.read_csv("NigeriaTRAIN.csv", sep = ",") 

#--------- Nigéria

print(nig.head())
