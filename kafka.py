from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=f"localhost:9093",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii'),
)
producer.send('foobar', key='foo', value='bar')
producer.flush()