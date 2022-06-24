import os
import time
from flask import Flask ,request
import logging

app = Flask(__name__)
###REGISTRO DE EVENTOS GET y POST EN NFS
logging.basicConfig(filename='/opt/nfs/record.log', level=logging.INFO, format=f' %(threadName)s : %(message)s')
 
###FUNCION CONTEO DE METODO POST
def postcount():
    file1 = open('/opt/nfs/record.log', 'r')
    Lines = file1.readlines()
    string1 = 'POST'
    global poc
    poc = 0
    for line in Lines:
        if string1 in line:
            poc += 1

## MAIN
@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        postcount()
        return "Hello World!!!"
    else:
        postcount()
        r = "Hello World!!!  METHODS POST = " + str(globals()['poc'])
        return r

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5030)

    
