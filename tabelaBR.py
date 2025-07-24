import sys
from dataclasses import dataclass


def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    jogos = le_arquivo(sys.argv[1])

    print(exibicao_times(jogos))

    # TODO: solução da pergunta 1


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

        jogos.append(Jogo(anfitriao, gol_anfitriao,
                     visitante, gol_visitante))
    return jogos


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


def desempate(estatis: list[Time]) -> list[Time]:
    '''
    Desempata os times com o mesmo número de pontos, saldo de gols e vitórias.
    Ordena por ordem alfabética do nome do time.
    >>> desempate([Time('Flamengo', 10, 5, 30), Time('Vasco', 10, 5, 30)])
    [Time(nome='Flamengo', vitorias=10, saldo_gols=5, pontos=30), Time(nome='Vasco', vitorias=10, saldo_gols=5, pontos=30)]
    >>> desempate([Time('Sao-Paulo', 12, 6, 36), Time('Palmeiras', 12, 6, 36)])
    [Time(nome='Palmeiras', vitorias=12, saldo_gols=6, pontos=36), Time(nome='Sao-Paulo', vitorias=12, saldo_gols=6, pontos=36)]
    '''
    for i in range(len(estatis)):
        j = i + 1
        while j < len(estatis):
            if (estatis[i].pontos == estatis[j].pontos and
                estatis[i].saldo_gols == estatis[j].saldo_gols and
                    estatis[i].vitorias == estatis[j].vitorias):
                if estatis[i].nome > estatis[j].nome:
                    estatis[i], estatis[j] = estatis[j], estatis[i]
            j += 1
    return estatis


def calcular_estatisticas(jogos: list[str]) -> list[Time]:
    '''
    Calcula as estatísticas de todos os times com base na lista de jogos.
    Retorna uma lista de objetos Time com nome, pontos, vitórias e saldo de gols.
    >>> calcular_estatisticas(["Flamengo 2 Vasco 1", "Palmeiras 3 Sao-Paulo 0"])
    [Time(nome='Flamengo', vitorias=1, saldo_gols=1, pontos=3), Time(nome='Palmeiras', vitorias=1, saldo_gols=3, pontos=3), Time(nome='Sao-Paulo', vitorias=0, saldo_gols=-3, pontos=0), Time(nome='Vasco', vitorias=0, saldo_gols=-1, pontos=0)]
    >>> calcular_estatisticas(["Sao-Paulo 1 Atletico-PR 2", "Flamengo 0 Palmeiras 1"])
    [Time(nome='Sao-Paulo', vitorias=0, saldo_gols=-1, pontos=0), Time(nome='Atletico-PR', vitorias=1, saldo_gols=1, pontos=3), Time(nome='Flamengo', vitorias=0, saldo_gols=-1, pontos=0), Time(nome='Palmeiras', vitorias=1, saldo_gols=1, pontos=3)]

    '''
    times_nomes = lista_de_times(jogos)
    times_estatisticas = []

    for time_nome in times_nomes:
        pontos_total = 0
        vitorias_total = 0
        gols_marcados = 0
        gols_sofridos = 0

    # Analisa cada jogo para calcular estatísticas do time
        for jogo in jogos:
            jogo_info = saldo_gols([jogo])[0]

            if jogo_info.anfitriao == time_nome:
                gols_marcados += jogo_info.gol_anfitriao
                gols_sofridos += jogo_info.gol_visitante

                if jogo_info.gol_anfitriao > jogo_info.gol_visitante:
                    pontos_total += 3
                    vitorias_total += 1
                elif jogo_info.gol_anfitriao == jogo_info.gol_visitante:
                    pontos_total += 1

            elif jogo_info.visitante == time_nome:
                gols_marcados += jogo_info.gol_visitante
                gols_sofridos += jogo_info.gol_anfitriao

                if jogo_info.gol_visitante > jogo_info.gol_anfitriao:
                    pontos_total += 3
                    vitorias_total += 1
                elif jogo_info.gol_visitante == jogo_info.gol_anfitriao:
                    pontos_total += 1

        saldo_gols_time = gols_marcados - gols_sofridos
        times_estatisticas.append(
            Time(time_nome, vitorias_total, saldo_gols_time, pontos_total))

    times_ordenados = ordenar_times(times_estatisticas)
    return desempate(times_ordenados)


def exibicao_times(jogos: list[str]) -> str:
    '''
    recebe uma lista de jogos e retorna uma string formatada com as estatísticas dos times.
    A string deve conter o nome do time, pontos, vitórias e saldo de gols,
    tudo alinhado corretamente.
    >>> exibicao_times(["Flamengo 2 Vasco 1", "Palmeiras 3 Sao-Paulo 0"])
    'Time          J  V  SG\nFlamengo      3  1  1\nVasco        0  0 -1\nPalmeiras    3  1  3\nSao-Paulo   0  0 -3\n'
    >>> exibicao_times(["Sao-Paulo 1 Atletico-PR 2", "Flamengo 0 Palmeiras 1"])
    'Time          J  V  SG\nSao-Paulo    0  0 -1\nAtletico-PR  3  1  1\nFlamengo     0  0 -1\nPalmeiras    3  1  1\n'
    '''
    estatisticas = calcular_estatisticas(jogos)

    maior_nome = 0
    for time in estatisticas:
        if len(time.nome) > maior_nome:
            maior_nome = len(time.nome)

    # Cabeçalho alinhado
    cabecalho = (
        "Time" + " " * (maior_nome - len("Time") + 2) +
        "P" + "  " +
        "V" + "  " +
        "SG\n"
    )

    resultado_str = cabecalho

    for time in estatisticas:
        espacos_nome = " " * (maior_nome - len(time.nome) + 2)
        espacos_pontos = " " * (3 - len(str(time.pontos)))
        espacos_vitorias = " " * (3 - len(str(time.vitorias)))

        linha = (
            time.nome + espacos_nome +
            str(time.pontos) + espacos_pontos +
            str(time.vitorias) + espacos_vitorias +
            str(time.saldo_gols) + "\n"
            if time.saldo_gols >= 0
            else time.nome + espacos_nome +
            str(time.pontos) + espacos_pontos +
            str(time.vitorias) + espacos_vitorias[0: len(espacos_vitorias) - 1] +
            str(time.saldo_gols) + "\n"

        )

        resultado_str += linha

    return resultado_str

    # TODO: solução da pergunta 2

    # TODO: solução da pergunta 3


def le_arquivo(nome: str) -> list[str]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento     
    representa uma linha.

    Por exemplo, se o conteúdo do arquivo for
    Sao-Paulo 1 Atletico-MG 2 
    Flamengo 2 Palmeiras 1 

    a resposta produzida é
    [‘Sao-Paulo 1 Atletico-MG 2’, ‘Flamengo 2 Palmeiras 1’]
    '''
    try:
        with open(nome) as f:
            return f.readlines()

    except IOError as e:
        print(
            f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.')
        sys.exit(1)


if __name__ == '__main__':
    main()
