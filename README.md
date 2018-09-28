# Using istio

kubectl create ns version
kubens version

**Enable istio autoinjection**
kubectl label namespace version istio-injection=enabled
kubectl apply -f deploy.yml


## To check istio setup

sh check_istio.sh http://xx.xx.xx.xx/version

