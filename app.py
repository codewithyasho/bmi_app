from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-kWMZfLHOq9NVYVeyG0iMT3BlbkFJ5N0H4R9XleIDT0aJX2Ce"
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculate_bmi():
    if request.method == "POST":
        height = float(request.form["height"])
        weight = float(request.form["weight"])

        bmi = weight / (height ** 2)

        # Your OpenAI chat completion code here
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a fitness consultant, dietition, healthcare professional, fitness enthusiast. you are given bmi calculated values. give some tips, personalized advice, consultancy for improvement on the basis of bmi index (give responses in 3-4 lines only)."},
                {"role": "user", "content": f"{bmi}"}
            ]
        )
        # ...

        if bmi < 18.5:
            result = chat_completion.choices[0].message.content
        elif bmi < 25:
            result = chat_completion.choices[0].message.content
        elif bmi < 30:
            result = chat_completion.choices[0].message.content
        elif bmi < 35:
            result = chat_completion.choices[0].message.content
        else:
            result = chat_completion.choices[0].message.content

        return render_template("result.html", bmi=bmi, result=result)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
