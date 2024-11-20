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
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submitHighlighterForm(formId) {
    const form = document.getElementById(formId);
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
            reason: formData.get('reason')
        })
    })
    .then(response => {
        if (response.status === 201) {
            return response.json();
        } else {
            throw new Error('Failed to mark as highlighter');
        }
    })
    .then(data => {
        const notificationContainer = document.getElementById('notificationContainer');
        const alert = document.createElement('div');
        alert.className = 'alert alert-success alert-dismissible fade show';
        alert.role = 'alert';
        alert.innerHTML = `
            ${data.channel_title} Marked as highlighter successfully!
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        notificationContainer.appendChild(alert);
    })
    .catch(error => {
        const notificationContainer = document.getElementById('notificationContainer');
        const alert = document.createElement('div');
        alert.className = 'alert alert-danger alert-dismissible fade show';
        alert.role = 'alert';
        alert.innerHTML = `
            ${error.message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        notificationContainer.appendChild(alert);
    });
}

function submitRejectedForm(formId) {
    const form = document.getElementById(formId);
    const formData = new FormData(form);
    const csrftoken = getCookie('csrftoken');
    const datetime = formData.get('published_at');
    console.log(datetime);

    fetch('/api/add/rejected/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title: formData.get('title'),
            published_at: formData.get('published_at'),
            channel_title: formData.get('channel_title'),
            video_id: formData.get('video_id'),
            description: formData.get('description'),
            reason: formData.get('reason')
        })
    })
    .then(response => {
        if (response.status === 201) {
            return response.json();
        } else {
            throw new Error('Failed to add to Rejected');
        }
    })
    .then(data => {
        const notificationContainer = document.getElementById('notificationContainer');
        const alert = document.createElement('div');
        alert.className = 'alert alert-success alert-dismissible fade show';
        alert.role = 'alert';
        alert.innerHTML = `
            ${data.title} Added to rejected successfully!
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        notificationContainer.appendChild(alert);
    })
    .catch(error => {
        const notificationContainer = document.getElementById('notificationContainer');
        const alert = document.createElement('div');
        alert.className = 'alert alert-danger alert-dismissible fade show';
        alert.role = 'alert';
        alert.innerHTML = `
            ${error.message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        notificationContainer.appendChild(alert);
    });
}
