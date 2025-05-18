// SPLASH SCREEN ANIMASI
document.addEventListener("DOMContentLoaded", function () {
  const splash = document.querySelector(".splash");
  setTimeout(() => {
    splash.style.opacity = 0;
    splash.style.visibility = "hidden";
  }, 3000);
});

// STICKY HEADER ON SCROLL
window.addEventListener("scroll", function () {
  const header = document.querySelector(".header");
  if (window.scrollY > 50) {
    header.style.background = "rgba(255,255,255,0.95)";
    header.style.boxShadow = "0 2px 6px rgba(0,0,0,0.1)";
  } else {
    header.style.background = "rgba(255,255,255,0.8)";
    header.style.boxShadow = "none";
  }
});

// WHATSAPP FLOAT BUTTON ACTION
document.addEventListener("DOMContentLoaded", function () {
  const whatsappBtn = document.querySelector(".whatsapp-float");
  if (whatsappBtn) {
    whatsappBtn.addEventListener("click", function () {
      window.open("https://wa.me/6281295738629", "_blank"); // Ganti dengan nomor WA kamu
    });
  }
});

function tampilkanHasil(bmi, status, kalori, tips) {
    document.getElementById("hasil-section").style.display = "block";
    document.getElementById("bmiValue").innerText = bmi;
    document.getElementById("statusGizi").innerText = status;
    document.getElementById("kaloriHarian").innerText = kalori + " kkal";
    document.getElementById("tipsGizi").innerText = tips;

    // Pie Chart (contoh)
    const ctx = document.getElementById('pieChart').getContext('2d');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Karbohidrat', 'Protein', 'Lemak'],
        datasets: [{
          label: 'Kalori',
          data: [60, 20, 20], // Kamu bisa ubah dinamis sesuai input
          backgroundColor: ['#f1c40f', '#2ecc71', '#e67e22']
        }]
      }
    });
  }

  // Contoh panggil manual (kamu bisa ganti ini jadi dinamis)
  // tampilkanHasil(22.5, "Ideal", 2200, "Pertahankan pola makan seimbang & olahraga!");
