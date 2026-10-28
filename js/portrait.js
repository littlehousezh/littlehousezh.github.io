// Keep the original portrait visible until the alternate image is decoded.
(() => {
  const frame = document.querySelector('.portrait-frame');
  const alternate = frame?.querySelector('.portrait-alternate');
  if (!alternate) return;
  alternate.decode().then(() => frame.classList.add('portrait-ready')).catch(() => {
    // If the alternate image cannot load, the original remains fully usable.
  });
})();
