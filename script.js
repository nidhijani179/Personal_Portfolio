function toggleDetails(id) {
    const element = document.getElementById(id);
    const button = element.previousElementSibling;
    if (element.style.display === 'none' || element.style.display === '') {
        element.style.display = 'block';
        button.textContent = 'Read Less';
    } else {
        element.style.display = 'none';
        button.textContent = 'Read More';
    }
}

// Contact form submission
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Thank you for contacting us!');
    this.reset();
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});