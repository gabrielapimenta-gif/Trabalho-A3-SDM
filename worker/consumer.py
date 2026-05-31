import pika
import json
import time


while True:

    try:

        connection = pika.BlockingConnection(
            pika.ConnectionParameters("rabbitmq")
        )

        channel = connection.channel()

        channel.queue_declare(queue="fila_cep")

        def callback(ch, method, properties, body):

            dados = json.loads(body)

            print("\n===== NOVA CONSULTA =====")
            print(f"CEP: {dados['cep']}")
            print(f"Cidade: {dados['cidade']}")
            print(f"Estado: {dados['estado']}")
            print("=========================\n")

        channel.basic_consume(
            queue="fila_cep",
            on_message_callback=callback,
            auto_ack=True
        )

        print("Consumidor aguardando mensagens...")

        channel.start_consuming()

    except Exception as e:

        print("RabbitMQ ainda não disponível...")
        time.sleep(5)