from flask import jsonify, request
# from webargs import fields
# from webargs.flaskparser import parser

from . import temperature


@temperature.route('/temperature', methods=['GET'])
def get_tests():
    return 'ok'
