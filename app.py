from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    if request.method == 'POST':
        nama = request.form['nama']
        umur = int(request.form['umur'])
        berat = float(request.form['berat'])
        tinggi = float(request.form['tinggi']) / 100  # cm to meter

        bmi = round(berat / (tinggi ** 2), 1)

        if bmi < 18.5:
            status = 'Underweight'
            video = 'https://www.youtube.com/embed/l3M3BVyCmc4'  # video gizi kurang
            pola_makan = 'Makan lebih sering dengan porsi kecil, tinggi protein dan karbohidrat kompleks.'
            saran_tidur = 'Tidur 7-9 jam setiap malam.'
            menu = 'Nasi, daging ayam, tahu/tempe, telur, alpukat, susu tinggi kalori.'
        elif 18.5 <= bmi <= 24.9:
            status = 'Ideal'
            video = 'https://www.youtube.com/embed/HFtelz2k4Gg'  # video gizi seimbang
            pola_makan = 'Pola makan seimbang dengan karbohidrat, protein, lemak sehat, buah, dan sayur.'
            saran_tidur = 'Tidur 7-8 jam setiap malam.'
            menu = 'Nasi merah, dada ayam, brokoli, wortel, buah segar, air putih.'
        else:
            status = 'Obesitas'
            video = 'https://www.youtube.com/embed/1bcRzI9YBG0'  # video obesitas
            pola_makan = 'Kurangi gula dan makanan berlemak, perbanyak serat dan air putih.'
            saran_tidur = 'Tidur 6-8 jam dan hindari makan malam terlalu larut.'
            menu = 'Sayuran hijau, nasi merah, ikan bakar, buah rendah gula (apel, pir).'

        # Nutrisi dalam persen (dummy static value, bisa diganti dinamis nanti)
        nutrisi = {
            'karbohidrat': 50,
            'protein': 30,
            'lemak': 20
        }

        return render_template('result.html',
                               nama=nama,
                               umur=umur,
                               berat=berat,
                               tinggi=tinggi * 100,
                               bmi=bmi,
                               status=status,
                               video=video,
                               pola_makan=pola_makan,
                               saran_tidur=saran_tidur,
                               menu=menu,
                               nutrisi=nutrisi)
if __name__ == '__main__':
    app.run(debug=True)