/home/aziro/api-check.sh ==> running in background process to hit both APIs. We have also added Prometheus, loki and tempo as datasource in Grafana on port 3000.   
  
 📱 Golang Application:  
    • URL:     http://172.30.38.246:8085  
    • Ping:    http://172.30.38.246:8085/ping  
    • Metrics: http://172.30.38.246:8085/metrics  
  
  📊 Prometheus:  
    • URL:     http://172.30.38.246:9095  
    • Targets: http://172.30.38.246:9095/targets  
    • Graph:   http://172.30.38.246:9095/graph  
  
  📈 Grafana:  
    • URL:      http://172.30.38.246:3005  
    • Username: admin  
    • Password: admin  
  
  📝 Loki:  
    • URL:     http://172.30.38.246:3105  
    • Ready:   http://172.30.38.246:3105/ready  
    • Metrics: http://172.30.38.246:3105/metrics  
  
  🔍 Tempo:  
    • URL:     http://172.30.38.246:3205  
    • Ready:   http://172.30.38.246:3205/ready  
    • Search:  http://172.30.38.246:3205/api/search