<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diffie-Hellman Key Exchange</title>
</head>
<body>
    <h1>Diffie-Hellman Key Exchange</h1>
    
    <script>
        // Common parameters (p and g) - These should be agreed upon by both parties
        const p = 23; // A prime number
        const g = 5;  // A primitive root modulo p

        // Alice's private key
        const alicePrivateKey = Math.floor(Math.random() * p) + 1;

        // Bob's private key
        const bobPrivateKey = Math.floor(Math.random() * p) + 1;

        // Calculate Alice's public key
        const alicePublicKey = (g ** alicePrivateKey) % p;

        // Calculate Bob's public key
        const bobPublicKey = (g ** bobPrivateKey) % p;

        // Exchange public keys (usually over a network, but here we'll simulate it)
        const exchangedAlicePublicKey = alicePublicKey;
        const exchangedBobPublicKey = bobPublicKey;

        // Calculate the shared secret
        const aliceSharedSecret = (exchangedBobPublicKey ** alicePrivateKey) % p;
        const bobSharedSecret = (exchangedAlicePublicKey ** bobPrivateKey) % p;

        // The shared secrets should match
        if (aliceSharedSecret === bobSharedSecret) {
            console.log("Shared secret:", aliceSharedSecret);
            alert("Shared secret matches! Key exchange successful.");
        } else {
            console.log("Shared secrets do not match.");
            alert("Key exchange failed.");
        }
    </script>
</body>
</html>