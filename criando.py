import csv
import time
import datetime


#dia 1 do 1 de 2009 = quinta feira = thursday

months = {'1' : 'January', '2' : 'February', '3' : 'March', '4' : 'April', '5' : 'May', '6' : 'June',
 '7' : 'July', '8' : 'August', '9' : 'September', '10' : 'October', '11' : 'November', '12' : 'December'}
# months_inday = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12]
daysweek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dict_daysweek = {'Sunday' : '7', 'Monday' : '1', 'Tuesday' : '2', 'Wednesday' : '3', 'Thursday' : '4', 'Friday' : '5', 'Saturday' : '6'}
daysweek_2009 = ['Thursday', 'Friday', 'Saturday']
# qnt_dias_mes_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# qnt_dias_mes_bis = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# days_31 = [x for x in range(1,32)]
# days_30 = [x for x in range(1,31)]
# days_29 = [x for x in range(1,30)]
# days_28 = [x for x in range(1,29)]
# years = [x for x in range(2009,2031)]
# bisexto = [x for x in range(2012,2031, 4)]

# colunas = "date_key", "dateinfull", "dayofweek", "month", "year", "quarter", "daynuminweek", "daynuminmonth", "daynuminyear", "monthnuminyear", "weeknuminyear", "holidays_key"

#DATA DE 2009 ATE 2030
#---------------------------------------------------
a = datetime.date(2029,12,31)
numdays = 7670
date_key = []
for x in range (0, numdays):
    date_key.append(a - datetime.timedelta(days = x))
date_key_certo = date_key[::-1]
#---------------------------------------------------
#DATA POR EXTENSO
#---------------------------------------------------
dateinfull = []

for x in range(len(date_key_certo)):
    # ano = str(date_key_certo[x]).split('-')[0]
    # mes = str(date_key_certo[x]).split('-')[1]
    # dia = str(date_key_certo[x]).split('-')[2]

    ano = str(date_key_certo[x].year)
    mes = str(date_key_certo[x].month)
    dia = str(date_key_certo[x].day)
    
    palavra = months[str(int(mes))] + ' ' + dia + ', ' + ano
    dateinfull.append(palavra)


#---------------------------------------------------
#DIA POR EXTENSO
#---------------------------------------------------
dias_absurdo = daysweek_2009 + daysweek * 1100

dayofweek = []
for x in range(len(date_key_certo)):
    dayofweek.append(dias_absurdo[x])

#---------------------------------------------------
#MES POR EXTENSO
#---------------------------------------------------
mes_extenso = []

for x in range(len(date_key_certo)):
    mes = str(date_key_certo[x].month)

    palavra = months[str(int(mes))]
    mes_extenso.append(palavra)
#---------------------------------------------------
#ANO
#---------------------------------------------------
ano = []

for x in range(len(date_key_certo)):
    ano.append(str(date_key_certo[x].year))


#---------------------------------------------------
#DIA DA SEMANA (NUMERO)
#---------------------------------------------------
dia_semana_num = []

for x in range(len(date_key_certo)):
    dia_semana_num.append(dict_daysweek[str(dias_absurdo[x])])

#---------------------------------------------------
#---------------------------------------------------
#QUARTER DO ANO (NUMERO)
quarter = []

for x in range(len(date_key_certo)):
    quarter.append(str((date_key_certo[x].month - 1)//3 + 1))



#---------------------------------------------------
#DIA DO MES (NUMERO)
#---------------------------------------------------
dia_mes = []

for x in range(len(date_key_certo)):
    dia = str(date_key_certo[x].day)
    dia_mes.append(str(int(dia)))

#---------------------------------------------------
#DIA DO ANO (NUMERO)
#---------------------------------------------------
dia_do_ano = []

for x in range(len(date_key_certo)):
    hoje = datetime.datetime(date_key_certo[x].year, date_key_certo[x].month, date_key_certo[x].day)
    inicio = datetime.datetime(date_key_certo[x].year,1 , 1)
    totald = hoje - inicio
    dia_do_ano.append(totald.days + 1)

#---------------------------------------------------
#MES DO ANO (NUMERO)
#---------------------------------------------------
mes_ano = []

for x in range(len(date_key_certo)):
    mes = str(date_key_certo[x].month)
    mes_ano.append(int(mes))

#---------------------------------------------------
#SEMANA DO ANO (NUMERO)
#---------------------------------------------------
semana_ano = []

for x in range(len(date_key_certo)):
    semana = date_key_certo[x].isocalendar()[1]
    semana_ano.append(semana)
#---------------------------------------------------



with open('dw_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["date_key", "dateinfull", "dayofweek", "month", "year", "quarter", "daynuminweek", "daynuminmonth", "daynuminyear", "monthnuminyear", "weeknuminyear", "holidays_key"])
    for x in range(len(date_key)):

        writer.writerow([date_key_certo[x],dateinfull[x],dayofweek[x],mes_extenso[x],ano[x],quarter[x],dia_semana_num[x],dia_mes[x], dia_do_ano[x],mes_ano[x],semana_ano[x],0])
