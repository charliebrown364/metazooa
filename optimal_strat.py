# Serine's optimal strat: https://discord.com/channels/1110266150106976297/1143347084930601034/1147388403009196103

def get_next_optimal_guess(animal: str, clade_name: str) -> str:
    
    animal_maps = {
        # weasel
        "weasel": {
            "Eumetazoa": "coral",
            "Bilateria": "ant",
            "Deuterostomia": "urchin",
            "Gnathostomata": "tiger shark", # tied with hammerhead shark, goblin shark, and great white shark
            "Euteleostomi": "pufferfish",
            "Tetrapoda": "poison frog",
            "Amniota": "crow",
            "Mammalia": "platypus", # tied with echidna
            "Theria": "kangaroo", # tied with koala, wombat, and possum
            "Eutheria": "anteater", # tied with two-toed sloth
            "Boreotheria": "mouse",
            "Laurasiatheria": "cow",
            "Carnivora": "lynx", # tied with bobcat
            "Caniformia": "wolf",
            "Musteloidea": "skunk", # tied with raccoon and red panda
            "Mustelidae": "sea otter", # tied with river otter, wolverine, badger
            "Mustela": "mink"
        },
        # going down the tree to weasel, w/out subtrees
        "coral": {
            "Hexacroallia": "anemone",
            "Cnidaria": "jellyfish" # tied with man o war
        },
        "jellyfish": {
            "Cnidaria": "man o war"
        },
        "ant": {
            # see subtree
        },
        "urchin": {
            "Euechinoidea": "sand dollar",
            "Echinozoa": "sea cucumber",
            "Eleutherozoa": "starfish"
        },
        "tiger shark": {
            "Elasmobranchii": "string ray",
            "Galeoidea": "great white shark",
            "Carcharhinidae": "hammerhead shark"
        },
        "string ray": {
            "Myliobatiformes": "manta ray"
        },
        "great white shark": {
            "Galeoidea": "goblin shark"
        },
        "pufferfish": {
            # see subtree
        },
        "poison frog": {
            "Amphibia": "axolotl",
            "Neobrachia": "frog",
            "Hyloidea": "toad"
        },
        "axolotl": {
            "Caudata": "salamander"
        },
        "crow": {
            # see subtree
        },
        "platypus": {
            "Monotremata": "echidna"
        },
        "kangaroo": {
            "Diprotodontia": "koala", # tied with wombat and possum
            "Metatheria": "tasmanian devil" # tied with opossum
        },
        "koala": {
            "Diprotodontia": "wombat" # tied with possum
        },
        "wombat": {
            "Diprotodontia": "possum"
        },
        "tasmanian devil": {
            "Metatheria": "opossum"
        },
        "anteater": {
            "Eutheria": "elephant", # tied with aardvark and manatee
            "Xenarthra": "armadillo",
            "Pilosa": "two-toed sloth"
        },
        "elephant": {
            "Afrotheria": "aardvark" # tied with manatee
        },
        "aardvark": {
            "Afrotheria": "manatee"
        },
        "mouse": {
            # see subtree
        },
        "skunk": {
            "Musteloidea": "raccoon" # tied with red panda
        },
        "raccoon": {
            "Musteloidea": "red panda"
        },
        "sea otter": {
            "Mustelidae": "badger", # tied with wolverine
            "Lutrinae": "river otter"
        },
        "badger": {
            "Mustelidae": "wolverine"
        },
        # wolf subtree
        "wolf": {
            "Caniformia": "polar bear", # tied with black bear and brown bear
            "Canidae": "red fox", # tied with arctic fox
            "Canis": "coyote" # tied with jackal
        },
        "polar bear": {
            "Caniformia": "seal", # tied with sea lion and walrus
            "Ursidae": "giant panda",
            "Ursus": "black bear" # tied with brown bear
        },
        "seal": {
            "Pinnipedia": "sea lion" # tied with walrus
        },
        "sea lion": {
            "Pinnipedia": "walrus"
        },
        "black bear": {
            "Ursus": "brown bear"
        },
        "red fox": {
            "Vulpes": "arctic fox"
        },
        "coyote": {
            "Canis": "jackal"
        },
        # lynx subtree
        "lynx": {
            "Feliformia": "mongoose", # tied with meerkat
            "Felidae": "lion", # tied with jaguar, tiger, and leopard
            "Felinae": "cat", # tied with puma and ocelot
            "Lynx": "bobcat"
        },
        "mongoose": {
            "Feliformia": "hyena",
            "Herpestidae": "meerkat"
        },
        "lion": {
            "Felidae": "cheetah",
            "Panthera": "jaguar" # tied with tiger and leopard
        },
        "jaguar": {
            "Panthera": "tiger" # tied with leopard
        },
        "tiger": {
            "Panthera": "leopard"
        },
        "cat": {
            "Felinae": "puma", # tied with ocelot
        },
        "puma": {
            "Felinae": "ocelot"
        },
        # cow subtree
        "cow": {
            "here": "here"
        },

    }

    try:
        return animal_maps[animal][clade_name.capitalize()]
    except:
        print("There's a mistake with the strategy. No animal is found.")
        return "[error]"

