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
      window.open("https://wa.me/6281234567890", "_blank"); // Ganti dengan nomor WA kamu
    });
  }
});
