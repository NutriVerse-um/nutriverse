from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = 'Kurus'
            image = 'bg_underweight.png'
        elif 18.5 <= bmi < 25:
            category = 'Normal'
            image = 'bg_ideal.png'
        elif 25 <= bmi < 30:
            category = 'Gemuk'
            image = 'bg_obesitas.png'
        else:
            category = 'Obesitas'
            image = 'bg_obesitas.png'

        return render_template('result.html', bmi=bmi, category=category, image=image, age=age, weight=weight, height=height_cm)
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

if __name__ == '__main__':
    app.run(debug=True)
