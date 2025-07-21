from dataclasses import dataclass


@dataclass
class Nome_times:
    anfitriao: str
    visitantes: str


def nome_das_equipes(jogo: str) -> Nome_times:
    ''' Recebe uma única string representando um jogo
        e extrair o nome das equipes (anfitrião e visitante).

    >>> nome_das_equipes("Palmeiras 1 Corinthians 0")
    nome_times(anfitriao='Palmeiras', visitantes='Corinthians')
    >>> nome_das_equipes("Flamengo 2 Vasco 1")
    nome_times(anfitriao='Flamengo', visitantes='Vasco')
    >>> nome_das_equipes("Sao-Paulo 3 Atletico-PR 2")
    nome_times(anfitriao='Sao-Paulo', visitantes='Atletico-PR')

    '''
    espacos = []

    for i in range(len(jogo)):
        if jogo[i] == " ":
            espacos.append(i)

    # vai do inicio até o espaço antras do placar do anfitrião
    anfitriao = jogo[:espacos[0]]

    # vai do espaço depois do placar do anfitrião até antes ao do visitante
    visitante = jogo[espacos[1] + 1: espacos[2]]

    jogos = Nome_times(anfitriao, visitante)

    return jogos


print(nome_das_equipes("Palmeiras 1 Corinthians 0"))


def espacos_i(jogo: str) -> list[int]:
    """
    Retorna uma lista com os índices dos espaços em branco na string do jogo.

    >>> espacos("Flamengo 2 Vasco 1")
    [8, 10, 16]
    >>> espacos("Sao-Paulo 1 Atletico-PR 2")
    [11, 13, 21]
    >>> espacos("Palmeiras 3 Fluminense 1")
    [10, 12, 22]
    """
    espacos = []
    for i in range(len(jogo)):
        if jogo[i] == " ":
            espacos.append(i)
    return espacos


@dataclass
class Placar:
    gol_anfitriao: int
    gol_visitante: int


def placar_jogo(lst: list[str]) -> list[Placar]:
    '''
placar_jogo recebe uma lista de strings representando jogos
e sai uma lista com o resultado dos placares.
>>> placar_jogo(["Fluminense 1 Corinthians 0", "Corinthians 9 Flamengo 0"])
[Placar(gol_anfitriao=1, gol_visitante=0), Placar(gol_anfitriao=9, gol_visitante=0)]
>>> placar_jogo(["Sao-Paulo 1 Atletico-PR 2", "Flamengo 0 Palmeiras 1"])
[Placar(gol_anfitriao=1, gol_visitante=2), Placar(gol_anfitriao=0, gol_visitante=1)]

    '''
    placares = []
    for j in lst:
        espacos_g = espacos_i(j)

        # pega os gols do anfitriao
        gol_anfitriao = int(j[espacos_g[0] + 1])
       # pega os gols do visitante
        gol_visitante = int(j[espacos_g[2] + 1])

        placares.append(Placar(gol_anfitriao, gol_visitante))

    return placares


# Agora funciona corretamente
print(placar_jogo(["Fluminense 1 Corinthians 0", "Corinthians 9 Flamengo 0"]))
