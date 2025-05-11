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

// Analyze button click
document.querySelector('.analyze-btn').addEventListener('click', function () {
    const input = document.querySelector('.input-field').value;
    if (input.trim() !== '') {
        document.getElementById('results').style.display = 'block';

        const resultsElement = document.getElementById('results');
        const offset = 100;
        const resultsPosition = resultsElement.getBoundingClientRect().top;
        const offsetPosition = resultsPosition + window.pageYOffset - offset;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });

        // Animate metric bars
        const bars = document.querySelectorAll('.metric-value');
        bars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0';
            setTimeout(() => { bar.style.width = width; }, 100);
        });
    }
});

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
