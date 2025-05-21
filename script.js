// script.js

document.addEventListener('DOMContentLoaded', function () {
  // Preloader hilang setelah 2 detik
  const preloader = document.getElementById('preloader');
  setTimeout(() => {
    preloader.style.opacity = '0';
    preloader.style.pointerEvents = 'none';
    setTimeout(() => preloader.remove(), 500);
  }, 2000);

  // Toggle dark/light mode
  const toggleTheme = document.getElementById('toggleTheme');
  const userPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  if (localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && userPrefersDark)) {
    document.documentElement.classList.add('dark');
  }

  toggleTheme.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    if (document.documentElement.classList.contains('dark')) {
      localStorage.setItem('theme', 'dark');
    } else {
      localStorage.setItem('theme', 'light');
    }
  });
});
