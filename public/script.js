document.querySelectorAll('.symptom-button').forEach(label => {
    label.addEventListener('click', () => {
        label.classList.toggle('selected');
    });
});