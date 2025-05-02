from flask import Flask, render_template, request

app = Flask(__name__)

runner_names = [
    "Anna", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy",
    "Kevin", "Laura", "Mallory", "Niaj", "Olivia", "Peggy", "Quentin", "Rupert", "Sybil", "Trent",
    "Uma", "Victor", "Walter", "Xander", "Yvonne", "Zara", "Alice", "Brian", "Catherine", "Derek"
]

# Sample runner data (with ID, Name, Age, and Time)
runners = [{"id": i+1, "name": f"{runner_names[i+1]}", "age": 20 + i%10, "time": f"{3+i%2}:{15+i%10}"} for i in range(29)]

RUNNERS_PER_PAGE = 5

@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    start = (page - 1) * RUNNERS_PER_PAGE
    end = start + RUNNERS_PER_PAGE
    displayed_runners = runners[start:end]

    total_pages = (len(runners) + RUNNERS_PER_PAGE - 1) // RUNNERS_PER_PAGE
    return render_template(
        'index.html',
        runners=displayed_runners,
        page=page,
        total_pages=total_pages
    )

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)


"""
demo:
Copilot edit -> select Agent: copilot can make automatic changes in multiple files
1.update the buttons to make them look prettier
2.can you add the functionality that we can filter the data based on the runners name? Can you run suitable unit tests?
"""