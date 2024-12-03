
async function solveProblem() {
    const problem = document.getElementById("problem").value;
    
    const response = await fetch('/solve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ problem })
    });
    
    const data = await response.json();
    document.getElementById("solution").innerText = data.solution;
}
