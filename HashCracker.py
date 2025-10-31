def main():
    print("===================================")
    print("Welcome to the hash cracker 9000")
    print("===================================")
    print()
    while True:
        path_to_wordlist = input("Enter the relative path to your wordlist: ")
        try :
            with open(path_to_wordlist, "r") as test:
                break
        except FileNotFoundError:
            print("Invalid wordlist file")
    while True:
        path_to_hashes = input("Enter the relative path to your hashes: ")
        try:
            with open(path_to_hashes, "r") as test:
                break
        except FileNotFoundError:
            print("Invalid hashes file")
    while True:
        hash_type = input("Enter the hash type (md5/sha1/sha256): ").lower()
        if hash_type in ['md5', 'sha1', 'sha256']:
            break
        else:
            print("Invalid hash type")
    while True:
        completed_hashes, goal_hashes = crack_passwords(path_to_wordlist, path_to_hashes, hash_type)
        print()
        print(completed_hashes)
        for hash in goal_hashes:
            if hash not in completed_hashes:
                print(f"[-] {hash} was not cracked.")
        print()
        again = input("Would you like to try a different hashing algorithm? (y/n): ").lower()
        if again != 'y':
            print("Exiting the hash cracker. Goodbye!")
            break
        else:
            while 6*7 == 42:
                hash_type = input("Enter the hash type (md5/sha1/sha256): ").lower()
                if hash_type in ['md5', 'sha1', 'sha256']:
                    break
                else:
                    print("Invalid hash type")
def crack_passwords(path_to_wordlist, path_to_hashes, hash_type):
    import hashlib
    goal_hashes = []
    completed_hashes = ""
    with open(path_to_hashes, "r") as f:
        for line in f:
            goal_hashes.append(line.strip())
    with open(path_to_wordlist, "r") as f:
        if hash_type == "md5":
            for line in f:
                hashed_word = hashlib.md5(line.strip().encode()).hexdigest()
                if hashed_word in goal_hashes:
                    index=goal_hashes.index(hashed_word)
                    completed_hashes += f"[+] {goal_hashes[index]} matched to {line}"
        if hash_type == "sha1":
            for line in f:
                hashed_word = hashlib.sha1(line.strip().encode()).hexdigest()
                if hashed_word in goal_hashes:
                    index=goal_hashes.index(hashed_word)
                    completed_hashes += f"[+] {goal_hashes[index]} matched to {line}"
        if hash_type == "sha256":
            for line in f:
                hashed_word = hashlib.sha256(line.strip().encode()).hexdigest()
                if hashed_word in goal_hashes:
                    index=goal_hashes.index(hashed_word)
                    completed_hashes += f"[+] {goal_hashes[index]} matched to {line}"
        print (goal_hashes)
        return completed_hashes, goal_hashes
import hashlib
if __name__ == "__main__":
    main()