// Splash screen animation
window.addEventListener('load', () => {
  const splash = document.getElementById('splash-screen');
  splash.classList.add('fade-out');
  setTimeout(() => splash.style.display = 'none', 1000);
});

// Header muncul saat scroll
window.addEventListener("scroll", function() {
  const header = document.getElementById("main-header");
  header.classList.toggle("scrolled", window.scrollY > 50);
});
