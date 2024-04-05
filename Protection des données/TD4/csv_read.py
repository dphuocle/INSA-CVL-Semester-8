# Author B.Nguyen 3/2020
# Licence CC BY-NC
import csv
pathin = 'D:/4e INSA CVL Semestre 8/Protection des données/TD4/student-mat.csv'
pathout = 'D:/4e INSA CVL Semestre 8/Protection des données/TD4/student-mat-dp.csv'
with open(pathin) as f:
    with open(pathout,'w', newline='') as f_out:
        f_csv_r = csv.DictReader(f, delimiter=',', quotechar='"')
        #fnames = ['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','guardian','traveltime','studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences','G1','G2','G3']
        fnames = ['G1', 'G2', 'G3']
        f_csv_w = csv.DictWriter(f_out, fieldnames = fnames, delimiter=',',quotechar='"')
        f_csv_w.writeheader()
        for ligne in f_csv_r:
            print (ligne['G1'], ligne['G2'], ligne['G3'])
            f_csv_w.writerow({'G1':ligne['G1'], 'G2':ligne['G2'], 'G3':ligne['G3']})
