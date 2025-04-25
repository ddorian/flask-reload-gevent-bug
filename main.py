import gevent.monkey

# reloading works if thread=False
gevent.monkey.patch_all(thread=True)

from flask import Flask
#from opentelemetry.instrumentation.threading import ThreadingInstrumentor

app = Flask(__name__)

@app.route("/")
def hello_world():
    """abc2356789012"""
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    # az
    app.run(debug=True)
