# Lecture Introduction
1. lecture1 is simple rabbitmq appliction,that one appliction send a job to queue and another appliction is receive the job 
2. lecture2 is rabbitmq fair worker queue application,that some application send job to queue and others application is faired receive job
3. lecture3 is rabbitmq fanout exchange application,that some application send job to temp queues and others application is receive job of temp queues
4. lecture4 is rabbitmq direct exchange application,that some application send job to temp queues and others application is receive job of temp queues by routing_key
5. lecture5 is rabbitmq topic exchange application,that some application send job to temp queues and others application is receive job of temp queues by topic routing_key
## setup rabbitmq
Pull rabbitmq image from Docker Hub
```
docker pull rabbitmq:3.6.15-management
```
Run rabbitmq
```
docker run -d --hostname localhost --name myrabbit -p 15672:15672 -p 5672:5672 rabbitmq:3.6.15-management
```
## RabbitMQ Command Line
list queue
```
rabbitmqctl list_queues
```
list queue content
```
rabbitmqctl -u admin -p adminpass get queue=queue_name count=10
```
list exchange
```
rabbitmqctl list_exchanges
```
list binding
```
rabbitmqctl list_bindings
```
## Reference
- [Getting started with RabbitMQ](https://www.rabbitmq.com/getstarted.html)