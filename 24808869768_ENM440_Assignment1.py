import pandas as pd
import matplotlib.pyplot as plt
import seaborn

titanic = pd.read_csv("titanic.csv", sep=",")
Sex_Type = ['male', 'female']  # type of SEX/GENDER : male female
j = 0
while j <= (len(Sex_Type) - 1):
    titanic['Sex'] = titanic['Sex'].replace(Sex_Type[j], j)
    j -= -1
# these are to show ^SEX^ information about passengers
Embarked_Type = ['C', 'Q', 'S']  # type of Embarked : C Q S
i = 0
while i <= (len(Embarked_Type) - 1):
    titanic['Embarked'] = titanic['Embarked'].replace(Embarked_Type[i], (i + 1))
    i += 1
# these are to show ^EMBARKED^ information about passengers
plt.figure(figsize=(12.24031997, 8.24031997))  # this size was set to view clearly, it is changeable
ax = seaborn.heatmap(titanic.corr().abs(), annot=True)
plt.axis('equal')  # to show the heat map proportionally
plt.title("Heatmap of Titanic Data Set")
plt.show()
