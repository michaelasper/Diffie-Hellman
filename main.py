import diffie_hellman

def main():
    alice = diffie_hellman.Diffie(256, 53)
    key = alice.get_common()
    bob = diffie_hellman.Diffie(256, 29, key)
    shared_alice = alice.compute_shared()
    shared_bob = bob.compute_shared()
    print(alice.get_shared_secret(shared_bob))
    print(bob.get_shared_secret(shared_alice))


if __name__ == "__main__":
    main()