import itertools

def tikz_permutations(n):
    # Creare una lista di n colori
    colors = ["red", "green", "blue", "yellow"]  # Aggiungi altri colori se necessario

    # Calcolare tutte le permutazioni di n colori
    all_permutations = list(itertools.permutations(colors[:n]))

    # Aprire il file .txt per la scrittura
    with open("tikz_permutations.txt", "w") as f:
        # Scrivere l'inizio del documento e del tabular environment
        f.write("\\begin{center}\n")
        f.write("\\begin{tabular}{ " + " c"*n + " }\n")

        # Scrivere ciascuna permutazione come una riga di palline colorate
        for permutation in all_permutations:
            row = []
            for color in permutation:
                row.append(f"\\begin{{tikzpicture}}\\draw [fill={color}] (0,0) circle (0.2);\\end{{tikzpicture}}")
            f.write(" & ".join(row) + " \\\\\n")

        # Scrivere la fine del tabular environment e del documento
        f.write("\\end{tabular}\n")
        f.write("\\end{center}\n")

n = 4  # Cambia questo valore per rappresentare un numero diverso di colori
tikz_permutations(n)
