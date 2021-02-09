from flask import Flask, jsonify
from flask import request
from flask import Response

nft_meta_app = Flask(__name__)
nft_meta_app.debug = True

@nft_meta_app.route('/api/get-json')
def hello():
    return jsonify(hello='world') # Returns HTTP Response with {"hello": "world"}


if __name__ == '__main__':
    nft_meta_app.run()