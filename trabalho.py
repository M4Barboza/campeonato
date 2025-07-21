
from dataclasses import dataclass


def lista_de_times(jogos: list[str]) -> list[str]:
    ''' 
    Recebe a lista de jogos e retorna uma lista com o nome 
    de todos os times que participaram, sem repetir nenhum.

    >>> lista_de_times(["Flamengo 2 Vasco 1", "Palmeiras 3 Flamengo 2"])
    ['Flamengo', 'Vasco', 'Palmeiras']
    >>> lista_de_times(["Sao-Paulo 1 Atletico-PR 2", "Flamengo 0 Palmeiras 1"])
    ['Sao-Paulo', 'Atletico-PR', 'Flamengo', 'Palmeiras']
    '''
    times = []

    for jogo in jogos:
        equipes = nome_dos_times(jogo)

        if not ja_esta_na_lista(times, equipes.anfitriao):
            times.append(equipes.anfitriao)

        if not ja_esta_na_lista(times, equipes.visitantes):
            times.append(equipes.visitantes)

    return times


def ja_esta_na_lista(lista: list[str], time: str) -> bool:
    ''' 
    Verifica se o time já está na lista.

    >>> ja_esta_na_lista(['Flamengo', 'Vasco'], 'Flamengo')
    True
    >>> ja_esta_na_lista(['Sao-Paulo', 'Atletico-PR'], 'Flamengo')
    False
    '''
    found = False
    i = 0
    while not found and i < len(lista):
        if lista[i] == time:
            found = True
        i += 1
    return found


@dataclass
class Nome_times:
    anfitriao: str
    visitantes: str


def nome_dos_times(jogo: str) -> Nome_times:
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


def vitorias(placar: list[Placar]) -> int:
    '''
    Recebe uma lista de placares e retorna uma lista com o número de vitórias de cada time.

    >>> vitorias([Placar(1, 0), Placar(2, 1), Placar(0, 3)])
    [2, 1]
    >>> vitorias([Placar(0, 1), Placar(3, 3), Placar(2, 0)])
    [1, 1]
    '''
    vitoria_anfitriao = 0
    vitoria_visitante = 0
    empate = 0

    for p in placar:
        if p.gol_anfitriao > p.gol_visitante:
            vitoria_anfitriao += 1
        elif p.gol_anfitriao < p.gol_visitante:
            vitoria_visitante += 1
    else:
        empate += 1
    return [vitoria_anfitriao, vitoria_visitante, empate]


@dataclass
class Jogo:
    anfitriao: str
    gol_anfitriao: int
    visitante: str
    gol_visitante: int


def saldo_gols(lista: list[str]) -> Jogo:
    '''
    Recebe uma lista de strings representando jogos e retorna uma lista de objetos Jogo, mostrando o nome do anfitriao e visitantes
    e o número de gols marcados por cada um.
    jogos str = ["Flamengo 2 Vasco 1", "Palmeiras 3 Sao-Paulo 0"]
    retorna lista de objetos Jogo
    >>> saldo_gols(["Flamengo 2 Vasco 1", "Palmeiras 3 Sao-Paulo 0"])
    [Jogo(anfitriao='Flamengo', gol_anfitriao=2, visitante='Vasco', gol_visitante=1), Jogo(anfitriao='Palmeiras', gol_anfitriao=3, visitante='Sao-Paulo', gol_visitante=0)]
    >>> saldo_gols(["Sao-Paulo 1 Atletico-PR 2", "Flamengo 0 Palmeiras 1"])
    [Jogo(anfitriao='Sao-Paulo', gol_anfitriao=1, visitante='Atletico-PR', gol_visitante=2), Jogo(anfitriao='Flamengo', gol_anfitriao=0, visitante='Palmeiras', gol_visitante=1)]
    '''
    jogos = []
    for j in lista:
        espacos = espacos_i(j)

        anfitriao = j[:espacos[0]]
        gol_anfitriao = int(j[espacos[0] + 1])
        visitante = j[espacos[1] + 1: espacos[2]]
        gol_visitante = int(j[espacos[2] + 1])

        jogos.append(Jogo(anfitriao, gol_anfitriao, visitante, gol_visitante))
    return jogos


print(saldo_gols(["Flamengo 2 Vasco 1", "Palmeiras 3 Sao-Paulo 0"]))


def pontos(placar: list[Placar]) -> list[int]:
    '''
    Recebe uma lista de placares e retorna uma lista com os pontos de cada time.
    Cada vitória vale 3 pontos, empate vale 1 ponto e derrota vale 0 pontos.

    >>> pontos([Placar(1, 0), Placar(2, 1), Placar(0, 3)])
    [6, 3]
    >>> pontos([Placar(0, 1), Placar(3, 3), Placar(2, 0)])
    [4, 4]
    '''
    pontos_anfitriao = 0
    pontos_visitante = 0

    for p in placar:
        if p.gol_anfitriao > p.gol_visitante:
            pontos_anfitriao += 3
        elif p.gol_anfitriao < p.gol_visitante:
            pontos_visitante += 3
        else:
            pontos_anfitriao += 1
            pontos_visitante += 1

    return [pontos_anfitriao, pontos_visitante]


@dataclass
class Time:
    nome: str
    vitorias: int
    saldo_gols: int
    pontos: int


def ordenar_times(estatis: list[Time]) -> list[Time]:
    '''
    Recebe uma lista de times e retorna a lista ordenada por pontos, saldo de gols e vitorias.
    ordenar_times([Time('Flamengo', 10, 5, 30), Time('Vasco', 8, 3, 24)])
    >>>[Time(nome='Flamengo', vitorias=10, saldo_gols=5, pontos=30), Time(nome='Vasco', vitorias=8, saldo_gols=3, pontos=24)]

    ordenar_times([Time('Sao-Paulo', 12, 6, 36), Time('Palmeiras', 11, 4, 33)])
    >>>[Time(nome='Sao-Paulo', vitorias=12, saldo_gols=6, pontos=36), Time(nome='Palmeiras', vitorias=11, saldo_gols=4, pontos=33)]


    '''
    for i in range(len(estatis)):
        for j in range(i + 1, len(estatis)):
            if (estatis[i].pontos < estatis[j].pontos or
                (estatis[i].pontos == estatis[j].pontos and estatis[i].saldo_gols < estatis[j].saldo_gols) or
                    (estatis[i].pontos == estatis[j].pontos and estatis[i].saldo_gols == estatis[j].saldo_gols and estatis[i].vitorias < estatis[j].vitorias)):
                estatis[i], estatis[j] = estatis[j], estatis[i]
    return estatis
