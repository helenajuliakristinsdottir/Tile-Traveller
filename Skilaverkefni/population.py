#Population project
#Helena Julia Kristinsdottir & Silja Björk Axelsdottir

People=307357870
birth_year=1/7*60*60*24*365 #fjöldi sem fæðist á ári
dead_year=1/13*60*60*24*365 #fjöldi sem deyr á ári
immigrant_year=1/35*60*60*24*365 #fjöldi innflytjenda á ári

year_str=input('Years: ') #notandi skrifar inn gildi
year=int(year_str) #hér breytum úr streng í heiltölu

if year<0:
    print('Invalid input!')
else:
    People_new=float((year*birth_year) - (year*dead_year) + (year*immigrant_year) + People)

People_new=int(People_new) #lokasvar er breytt úr float í heiltölu

print('New population after',year,\
      'years is',People_new)
