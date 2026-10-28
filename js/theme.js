// Set the theme before paint; restricted storage must never prevent rendering.
(() => {
  try {
    const saved = localStorage.getItem('zihan-theme');
    if (saved === 'dark' || saved === 'light') document.documentElement.dataset.theme = saved;
  } catch (_) { /* System preference remains available through CSS. */ }
})();
