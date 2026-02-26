// portfolio-animations.js
// Adds scroll-triggered fade-in animations to sections and cards
document.addEventListener('DOMContentLoaded', function () {

    const sections = document.querySelectorAll('main section');
    const cards = document.querySelectorAll('.portfolio-card');

    sections.forEach(function (section) {
        section.classList.add('reveal');
    });

    cards.forEach(function (card) {
        card.classList.add('reveal');
    });

    const observer = new IntersectionObserver(
        function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.1,
            rootMargin: '0px 0px -40px 0px'
        }
    );

    sections.forEach(function (el) { observer.observe(el); });
    cards.forEach(function (el) { observer.observe(el); });

});