date = Popen(["date"], stdout=PIPE)
stdout, stderr = date.communicate()
app = Flask(__name__)

@app.route("/")
def get_date():
    return stdout.decode('utf-8').split("\n")[0]

if __name__ == "__main__":
    app.run()

