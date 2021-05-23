from flask import Flask, render_template, redirect, request

import Caption_it

# __name__ == __main__
app = Flask(__name__)

app.static_folder = 'static'
@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def marks():
    if request.method == 'POST':
        if request.files['userfile'].filename == '':

            return render_template("index.html", output="No File Selected")
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)  # ./static/images.jpg
        f.save(path)

        caption = Caption_it.caption_this_image(path)

        result_dic = {
            'image': path,
            'caption': caption
        }

    return render_template("index.html", your_caption=result_dic)


if __name__ == '__main__':
    #app.debug = True
    # due to versions of keras we need to pass another paramter threaded = Flase to this run function
    app.run(debug=True,host='127.0.0.1',port=6857)
