from flask import jsonify, make_response

def success(values, message):
    res = {
        'data' : values,
        'message': message
    }
    # Menggunakan make_response untuk memastikan objek response yang valid
    return make_response(jsonify(res), 200)

def badRequest(values, message):
    res = {
        'data' : values,
        'message': message
    }
    # Menggunakan make_response untuk memastikan objek response yang valid
    return make_response(jsonify(res), 400)
