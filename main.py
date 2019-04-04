from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20 px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action= "" method="POST" id=form1>
        <label for= "rot">Rotate by: </label>
        <input type="text" name="rot" default=int(0)/>
        <textarea name="text"></textarea>
        <button type="submit" form=form1 value="Submit">Submit Query</button>
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form['text']
    
    encrypted_string_element = rotate_string(text, rot)
    content = form + encrypted_string_element 
    return content
    

app.run()

#@app.route("/crossoff", methods=['POST'])
#def crossoff_movie():
 #   crossed_off_movie = request.form['crossed-off-movie']    

  #  crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
   # sentence = crossed_off_movie_element + " has been crossed off your Watchlist!"
    #content = page_header + "<p>" + sentence + "</p>" + page_footer

    #return content
