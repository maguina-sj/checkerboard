from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', color1='red', color2='black', across=8, down=8)

@app.route('/<int:down>/')
def changeDown(down):
    return render_template('index.html', color1='red', color2='black', across=8, down=down)

@app.route('/<int:across>/<int:down>/')
def boardChange(across,down):
    return render_template('index.html', color1='red', color2='black', across=across, down=down)


@app.route('/<int:across>/<int:down>/<string:color1>/<string:color2>/')
def board(across,down,color1,color2):
    return render_template('index.html', across=across, down=down, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)