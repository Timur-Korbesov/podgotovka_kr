from flask import Flask, jsonify
import argparse

app = Flask(__name__)


@app.route('/firecrab/')
def fire_crab():
    result = {}

    with open(args.file, "r", encoding='utf-8') as file:
        text = file.readlines()

    for line in text[1:]:
        line = line.strip().split(";")
        if line[2] not in result:
            result[line[2]] = []

        result[line[2]].append([int(line[1]), int(line[3])])

    for key in result.keys():
        result[key].sort(key=(lambda x: (-x[0], -x[1])))

    return jsonify(result)


parser = argparse.ArgumentParser()
parser.add_argument("--server", required=True)
parser.add_argument("--port", required=True)
parser.add_argument("--file", required=True)

args = parser.parse_args()


if __name__ == '__main__':
    app.run(port=args.port, host=args.server)