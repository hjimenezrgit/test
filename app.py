import os
import time
from flask import Flask ,request
from kubernetes.client.rest import ApiException
from kubernetes import client, config
import logging

app = Flask(__name__)
#logging.basicConfig(filename='record.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logging.basicConfig(filename='/opt/nfs/record.log', level=logging.INFO, format=f' %(threadName)s : %(message)s')
 
#file1 = open('record.log', 'r')
#Lines = file1.readlines()

#count = 0
#poc = 0
#string1 = 'POST'

#for line in Lines:
#    count += 1
#    if string1 in line:
#        poc += 1

#print(poc)  
global poc
poc = 0



@app.route("/", methods=['GET', 'POST'])
def hello():
    app.logger.info('Info level log')
    file1 = open('/opt/nfs/record.log', 'r')
    Lines = file1.readlines()
    count = 0
    string1 = 'POST'
    if request.method == 'POST':
        globals()['poc'] = 0
        for line in Lines:
            count += 1
            if string1 in line:
                globals()['poc'] += 1    
        return "Hello World!!!"
    else:
        return str(globals()['poc'])    

    #

#def log_request_info():
#    app.logger.debug('Headers: %s', request.headers)
#    app.logger.debug('Body: %s', request.get_data())
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

    
