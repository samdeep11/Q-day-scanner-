import ssl
import socket

def scan_domain(domain):
    print(f"🔍 Scanning {domain} for Q-Day Risk...\n")
    try:
        # SSL check
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                print(f"✅ Site LIVE: {domain}")
                print(f"🔐 Cipher: {cipher[0]}")

                # Simple Quantum check
                if "RSA" in str(cipher) or "ECDHE" in str(cipher[0]):
                    print("\n🚨 RESULT: HIGH RISK - Quantum Vulnerable!")
                    print("Reason: Using RSA/ECC - Quantum can break it.")
                    print("\n💡 Fix: Upgrade to PQC (Dilithium / Kyber)")
                    print("📩 Contact: Sandeep @samdeep11 for $20 detailed report")
                else:
                    print("\n✅ RESULT: Possibly Safe")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Try without https, like: example.com")

# Change domain here
scan_domain("google.com")