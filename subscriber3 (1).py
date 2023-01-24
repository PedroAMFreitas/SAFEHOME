import zmq
import json

def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://127.0.0.1:2000')
    subscriber.setsockopt(zmq.SUBSCRIBE, b"aluno")

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
            n1 = x["n1"]
            n2 = x["n2"]
            n3 = x["n3"]
            m = (n1 + n2)/2
            if ( m >= 7 or (m + n3)/2 >= 5):
                resultado = "Aprovado"
            else:
                resultado = "Reprovado"


            print("Resultado : ",resultado)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
