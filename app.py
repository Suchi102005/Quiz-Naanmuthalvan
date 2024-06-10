from flask import Flask, render_template, request

app = Flask(__name__)

# Sample questions dictionary
questions = {
    'math': [
        "What is 2 + 2?",
        "What is the square root of 16?"
    ],
    'science': [
        "What is the chemical symbol for water?",
        "What planet is known as the Red Planet?"
    ],
    'literature': [
        "Who wrote 'To Kill a Mockingbird'?",
        "Who is the author of '1984'?"
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subjects', methods=['POST'])
def subjects():
    name = request.form['name']
    email = request.form['email']
    return render_template('subjects.html', name=name, email=email)

@app.route('/quiz', methods=['POST', 'GET'])
def quiz():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        question_number = 0
        question = questions[subject][question_number]
        return render_template('quiz.html', name=name, email=email, subject=subject, question_number=question_number, question=question)
    else:
        name = request.args.get('name')
        email = request.args.get('email')
        subject = request.args.get('subject')
        question_number = int(request.args.get('question_number', 0))
        answer = request.args.get('answer', '')

        if question_number < len(questions[subject]):
            question = questions[subject][question_number]
            return render_template('quiz.html', name=name, email=email, subject=subject, question_number=question_number, question=question)
        else:
            return render_template('complete.html', name=name, email=email, subject=subject)

if __name__ == '__main__':
    app.run(debug=True)
