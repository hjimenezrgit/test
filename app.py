import os
from flask import Flask
from kubernetes.client.rest import ApiException
from kubernetes import client, config

app = Flask(__name__)

config.load_kube_config(
    os.path.join(os.environ["HOME"], '/opt/app/config'))

v1 = client.CoreV1Api()

pod_list = v1.list_namespaced_pod("default")



@app.route("/")
def hello():
    return "Hello World!!!"
for pod in pod_list.items:
    print("%s\t%s\t%s" % (pod.metadata.name, 
                          pod.status.phase,
                          pod.status.pod_ip))


    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    

