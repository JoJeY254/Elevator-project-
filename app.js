window.onload = () => {
    document.getElementById('log-display').innerHTML = "<b>System:</b> Ready.";
    // Start with doors open at Ground
    document.getElementById('elevator').classList.add('open');
};

async function requestFloor(floor) {
    const elevator = document.getElementById('elevator');
    const logDisplay = document.getElementById('log-display');
    const queueDisplay = document.getElementById('queue-display');

    const label = floor === 0 ? "Ground" : `Floor ${floor}`;

    // 1. Close doors before moving
    elevator.classList.remove('open');
    logDisplay.innerHTML += `<br><b>[User]</b>: ${label} (Closing Doors)`;

    // 2. Move (Wait a tiny bit for door animation to look real)
    setTimeout(() => {
        const position = floor * 80; 
        elevator.style.transform = `translateY(-${position}px)`;
    }, 300);

    // 3. Arrival & Door Logic
    setTimeout(() => {
        elevator.classList.add('open');
        logDisplay.innerHTML += `<br><b>[System]</b>: Arrived at ${label}`;
    }, 1800); // 1.5s move + 0.3s delay

    // 4. API Request
    try {
        const response = await fetch('/api/request', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({floor: floor})
        });
        const data = await response.json();
        queueDisplay.innerText = `Queue: [${data.queue}]`;
    } catch (e) {
        console.error("Connection failed");
    }
}