from flask import Flask
from kubernetes.client.rest import ApiException
from kubernetes import client, config

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!"

class KubernetesService:
    def __init__(self):
        super().__init__()
        load_config()

pod_name = "devops-arkon"
try:
    api_instance = client.CoreV1Api()
    api_response = api_instance.read_namespaced_pod_log(name=pod_name, namespace='default')
    print(api_response)
except ApiException as e:
    print('Found exception in reading the logs')
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    

