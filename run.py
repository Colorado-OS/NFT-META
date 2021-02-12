from flask import Flask, jsonify
from flask import request
from flask import Response

nft_meta_app = Flask(__name__)
nft_meta_app.debug = True


@nft_meta_app.route('/parks-pass/v/<pass_id>')
def parks_pass(pass_id):
    pass_id = int(pass_id)

    if pass_id == 1:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmeAns2p1zrYPvP2sPqAaDjq879ce9qnUEpeABSaYGxWvb/Colorado_NFT-10.png' 
    elif pass_id == 2:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmX8LNhPuVRpVB82Use8wZTdweWh8FHXa5sLbCCSZz5qMp/Colorado_NFT-06.png' 
    else:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmTsZ7oW94HDpYoowpEPTmJZ5augM7vUVQbhmamPqFwwm8/Colorado_NFT-11.png'

    return jsonify({
        'name': 'Colorado Park Pass',
        'description': 'ETHDenver 2021 - ColoradoJam - Colorado OS - Parks Pass NFT',
        'image': image_url
    })

@nft_meta_app.route('/gaming/v/<license_id>')
def gaming_license(license_id):
    license_id = int(license_id)

    if license_id == 1:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmSJqmXREd1f2WPV7hg9DK1fr3RQTURnGx9QqnjV1j98aW/iconfinder_colorado_state_flag_usa_5681508.png' 
    elif license_id == 2:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmbJiWqEyJ7U9dWagyMCGATqm6MkWLtKGt3sZdDpBChHoH/colo-parks-logo-768x768.jpg' 
    else:
        image_url = 'https://gateway.pinata.cloud/ipfs/QmbJiWqEyJ7U9dWagyMCGATqm6MkWLtKGt3sZdDpBChHoH/colo-parks-logo-768x768.jpg'

    return jsonify({
        'name': 'Colorado Digital Gaming License',
        'description': 'ETHDenver 2021 - ColoradoJam - Colorado OS - Players Gaming License NFT',
        'image': image_url
    })


@nft_meta_app.route('/api/get-json')
def hello():
    return jsonify(hello='world') # Returns HTTP Response with {"hello": "world"}


if __name__ == '__main__':
    nft_meta_app.run()
