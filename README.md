# Using istio

kubectl create ns version
kubens version

**Enable istio autoinjection**
kubectl label namespace version istio-injection=enabled
kubectl apply -f deploy.yml




