import requests


def horklump(address, port, **kwargs):
    js = requests.get("http://" + address + ":" + str(port) + "/").json()
    if kwargs['place'] in js:
        js[kwargs['place']].append(dict(filter(lambda x: x[0] != 'place', kwargs.items())))
    else:
        js[kwargs['place']] = dict(filter(lambda x: x != 'place', kwargs.items()))

    return js


print(horklump('127.0.0.1', 5000, place='France', weight=13, count=3))