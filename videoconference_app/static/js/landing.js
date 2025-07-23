// Smooth scroll for anchor links
const links = document.querySelectorAll('a[href^="#"]');
for (const link of links) {
  link.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
}
// Fade-in animation on scroll
const fadeSections = document.querySelectorAll('.features, .brands, .testimonials, .cta');
const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = 1;
      entry.target.style.transform = 'none';
      fadeObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.2 });
fadeSections.forEach(section => {
  section.style.opacity = 0;
  section.style.transform = 'translateY(40px)';
  fadeObserver.observe(section);
});
// Keyboard navigation for nav
const navLinks = document.querySelectorAll('.nav ul li a');
navLinks.forEach(link => {
  link.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      this.click();
    }
  });
});
// Newsletter form ARIA feedback (optional)
const newsletter = document.querySelector('.newsletter');
if (newsletter) {
  newsletter.addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Thank you for subscribing!');
  });
} 