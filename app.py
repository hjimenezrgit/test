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

v1 = client.CoreV1Api()

pod_logs = v1.read_namespaced_pod_log(name='devops-arkon', namespace='default')
print(pod_logs)



for i in api_response.items:
    print(i.metadata.name + " " + i.status.phase)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    

