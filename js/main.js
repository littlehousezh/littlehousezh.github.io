(() => {
  const root = document.documentElement;
  const button = document.querySelector('.theme-toggle');
  const preference = window.matchMedia('(prefers-color-scheme: dark)');
  function updateTheme(theme) {
    root.dataset.theme = theme;
    button.setAttribute('aria-pressed', String(theme === 'dark'));
    button.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
  }
  updateTheme(root.dataset.theme || (preference.matches ? 'dark' : 'light'));
  button.hidden = false;
  button.addEventListener('click', () => {
    const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    updateTheme(theme);
    try { localStorage.setItem('zihan-theme', theme); } catch (_) { /* Optional preference. */ }
  });
  preference.addEventListener('change', event => {
    try { if (localStorage.getItem('zihan-theme')) return; } catch (_) { /* Use system preference. */ }
    updateTheme(event.matches ? 'dark' : 'light');
  });
  const navLinks = [...document.querySelectorAll('nav a[href^="#"]')];
  const sections = navLinks.map(a => document.querySelector(a.getAttribute('href')));
  let queued = false;
  function updateNavigation() {
    const threshold = document.querySelector('.site-header').getBoundingClientRect().height + 100;
    let active = sections[0];
    for (const section of sections) if (section.getBoundingClientRect().top <= threshold) active = section;
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 3) active = sections.at(-1);
    for (const anchor of navLinks) {
      if (anchor.getAttribute('href') === '#' + active.id) anchor.setAttribute('aria-current', 'location');
      else anchor.removeAttribute('aria-current');
    }
    queued = false;
  }
  window.addEventListener('scroll', () => {
    if (!queued) { queued = true; requestAnimationFrame(updateNavigation); }
  }, { passive: true });
  window.addEventListener('resize', updateNavigation);
  window.addEventListener('pageshow', updateNavigation);
  // Existing bookmarks retain their destinations after the single-page migration.
  const aliases = { 'About-me':'about', Publications:'publications', Awards:'awards', Service:'service', News:'awards' };
  function resolveLegacyHash() {
    const target = aliases[location.hash.slice(1)];
    if (target) { history.replaceState(null, '', '#' + target); document.getElementById(target).scrollIntoView(); }
  }
  resolveLegacyHash();
  window.addEventListener('hashchange', resolveLegacyHash);
  updateNavigation();
})();
