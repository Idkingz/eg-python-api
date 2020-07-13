from app import app

@app.route('/')
@app.route('/index')
def index():
  # JSON works!
  user = {
    "tp": "simple string property",
    "numeric": 1,
    "complex": {
      "things": [1,2,3]
    }
  }
  return user["complex"]