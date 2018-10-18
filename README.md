# Using istio

kubectl create ns version
kubens version

**Enable istio autoinjection**
kubectl label namespace version istio-injection=enabled
kubectl apply -f deploy.yml


## To check istio setup

sh check_istio.sh http://xx.xx.xx.xx/version

## Test

You must use python 2.7 to run locust (or python 3.4)
pip install locustio
locust --host=http:xxx:xx.xx.xx