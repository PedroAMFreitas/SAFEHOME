import zmq
import json

def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://127.0.0.1:2000')
    subscriber.setsockopt(zmq.SUBSCRIBE, b"peso")

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
            altura = x["altura"]
            sexo = x["sexo"]
            if ( sexo == "masculino"):
                peso = (72.7*altura)-58
            else:
                peso = (62.1*altura)-44.7

            print("Peso : ",peso)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
