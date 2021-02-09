from flask import Flask, jsonify
from flask import request
from flask import Response

nft_meta_app = Flask(__name__)
nft_meta_app.debug = True


@nft_meta_app.route('/parks-pass/v/<pass_id>')
def parks_pass(pass_id):
    pass_id = int(pass_id)

    if pass_id == 1:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmSJqmXREd1f2WPV7hg9DK1fr3RQTURnGx9QqnjV1j98aW/iconfinder_colorado_state_flag_usa_5681508.png' 
    elif pass_id == 2:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmbJiWqEyJ7U9dWagyMCGATqm6MkWLtKGt3sZdDpBChHoH/colo-parks-logo-768x768.jpg' 
    else:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmbJiWqEyJ7U9dWagyMCGATqm6MkWLtKGt3sZdDpBChHoH/colo-parks-logo-768x768.jpg'

    return jsonify({
        'name': 'Colorado Park Pass',
        'description': 'ETHDenver 2021 - ColoradoJam - Parks Pass NFT',
        'image': image_url
    })
     

@nft_meta_app.route('/api/get-json')
def hello():
    return jsonify(hello='world') # Returns HTTP Response with {"hello": "world"}


if __name__ == '__main__':
    nft_meta_app.run()