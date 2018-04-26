'''
Sanchit Goel
https://github.com/sngoel/rsa
'''

import math

# Euclid's algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Euclid's extended algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def multiplicative_inverse(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

# Prime Number Validator
def is_prime(n):
    if not n > 1:
        print "Please input a natural number." 
        return False
    if n % 2 == 0 and n > 2 : 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


# Private and Public Key Generator
def generate_keys(p, q):
    n = p * q
    print "n = p * q = ", n

    k = (p - 1) * (q - 1)
    print "k = (p - 1) * (q - 1) = ", k

    e = 2
    g = gcd(e, k)
    print "\nCalculating e:"
    for i in range (2, k):
        g = gcd(e, k)
        if g != 1:
            print "gcd(", e,", ", k,") != 1"
            e = e + 1
        elif g == 1:
            print "gcd(", e,", ", k,") = 1"
            break
    print "\ne = ", e
    
    d = multiplicative_inverse(e, k)
    print "d = ", d

    return ((e, n), (d, n))


# Encryption
def encryption(private_key, plaintext):
    temp_private_key, n = private_key
    cipher = [(ord(char) ** temp_private_key) % n for char in plaintext]
    return cipher


# Decryption
def decryption(public_key, ciphertext):
    temp_public_key, n = public_key
    plain = [chr((char ** temp_public_key) % n) for char in ciphertext]
    return ''.join(plain)    

if __name__ == '__main__':

    print "RSA Encrypter/ Decrypter:"
    p = int(raw_input("\nEnter a prime number: "))
    while not is_prime(p):
    	p = int(raw_input("It is not Prime, Please enter a prime number: "))
    print "p = ", p

    q = int(raw_input("\nEnter another prime number (Different from the one above): "))
    while not is_prime(q):
    	q = int(raw_input("It is not Prime, Please enter a prime number: "))
    
    while q == p :
    	print('\nBoth the numbers cannot be same.')
    	q = q = int(raw_input("Please enter a different prime number (other than p): "))
    	if not is_prime(q):
    		continue    	 	
    print "q = ", q

    print "\nGenerating Public & Private keys..."
    public, private = generate_keys(p, q)
    print "Your Public key is ", public ," and your Private key is ", private

    message = raw_input("\nEnter a message to encrypt with your private key: ")
    encrypted_msg = encryption(private, message)
    print "Your encrypted message is: "
    val = ''.join(map(lambda x: str(x), encrypted_msg))
    print gcd(int(val), 26)

    print "\nDecrypting the encrypted message with public key,"
    print "Your message is:"
    print decryption(public, encrypted_msg)