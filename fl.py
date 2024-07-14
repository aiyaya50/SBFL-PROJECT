# invoke_script.py
import subprocess

# Checkout Closure-27, compile it, and get its metadata
trial= {'Chart':'26', 'Time':'26','Gson':'18', 'Jsoup':'93'}
v1 = {'Chart':26, 'Time':26, 'Lang':64, 'Mockito':38, 'Math':106, 'JxPath':22,'Closure':174}
v2={'Collections':4, 'Codec':18, 'Csv':16, 'Cli':39, 'Math':106, 'JxPath':22, \
          'Jsoup':93, 'JacksonXml':6,'JacksonDatabind':112, 'JacksonCore':26, 'Gson':18, 'Compress':47, 'Closure':174}
for p in trial:
    PID=p
    BID=int(trial[p])
    for e in range(1, BID+1):
        e=f'{e}'
        command='echo PID='+PID+'>f.sh;echo BID='+e+'>>f.sh;cat run.sh >> f.sh;sh f.sh'
        process = subprocess.run(command, shell=True)
        print(process)
    