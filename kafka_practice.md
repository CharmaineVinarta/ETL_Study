# Practice Exercises

### Problem 1
- Create a new topic named `weather`.
```
bin/kafka-topics.sh --create --topic weather --bootstrap-server localhost:9092
```

### Problem 2
- Post messages to the topic `weather`.
```
bin/kafka-console-producer.sh --topic weather --bootstrap-server localhost:9092
```


### Problem 2
- Read the messages from the topic `weather`.
```
bin/kafka-console-consumer.sh --topic weather --from-beginning --bootstrap-server localhost:9092
```
