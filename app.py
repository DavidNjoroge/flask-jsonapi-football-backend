from flask import Flask

app = Flask(__name__)


# GET /users?sort_by=first_name&order=asc
# GET /users?page=3&results_per_page=20
# GET /users?first_name=Tania

@app.route('/')
def hello_world():
    return {
        'content': [],
        'page': 1,
        'results_per_page': 5,
        'total_results': 100
    }


if __name__ == '__main__':
    app.run()
