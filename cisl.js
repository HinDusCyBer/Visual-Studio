<!DOCTYPE html>
<html>
<head>
    <title>Diffie-Hellman Key Exchange</title>
</head>
<body>
    <h1>Diffie-Hellman Key Exchange</h1>
    <div id="alice">
        <h2>Alice</h2>
        <p>Choose a secret number (a): <input type="number" id="aliceSecret"></p>
        <p>Publicly share your prime number (p) and base (g):</p>
        <p>p: <input type="number" id="primeP" value="23"></p>
        <p>g: <input type="number" id="baseG" value="5"></p>
        <button onclick="aliceGeneratePartialKey()">Generate Partial Key</button>
        <p>Partial Key (A): <span id="partialKeyA"></span></p>
        <p>Received Partial Key (B): <input type="number" id="receivedPartialKeyB"></p>
        <button onclick="aliceCalculateSharedSecret()">Calculate Shared Secret</button>
        <p>Shared Secret: <span id="sharedSecret"></span></p>
    </div>
    <div id="bob">
        <h2>Bob</h2>
        <p>Choose a secret number (b): <input type="number" id="bobSecret"></p>
        <p>Received prime number (p) and base (g):</p>
        <p>p: <span id="receivedPrimeP"></span></p>
        <p>g: <span id="receivedBaseG"></span></p>
        <button onclick="bobGeneratePartialKey()">Generate Partial Key</button>
        <p>Partial Key (B): <span id="partialKeyB"></span></p>
        <p>Received Partial Key (A): <input type="number" id="receivedPartialKeyA"></p>
        <button onclick="bobCalculateSharedSecret()">Calculate Shared Secret</button>
        <p>Shared Secret: <span id="sharedSecret"></span></p>
    </div>

    <script>
        // Common prime number and base
        const primeP = document.getElementById("primeP").value;
        const baseG = document.getElementById("baseG").value;

        let aliceSecret, bobSecret;
        let partialKeyA, partialKeyB;
        let sharedSecretA, sharedSecretB;

        // Alice's actions
        function aliceGeneratePartialKey() {
            aliceSecret = parseInt(document.getElementById("aliceSecret").value);
            partialKeyA = Math.pow(baseG, aliceSecret) % primeP;
            document.getElementById("partialKeyA").textContent = partialKeyA;
        }

        function aliceCalculateSharedSecret() {
            const receivedPartialKeyB = parseInt(document.getElementById("receivedPartialKeyB").value);
            sharedSecretA = Math.pow(receivedPartialKeyB, aliceSecret) % primeP;
            document.getElementById("sharedSecret").textContent = sharedSecretA;
        }

        // Bob's actions
        function bobGeneratePartialKey() {
            bobSecret = parseInt(document.getElementById("bobSecret").value);
            partialKeyB = Math.pow(baseG, bobSecret) % primeP;
            document.getElementById("partialKeyB").textContent = partialKeyB;

            // Share received p and g with Alice
            document.getElementById("receivedPrimeP").textContent = primeP;
            document.getElementById("receivedBaseG").textContent = baseG;
        }

        function bobCalculateSharedSecret() {
            const receivedPartialKeyA = parseInt(document.getElementById("receivedPartialKeyA").value);
            sharedSecretB = Math.pow(receivedPartialKeyA, bobSecret) % primeP;
            document.getElementById("sharedSecret").textContent = sharedSecretB;
        }
    </script>
</body>
</html>
