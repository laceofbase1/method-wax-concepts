document.addEventListener('click', e => {
  if (e.target.closest('.burger')) document.body.classList.toggle('menu-open');
  else if (e.target.closest('.drawer a')) document.body.classList.remove('menu-open');
});
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
}), { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.rv').forEach(el => io.observe(el));
