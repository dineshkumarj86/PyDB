from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/germanenessauth/api/v1/application', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
