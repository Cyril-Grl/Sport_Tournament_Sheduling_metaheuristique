if __name__ == "__main__":
    import time
    import argparse
    import random
    from src.init_recherche import init_algo_gen, init_algo_meme, init_algo_meme_modif, \
        recherche_locale_tabou_modif_init, recherche_locale_init, \
        recherche_locale_tabou_init

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="Nombre d'equipes")
    parser.add_argument("-m", type=str, help="RL : recherche locale, RLT : recherche locale avec tabou," +
                                             "RLM : recherche locale modifiee (voir rapport)," +
                                             "AG : algorithmes genetiques," +
                                             "AM : algorithmes memetiques," +
                                             "AMM : algorithmes memetiques modifiees (voir rapport")

    parser.add_argument("-f", type=str, help="nom du fichier pour enregistrer la fitness de l'execution")

    parser.add_argument("-e", type=int, help="nombre d'executions")
    parser.add_argument("-r", type=int, help="graine aléatoire")

    args = parser.parse_args()

    n = args.n if args.n else 8
    m = args.m if args.m else 'RLM'
    f = args.f if args.f else None
    e = args.e if args.e else 1

    print(f'Methode : {m}')

    methodes = {
            "RL" : recherche_locale_init,
            "RLT": recherche_locale_tabou_init,
            "RLM": recherche_locale_tabou_modif_init,
            "AG" : init_algo_gen,
            "AM" : init_algo_meme,
            "AMM": init_algo_meme_modif
    }
    methode = methodes[m]
    stats = {}
    start_time = time.time()
    s = 0
    for i in range(e):
        random.seed(args.r + 1 if args.r else i)
        score, fitness = methode(n)
        s += score
        stats[f'{n}_{i}'] = fitness

    print(f'nombre d equipes = {n}')
    print(f'score = {s}/{e}')
    print(f'temps total = {time.time() - start_time} s')

    if f is not None:
        import json

        with open(f, 'w') as fp:
            json.dump(stats, fp)
