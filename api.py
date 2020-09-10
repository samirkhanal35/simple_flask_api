from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        return jsonify(str("Successfully stored  " + str(data)))

@app.route("/message", methods=["GET"])
def message():
    posted_data = request.args['name']
    # print(posted_data)
    # data = posted_data['name']
    return jsonify(" Hope you are having a good time " +  posted_data + "!!!")
    # return jsonify(" Hope you are having a good time !!")

#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)