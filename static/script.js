// Toggle dark/light mode
document.querySelector('.toggle-mode').addEventListener('click', function () {
    document.body.classList.toggle('dark-mode');
    const icon = this.querySelector('i');
    icon.className = document.body.classList.contains('dark-mode') ? 'fas fa-sun' : 'fas fa-moon';
});

// Collapse sidebar
document.querySelector('.collapse-btn').addEventListener('click', function () {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('collapsed');
    const icon = this.querySelector('i');
    icon.className = sidebar.classList.contains('collapsed') ? 'fas fa-chevron-right' : 'fas fa-chevron-left';
});

// Analyze button click - modified to interact with Flask backend
document.getElementById('analyze-btn').addEventListener('click', function () {
    performAnalysis();
});

// Also analyze on Enter key in the input field
document.getElementById('input-text').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        performAnalysis();
    }
});

function performAnalysis() {
    const input = document.getElementById('input-text').value.trim();
    const resultsElem = document.getElementById('results');
    const fullResultsElem = document.getElementById('full-results');
    const loader = document.getElementById('loader');
    const analysisBox = document.getElementById('analysis-box');

    // Clear old results
    resultsElem.style.display = 'none';
    fullResultsElem.innerHTML = '';
    const oldDownloadBtn = document.getElementById('download-analysis-btn');
    if (oldDownloadBtn) oldDownloadBtn.remove();

    // Check for empty input
    if (input === '') {
        loader.style.display = 'none'; // Stop any flicker from loader
        resultsElem.style.display = 'none'; // ✅ Ensure hidden while resetting

        // Reset styles in inner box
        analysisBox.style.backgroundColor = '';
        analysisBox.style.borderColor = '';
        fullResultsElem.style.color = '';
        fullResultsElem.innerHTML = ''; // Clear first

        // Then inject yellow warning box
        setTimeout(() => {
            fullResultsElem.innerHTML = `<div style="
                font-family: 'Montserrat', sans-serif;
                background-color: #FFD700;
                color: black;
                font-weight: 600;
                text-align: center;
                padding: 15px 20px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            ">‼️No sentence found</div>`;

            resultsElem.style.display = 'block'; // ✅ Only show after content is ready
        }, 0);

        return;
    }


    loader.style.display = 'block';

    const formData = new FormData();
    formData.append('text', input);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loader.style.display = 'none';
        resultsElem.style.display = 'block';

        const keywordEmojis = {
            "INPUT SENTENCE": "💭",
            "CATEGORY": "🏷️",
            "TYPE": "🧩",
            "SUGGESTED ALTERNATIVES": "♻️",
            "HARMFUL CONTENT": "☠️",
            "TOTAL WORDS": "🔠",
            "FLAGGED PERCENTAGE": "📉",
            "REASON": "📝"
        };

        let formattedResult = data.result;

        // Add space after colons
        formattedResult = formattedResult.replace(/:(?!\s)/g, ': ');

        // Add emojis and formatting
        Object.entries(keywordEmojis).forEach(([keyword, emoji]) => {
            const regex = new RegExp(`\\b(${keyword}):`, 'gi');
            formattedResult = formattedResult.replace(regex, `<br><strong>${emoji} $1:</strong> `);
        });

        // Clean leading <br>
        formattedResult = formattedResult.replace(/^<br>/, '');

        fullResultsElem.innerHTML = formattedResult;

        // Reset any previous styling
        analysisBox.style.backgroundColor = '';
        analysisBox.style.borderColor = '';
        fullResultsElem.style.color = '';

        const resultText = data.result.toLowerCase();

        if (resultText.includes('not cyberbullying')) {
            analysisBox.style.backgroundColor = '#008000'; // green
            analysisBox.style.borderColor = '#008000';
        } else {
            analysisBox.style.backgroundColor = '#eb0707'; // red
            analysisBox.style.borderColor = '#eb0707';
        }

        fullResultsElem.style.color = 'white';

        // Scroll to results
        const offset = 100;
        const resultsPosition = resultsElem.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: resultsPosition, behavior: 'smooth' });

        // Create download button
        const downloadBtn = document.createElement('button');
        downloadBtn.id = 'download-analysis-btn';
        downloadBtn.className = 'analyze-btn';
        downloadBtn.textContent = 'DOWNLOAD ANALYSIS';
        downloadBtn.style.marginTop = '30px';
        downloadBtn.addEventListener('click', () => {
            const blob = new Blob([data.result], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'Analysis.txt';
            a.click();
            URL.revokeObjectURL(url);
        });

        resultsElem.appendChild(downloadBtn);
    })
    .catch(error => {
        console.error('Error:', error);
        loader.style.display = 'none';
        alert('An error occurred during analysis. Please try again.');
    });
}

// QR popup
document.getElementById('qr-link').addEventListener('click', function (e) {
    e.preventDefault();
    document.getElementById('qr-popup').classList.add('active');
});
document.getElementById('close-qr').addEventListener('click', function () {
    document.getElementById('qr-popup').classList.remove('active');
});

// About popup
document.getElementById('about-link').addEventListener('click', function (e) {
    e.preventDefault();
    document.getElementById('about-popup').classList.add('active');
});
document.getElementById('close-about').addEventListener('click', function () {
    document.getElementById('about-popup').classList.remove('active');
});

// Bubble canvas background
const canvas = document.getElementById('bubble-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let bubbles = Array.from({ length: 40 }).map(() => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 8 + 2,
    d: Math.random() * 1 + 0.5
}));

function drawBubbles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let b of bubbles) {
        ctx.beginPath();
        ctx.arc(b.x, b.y, b.r, 0, 2 * Math.PI);
        ctx.fillStyle = 'rgba(67,97,238,0.07)';
        ctx.fill();
        b.y -= b.d;
        if (b.y < -10) b.y = canvas.height + 10;
    }
    requestAnimationFrame(drawBubbles);
}
drawBubbles();

window.addEventListener('resize', function () {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    bubbles = Array.from({ length: 40 }).map(() => ({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 8 + 2,
        d: Math.random() * 1 + 0.5
    }));
});