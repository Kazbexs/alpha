from flask import Flask, render_template, request
import alpha
import petrinet
import pydot


#HOST = "localhost"
#PORT = 3000


server = Flask("server")

# upload config
# server.config["UPLOAD_FOLDER"] = "/uploads"
# server.config['MAX_CONTENT_PATH'] = 500000


@server.route("/")
def main_page():
    return render_template("index.html")


# uploader
@server.route("/uploader", methods=["POST"])
def upload():
    file = request.files.get("file")
    binary = file.stream.read()
    data_dict = alpha.generate_alpha(binary)
    code = petrinet.build_petrinet(data_dict)
    graph = pydot.graph_from_dot_data(code)
    result = graph[0].create_svg()
    print(result)
    return result
