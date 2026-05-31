import pika
import json


def enviar_mensagem(dados):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters("rabbitmq")
    )

    channel = connection.channel()

    channel.queue_declare(queue="fila_cep")

    channel.basic_publish(
        exchange="",
        routing_key="fila_cep",
        body=json.dumps(dados)
    )

    connection.close()