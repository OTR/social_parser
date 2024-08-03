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
