import os, sys, random, time

country = ["Albania",",Greece","Portugal","Argentina","Hong_Kong"
,"Romania","Australia","Hungary","Serbia"
,"Austria","Iceland","Singapore","Belgium"
,"India","Slovakia","Bosnia_And_Herzegovina"
,"Indonesia","Slovenia","Brazil"
,"Ireland","South_Africa"
,"Bulgaria","Israel","South_Korea"
,"Canada","Italy","Spain"
,"Chile","Japan","Sweden"
,"Costa_Rica","Latvia","Switzerland"
,"Croatia","Luxembourg","Taiwan"
,"Cyprus","Malaysia","Thailand"
,"Czech_Republic","Mexico","Turkey"
,"Denmark","Moldova","Ukraine"
,"Estonia","Netherlands","United_Kingdom"
,"Finland","New_Zealand","United_States"
,"France","North_Macedonia"]

while True:
    for i in range(1):
        ran = random.choices(country)
        os.system(f"nordvpn,connect,{ran}")
        time.sleep(20)
    
    
    
    