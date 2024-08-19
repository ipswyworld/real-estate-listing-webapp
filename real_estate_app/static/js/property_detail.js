document.querySelector('.favorite-btn').addEventListener('click', function() {
    const propertyId = this.dataset.propertyId;
    fetch(`/favorite/${propertyId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
    }).then(response => response.json()).then(data => {
        if (data.status === 'added') {
            this.innerHTML = '❤️ Unfavorite';
        } else {
            this.innerHTML = '💙 Favorite';
        }
    });
});
