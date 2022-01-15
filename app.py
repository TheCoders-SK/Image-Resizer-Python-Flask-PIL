from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    if request.args.get('file') != None:
        img = Image.open(request.args.get('file'))
        w, h = img.size
        if request.args.get('resize') != None or int(request.args.get('resize')) < 0:
            n = request.args.get('resize')
            n = int(n)
        outimg = img.resize((w * n, h * n))
        outimg.save(request.args.get('file'))
    return render_template('home.html')