"""

subtree for cow:
Laurasiatheria again -> horse (Equus -> donkey, zebra) (Perissodactyla -> rhino), bat (Chiroptera -> bat), mole (Eulipotyphla -> hedgehog), pangolin
Artiodactyla -> dolphin (Whippomorpha -> Hippopotamus) (Cetacea -> humpback) (Odontoceti -> beluga [Monodontidae: narwhal], sperm whale) (Delphinidae -> orca), camel (Camelidae -> llama, alpaca), pig
Pecora -> deer (Odocoileinae -> caribou, moose) (Cervidae -> elk), giraffe
Bovidae -> goat (Caprinae -> sheep), antelope, gazelle
Bovinae -> bison, buffalo
Bos -> yak

subtree for mouse:
Euarchontoglires -> (Euarchonta) -> chimpanzee (Primate -> lemur) (Simiiformes -> capuchin) (Catarrhini -> macaque, mandrill, baboon) (Homoinoidea -> gibbon) (Hominidae -> orangutan) (Homininae -> human, gorilla) (Pan -> bonobo)
Glires -> rabbit
Rodentia -> capybara (Hystricomorpha -> porcupine, guinea), squirrel (Marmotini -> groundhog, chipmunk) (Scurinae -> squirrel), beaver
Muroidea -> hamster
Muridae -> gerbil
Murinae -> rat

subtree for crow:
Sauria -> viper (see subtree)
Archelosauria -> box turtle (Durocryptodira -> turtle, turtle) (Testudinoidea -> tortoise)
Archosauria -> alligator (Crocodylia -> crocodile) (Alligatoridae -> caiman)
Aves -> ostrich, emu, kiwi
Neognathae -> chicken (see subtree)
Passeriformes -> finch (Passeroidea -> sparrow) (Fringillidae -> canary), blackbird (Turdidae -> robin, nightingale), mockingbird
Corvidae -> jay, magpie
Corvus -> raven
 
subtree for chicken:
Neognathae -> parrot (Psittacidae -> parakeet, macaw) (Psittacifomes -> cockatoo, cockatiel), hawk (Accipitrinae -> vulture, eagle) (Accipitrifomes -> condor), macaroni penguin (Eudyptes -> rockhopper) (Spheniscidae -> emperor), owl (Strigiformes -> owl), falcon (Falco -> kestrel), puffin (Charadriiformes -> seagull), dove (Columbidae -> pigeon), albatross, toucan (_ -> wooodpecker), flamingo
Galloanserae ->  swan (Anserinae -> goose) (Anatidae -> duck)
Phasianidae -> turkey
Phasianinae -> pheasant, peacock

subtree for viper:
Squamata -> gecko
Toxicofera -> iguana (Iguania -> chameleon), gila (Anguimorpha -> komodo)
Serpentes -> anaconda (Henophidia -> python) (Boinae -> boa)
Colubroidea -> mamba (Elapinae -> cobra), snake
Viperidae -> rattlesnake

subtree for frog:
Neobatrachia -> bullfrog
Hyloidea -> toad

subtree for pufferfish:
Osteoglossocephalai -> eel (Characiphysae -> piranha, catfish) (Otophysi -> goldfish, carp)
Euteleosteomorpha -> salmon (Salmonidae -> trout)
Acanthomorphata -> cod
Percomorphaceae -> barracuda (Carangaria -> swordfish), clownfish (Ovalentaria -> guppy), seahorse, tuna
Eupercaria -> bass, anglerfish
 
subtree for ant:
Protostomia -> squid (see subtree)
Arthropoda -> spider (Arachnida -> scorpion) (Araneae -> tarantula) (Entelegynae -> widow)
Mandibulata -> centipede (Myriapoda -> millipede)
Pancrustacea -> crab (Multicrustacea -> barnacle)  (Eumalacostraca -> shrimp, pillbug) (Eucarida -> krill) (Pleocyemata -> lobster, prawn)
Pterygota -> dragonfly (Paleoptera -> mayfly)
Neoptera -> cockroach (Polyneoptera -> grasshopper [Schistocerca -> locust] [Orthoptera -> cricket], stick bug, earwig) (Dictyoptera -> praying mantis) (Blattoidea -> termite)
Endopterygota -> beetle (Polyphaga -> ladybug, firefly) (Scarabaeidae -> beetle), fly (Diptera -> mosquito) (Cyclorrhapha -> fruit fly), moth (Obtectomera -> butterfly) (Bombycoidea -> silkworm)
Aculeata -> bee (Apinae -> bee), wasp (Vespinae -> hornet)
Formicidae -> ant

subtree for squid:
Lophotrochozoa -> leech, worm
Mollusca -> oyster (Autobranchia -> clam) (Pteriamorpha -> mussel), snail (Helicina -> slug)
Cephalopoda -> nautilus
Coleoidea -> octopus (Octopodidae -> octopus)
Decapodiformes -> squid, cuttlefish

"""

def run_strat():

    optimal_guess = "weasel"
    print(f"\nThe most optimal initial guess is {optimal_guess}.")

    while True:
        clade_name = input("\nWhat is the most closely related group name? ")
        optimal_guess = get_next_optimal_guess(optimal_guess, clade_name)
        print(f"The next most optimal guess is {optimal_guess}.")

if __name__ == "__main__":
    run_strat()