from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    "foobar",
    auto_offset_reset="START_FROM",
    bootstrap_servers=f"localhost:9093",
    client_id = "client1",
    group_id = "g1",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    value_deserializer=lambda v: json.dumps(v).encode('ascii'),
    key_deserializer=lambda v: json.dumps(v).encode('ascii'),
)
print(consumer.topics())