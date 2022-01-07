import pickle

hobbys = ["Invest in crypto", "Listen to music", "Be a mathematician", "FUCK WITH THE MARKET"]

with open("Pippex's_hobbys", "wb") as binary_file:
    pickle.dump(hobbys, binary_file)
    

with open("Pippex's_hobbys", "rb") as binary_file:
    pippex_is_god = pickle.load(binary_file)
    print(pippex_is_god)

pray_to_pippex = "PIPPEX IS MY GOD, I LOVE PIPPEX, I WANT TO FUCK WITH PIPPEX"

with open("i_love_pippex", "wb") as binary_pray:
    binary_file = pickle.dump(pray_to_pippex, binary_pray)

#with open("i_love_pippex", "ab") as binary_pray:
#    binary_file = pickle.dump("PIPPEX PLEASE DESTROY MY ASS", binary_file)

with open("i_love_pippex", "rb") as binary_pray:
    print(pickle.load(binary_pray))

