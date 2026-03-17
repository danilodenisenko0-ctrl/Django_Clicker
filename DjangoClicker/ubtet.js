// функція для отримання CSRF токену з cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.querySelector('#buy-btn').addEventListener('click', function() {
    fetch("/buy/1/", { // заміни 1 на upgrade.id
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => console.log(data));
});