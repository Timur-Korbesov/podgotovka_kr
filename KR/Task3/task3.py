import requests


def sledge_under_sail(*args):
    host, port = args[0], args[1]
    res = requests.get(f"http://{host}:{str(port)}/").json()

    ans = {"directions": [], "velocities": []}

    for local in args[2:]:
        for el in res:
            if el["locality"] == local:
                ans["directions"].append(el["wind"])
                ans["velocities"].append(el["speed"])
    return ans


data = ["127.0.0.1", 8080, "Anderson", "Hooper Bay", "Ambler", "Ketchikan"]
print(sledge_under_sail(*data))