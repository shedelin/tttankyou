import wrapper
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/api/v0/customer/', methods=['POST'])
def create_customer():
    payload = request.form.to_dict()
    result = wrapper.add_customer(**payload)

    if result:
        return jsonify(status='True', message='Customer created')
    return jsonify(status='False')

@app.route('/api/v0/customer/', methods=['GET'])
def get_all_customers():
    result = wrapper.get_all_customers()
    if result:
        return jsonify(status="True", 
        result= [
            {"id":customer.customer_id
             "first_name":customer.first_name,
             "last_name":customer.last_name,
             "email":customer.mail,
             "create_at": customer.create_at} for customer in result.all() ])
    return jsonify(status="False")

@app.route('/api/v0/customer/<id>', methods=['GET'])
def get_user(email):
    result = wrapper.get_customer_by_id(id)
    if result:
        return jsonify(status="True", 
                    result={"customer_id":customer.customer_id
                            "first_name":customer.first_name,
                            "last_name":customer.last_name,
                            "email":customer.mail,
                            "create_at": customer.create_at}
                        )
    return jsonify(status="False")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)