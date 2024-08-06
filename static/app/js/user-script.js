function loadIframeOnCollapse(event) {
    var button = event.target;
    var collapseId = button.getAttribute('data-target').substring(1);
    var collapseElement = document.getElementById(collapseId);
    var videoId = collapseElement.getAttribute('data-video-id');

    if (!collapseElement.getAttribute('data-iframe-loaded')) {
        var iframe = document.createElement('iframe');
        iframe.className = 'embed-responsive-item';
        iframe.src = 'https://www.youtube.com/embed/' + videoId + '?rel=0';
        iframe.allowFullscreen = true;
        collapseElement.appendChild(iframe);
        collapseElement.setAttribute('data-iframe-loaded', 'true');
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submitHighlighterForm() {
    const form = document.getElementById('highlighterForm');
    const formData = new FormData(form);
    const csrftoken = getCookie('csrftoken');

    fetch('/api/add/highlighter/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            channel_id: formData.get('channel_id'),
            channel_title: formData.get('channel_title'),
            // published_at: formData.get('published_at'),
            reason: formData.get('reason')
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            console.log('Marked as highlighter successfully!');
        } else {
            console.log('Failed to mark as highlighter');
        }
    })
    .catch(error => console.error('Error:', error));
}
