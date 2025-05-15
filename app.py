from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100  # convert cm to m

    bmi = round(weight / (height ** 2), 2)

    # Determine BMI category
    if bmi < 18.5:
        status = "Underweight"
        youtube = "https://www.youtube.com/embed/gZ1Zj7d-3Vs"
        menu = "Nasi, ayam goreng, sayur bayam, susu"
        pattern = "3x makan besar, 2x snack sehat"
        advice = "Perbanyak makanan tinggi kalori dan protein"
    elif 18.5 <= bmi < 25:
        status = "Ideal"
        youtube = "https://www.youtube.com/embed/xvFZjo5PgG0"
        menu = "Nasi, ikan, sayur, buah segar"
        pattern = "3x makan teratur, cukup minum"
        advice = "Pertahankan pola makan dan tidur yang sehat"
    else:
        status = "Obesitas"
        youtube = "https://www.youtube.com/embed/vKtwXklQwl4"
        menu = "Nasi merah, dada ayam rebus, sayur kukus"
        pattern = "Porsi kecil, hindari makanan berlemak"
        advice = "Kurangi gula dan olahraga rutin"

    # Nutrisi pie chart (dummy data)
    nutrisi = {
        'Karbohidrat': 50,
        'Protein': 30,
        'Lemak': 20
    }

    return render_template('result.html',
                           bmi=bmi,
                           status=status,
                           youtube=youtube,
                           menu=menu,
                           pattern=pattern,
                           advice=advice,
                           nutrisi=nutrisi)

    return render_template("result.html", 
    bmi=bmi, 
    status=status, 
    saran=saran_menu, 
    video_url=video_url, 
    chart_data=[karbo, protein, lemak]
)


if __name__ == '__main__':
    app.run(debug=True)
