document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('downloadForm');
    const loadingDiv = document.getElementById('loading');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Verhindert das Standardformularverhalten

        // Zeige die Ladeanzeige an
        loadingDiv.style.display = 'block';
        resultDiv.innerHTML = '';

        const formData = new FormData(form);

        fetch('/download', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                // Extrahiere den Dateinamen aus dem Content-Disposition-Header
                const contentDisposition = response.headers.get('Content-Disposition');
                let fileName = 'video.mp4'; // Fallback-Name
                if (contentDisposition && contentDisposition.includes('filename=')) {
                    const matches = contentDisposition.match(/filename="(.+)"/);
                    if (matches && matches[1]) {
                        fileName = matches[1];
                    }
                }
                return response.blob().then(blob => ({ blob, fileName }));
            } else {
                throw new Error('Failed to download video.');
            }
        })
        .then(({ blob, fileName }) => {
            // Erstelle einen Download-Link mit dem richtigen Dateinamen
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = fileName; // Dynamischer Dateiname
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);

            // Verstecke die Ladeanzeige und zeige Erfolgsmeldung
            loadingDiv.style.display = 'none';
            resultDiv.innerHTML = '<p class="text-success">Download completed successfully!</p>';
        })
        .catch(error => {
            // Verstecke die Ladeanzeige und zeige Fehlermeldung
            loadingDiv.style.display = 'none';
            resultDiv.innerHTML = `<p class="text-danger">Error: ${error.message}</p>`;
        });
    });
});