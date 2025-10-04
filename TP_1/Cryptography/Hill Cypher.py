import itertools, math

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 26

def clean(text):
    return "".join([c for c in text.upper() if c.isalpha()])

def text_to_nums(text):
    return [ALPHABET.index(c) for c in text]

def nums_to_text(nums):
    return "".join(ALPHABET[n % MOD] for n in nums)

def chunk2(nums):
    if len(nums) % 2 != 0:
        nums.append(ALPHABET.index("X"))
    return [nums[i:i+2] for i in range(0, len(nums), 2)]

def modinv(a, m):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    return None

def inv_key(key):
    a,b,c,d = key[0][0],key[0][1],key[1][0],key[1][1]
    det = (a*d - b*c) % MOD
    inv_det = modinv(det, MOD)
    if inv_det is None: return None
    return [[ d*inv_det % MOD, -b*inv_det % MOD],
            [-c*inv_det % MOD,  a*inv_det % MOD]]

def mul(mat, vec):
    return [(mat[0][0]*vec[0] + mat[0][1]*vec[1]) % MOD,
            (mat[1][0]*vec[0] + mat[1][1]*vec[1]) % MOD]

def encrypt(text, key):
    nums = text_to_nums(clean(text))
    return nums_to_text(sum([mul(key, v) for v in chunk2(nums)], []))

def decrypt(text, key):
    inv = inv_key(key)
    if not inv: return None
    nums = text_to_nums(clean(text))
    return nums_to_text(sum([mul(inv, v) for v in chunk2(nums)], []))

def brute_force(cipher, crib=None, max_out=10):
    results = []
    for a,b,c,d in itertools.product(range(26), repeat=4):
        det = (a*d - b*c) % 26
        if math.gcd(det,26) != 1: continue
        key = [[a,b],[c,d]]
        pt = decrypt(cipher, key)
        if pt and (crib is None or crib in pt):
            results.append((key, pt))
            if len(results) >= max_out: break
    return results

# ---------------- Menu-driven ----------------
def main():
    while True:
        print("\n===== Hill Cipher Menu =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter plaintext: ")
            key = [[3,3],[2,5]]   # fixed example key, you can modify
            cipher = encrypt(text, key)
            print("Ciphertext:", cipher)

        elif choice == "2":
            text = input("Enter ciphertext: ")
            key = [[3,3],[2,5]]   # same fixed key
            plain = decrypt(text, key)
            if plain:
                print("Decrypted:", plain)
            else:
                print("Invalid key, cannot decrypt.")

        elif choice == "3":
            text = input("Enter ciphertext to brute force: ")
            crib = input("Enter crib (known word, optional, press Enter to skip): ").strip().upper() or None
            results = brute_force(text, crib=crib, max_out=10)
            if not results:
                print("No matches found.")
            else:
                for k, pt in results:
                    print("Key:", k, "-> Plaintext:", pt)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

main()
