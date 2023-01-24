import zmq
import json

def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://127.0.0.1:2000')
    subscriber.setsockopt(zmq.SUBSCRIBE, b"esporte")

    poller = zmq.Poller()
    poller.register(subscriber, zmq.POLLIN)

    while True:

        try:
            socks = dict(poller.poll())
        except KeyboardInterrupt:
            exit()

        if subscriber in socks:
            [address, contents] = subscriber.recv_multipart()
            x = json.loads(contents)
            idade = x["idade"]
            if (idade <= 7):
                categoria  = "infantil A"
            elif(idade >= 8 and idade <= 10):
                categoria  = "infantil B"
            elif(idade >= 11 and idade <= 13):
                categoria  = "juvenil A"
            elif(idade >= 14 and idade <= 17):
                categoria  = "juvenil B"
            else:
                categoria  = "Adulto"

            print("Categoria : ",categoria)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
