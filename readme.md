# Deploy App
kubectl apply -f deployment.yaml

# Access app
kubectl port-forward svc/sherlock-service --address 0.0.0.0 9090:80