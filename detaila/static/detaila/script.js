document.addEventListener('DOMContentLoaded', function() {
    const vitaminCards = document.querySelectorAll('.vitamin-card');

    vitaminCards.forEach(card => {
        card.addEventListener('click', function() {
            this.classList.toggle('show');
        });
    });
});
