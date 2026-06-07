areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]



def ler_float(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"  [!] Valor mínimo permitido: {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"  [!] Valor máximo permitido: {maximo}")
                continue
            return valor
        except ValueError:
            print("  [!] Digite um número válido.")


def ler_int(mensagem, minimo=1):

    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"  [!] Valor mínimo permitido: {minimo}")
                continue
            return valor
        except ValueError:
            print("  [!] Digite um número inteiro válido.")




def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura muito baixa"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Sem comunicação"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio baixo"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional em níveis críticos"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


#===========================================================================
#
#                              SERS
#
#=========================================================================

def calcular_potencias(tensao, corrente, fator_potencia):

    potencia_aparente = tensao * corrente
    potencia_ativa    = potencia_aparente * fator_potencia
    potencia_reativa  = (potencia_aparente ** 2 - potencia_ativa ** 2) ** 0.5
    return potencia_ativa, potencia_reativa, potencia_aparente



def calcular_rendimento_motor(potencia_util, potencia_ativa):

    if potencia_ativa == 0:
        return 0.0
    return (potencia_util / potencia_ativa) * 100


def calcular_energia_consumida(potencia_ativa_kw, tempo_horas):

    return potencia_ativa_kw * tempo_horas


def analisar_fator_potencia(fp):

    if fp < 0.70:
        return "CRÍTICO", 2, "FP crítico — excesso reativo severo"
    elif fp < 0.92:
        return "ATENÇÃO", 1, "FP abaixo do mínimo (< 0,92) — corrigir reativo"
    else:
        return "NORMAL", 0, "Fator de potência adequado"


def analisar_rendimento(rendimento):
    if rendimento < 60:
        return "CRÍTICO", 2, "Rendimento do motor crítico — perdas excessivas"
    elif rendimento < 80:
        return "ATENÇÃO", 1, "Rendimento abaixo do esperado"
    else:
        return "NORMAL", 0, "Rendimento do motor adequado"




def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(classificacao_ciclo, resultados_ciclo):
    if classificacao_ciclo == "MISSÃO ESTÁVEL":
        return "Manter operação normal e continuar monitoramento."

    recomendacoes = []

    for nome_area, classificacao, _, _ in resultados_ciclo:
        if classificacao == "CRÍTICO":
            if nome_area == "Temperatura interna":
                recomendacoes.append("verificar controle térmico imediatamente!")
            elif nome_area == "Comunicação com a base":
                recomendacoes.append("tentar restabelecer contato com urgência!")
            elif nome_area == "Sistema de energia":
                recomendacoes.append("ativar modo de economia de energia")
            elif nome_area == "Suporte de oxigênio":
                recomendacoes.append("acionar protocolo de suporte à vida agora!")
            elif nome_area == "Estabilidade operacional":
                recomendacoes.append("reduzir operações não essenciais")
            elif nome_area == "Fator de Potência":
                recomendacoes.append("corrigir banco de capacitores — reativo excessivo!")
            elif nome_area == "Rendimento do Motor":
                recomendacoes.append("verificar motor elétrico — perdas térmicas elevadas!")

    if len(recomendacoes) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação!"

    if recomendacoes:
        return "Ações urgentes: " + "; ".join(recomendacoes) + "."

    return "Monitorar sistemas em atenção e preparar plano de ação."




def analisar_tendencia(riscos_por_ciclo):
    risco_inicial = riscos_por_ciclo[0]
    risco_final   = riscos_por_ciclo[-1]

    if risco_final > risco_inicial:
        return "A missão apresentou tendência de piora."
    elif risco_final < risco_inicial:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacao_acumulada_por_area):
    area_mais_afetada = None
    maior_pontuacao   = -1

    for area, pontuacao in pontuacao_acumulada_por_area.items():
        if pontuacao > maior_pontuacao:
            maior_pontuacao   = pontuacao
            area_mais_afetada = area

    return area_mais_afetada


def gerar_relatorio_final(
    riscos_por_ciclo,
    ciclo_mais_critico,
    pontuacao_acumulada_por_area,
    medias_operacionais,
    medias_energeticas,
    quantidade_ciclos
):
    sep = "=" * 60
    print(f"\n{sep}")
    print("           RELATÓRIO FINAL DA MISSÃO")
    print(sep)
    print(f"  Ciclos analisados: {quantidade_ciclos}")

    print("\n  [ MÉDIAS OPERACIONAIS ]")
    print(f"  Temperatura média   : {medias_operacionais[0]:.2f} °C")
    print(f"  Comunicação média   : {medias_operacionais[1]:.2f} %")
    print(f"  Bateria média       : {medias_operacionais[2]:.2f} %")
    print(f"  Oxigênio médio      : {medias_operacionais[3]:.2f} %")
    print(f"  Estabilidade média  : {medias_operacionais[4]:.2f} %")

    print("\n  [ MÉDIAS ENERGÉTICAS ]")
    print(f"  Potência Ativa  (P) : {medias_energeticas['P']:.2f} W")
    print(f"  Potência Reativa(Q) : {medias_energeticas['Q']:.2f} VAr")
    print(f"  Potência Aparente(S): {medias_energeticas['S']:.2f} VA")
    print(f"  Fator de Potência   : {medias_energeticas['FP']:.3f}")
    print(f"  Rendimento do Motor : {medias_energeticas['RND']:.2f} %")
    print(f"  Calor Joule médio   : {medias_energeticas['JOULE']:.2f} J")
    print(f"  Energia consumida   : {medias_energeticas['ENERGIA']:.6f} kWh")

    maior_risco  = max(riscos_por_ciclo)
    risco_medio  = sum(riscos_por_ciclo) / len(riscos_por_ciclo)
    qtd_criticos = sum(1 for r in riscos_por_ciclo if r >= 6)

    print("\n  [ ESTATÍSTICAS DE RISCO ]")
    print(f"  Ciclo mais crítico        : Ciclo {ciclo_mais_critico + 1}")
    print(f"  Maior pontuação de risco  : {maior_risco}")
    print(f"  Risco médio da missão     : {risco_medio:.2f}")
    print(f"  Ciclos com status CRÍTICO : {qtd_criticos}")

    tendencia = analisar_tendencia(riscos_por_ciclo)
    print(f"\n  [ TENDÊNCIA ]")
    print(f"  {tendencia}")

    print("\n  [ PONTUAÇÃO ACUMULADA POR ÁREA ]")
    for area, pontos in pontuacao_acumulada_por_area.items():
        print(f"  {area}: {pontos} ponto(s)")

    area_mais_afetada = identificar_area_mais_afetada(pontuacao_acumulada_por_area)
    print(f"\n  Área mais afetada: {area_mais_afetada}")

    classificacao_final = classificar_ciclo(round(risco_medio))
    print(f"\n  [ CLASSIFICAÇÃO FINAL DA MISSÃO ]")
    print(f"  {classificacao_final}")
    print(f"{sep}\n")




def main():
    sep_grande  = "=" * 60
    sep_pequeno = "-" * 60

    print(sep_grande)
    print("          MISSION CONTROL AI")
    print("    Monitoramento Energético Espacial")
    print(sep_grande)

    quantidade_ciclos = ler_int("Quantos ciclos deseja analisar? ", minimo=1)

    print(sep_grande)

    # Acumuladores
    riscos_por_ciclo             = []
    ciclo_mais_critico           = 0
    maior_risco_registrado       = -1
    pontuacao_acumulada_por_area = {area: 0 for area in areas_monitoradas}
    pontuacao_acumulada_por_area["Fator de Potência"]   = 0
    pontuacao_acumulada_por_area["Rendimento do Motor"] = 0
    totais_operacionais = [0, 0, 0, 0, 0]
    totais_energeticos  = {"P": 0, "Q": 0, "S": 0, "FP": 0,
                           "RND": 0, "JOULE": 0, "ENERGIA": 0}

    for indice_ciclo in range(quantidade_ciclos):

        print(f"\nCICLO {indice_ciclo + 1}")
        print(sep_pequeno)
        print("  [ DADOS OPERACIONAIS ]")

        temperatura  = ler_float("  Temperatura interna (°C)          : ")
        comunicacao  = ler_float("  Comunicação com a base (%)        : ", 0, 100)
        bateria      = ler_float("  Nível de energia / bateria (%)    : ", 0, 100)
        oxigenio     = ler_float("  Nível de oxigênio (%)             : ", 0, 100)
        estabilidade = ler_float("  Estabilidade operacional (%)      : ", 0, 100)

        print("  [ DADOS ELÉTRICOS ]")
        tensao         = ler_float("  Tensão do sistema (V)             : ", 0)
        corrente       = ler_float("  Corrente do sistema (A)           : ", 0)
        fator_potencia = ler_float("  Fator de potência (0.00 a 1.00)  : ", 0, 1)
        resistencia    = ler_float("  Resistência do sistema (Ω)        : ", 0)
        tempo_seg      = ler_float("  Tempo do ciclo (segundos)         : ", 1)
        potencia_util  = ler_float("  Potência útil do motor (W)        : ", 0)

        # --- Cálculos energéticos ---
        P, Q, S     = calcular_potencias(tensao, corrente, fator_potencia)
        rendimento  = calcular_rendimento_motor(potencia_util, P)
        energia_kwh = calcular_energia_consumida(P / 1000, tempo_seg / 3600)

        # Acumular
        totais_operacionais[0] += temperatura
        totais_operacionais[1] += comunicacao
        totais_operacionais[2] += bateria
        totais_operacionais[3] += oxigenio
        totais_operacionais[4] += estabilidade
        totais_energeticos["P"]       += P
        totais_energeticos["Q"]       += Q
        totais_energeticos["S"]       += S
        totais_energeticos["FP"]      += fator_potencia
        totais_energeticos["RND"]     += rendimento
        totais_energeticos["ENERGIA"] += energia_kwh

        # --- Análises ---
        resultado_temp  = ("Temperatura interna",      *analisar_temperatura(temperatura))
        resultado_com   = ("Comunicação com a base",   *analisar_comunicacao(comunicacao))
        resultado_bat   = ("Sistema de energia",       *analisar_bateria(bateria))
        resultado_oxi   = ("Suporte de oxigênio",      *analisar_oxigenio(oxigenio))
        resultado_est   = ("Estabilidade operacional", *analisar_estabilidade(estabilidade))
        resultado_fp    = ("Fator de Potência",        *analisar_fator_potencia(fator_potencia))
        resultado_rnd   = ("Rendimento do Motor",      *analisar_rendimento(rendimento))

        resultados_ciclo = [
            resultado_temp,
            resultado_com,
            resultado_bat,
            resultado_oxi,
            resultado_est,
            resultado_fp,
            resultado_rnd,
        ]

        # --- Exibir resultado do ciclo ---
        print(f"\n  RESULTADO — CICLO {indice_ciclo + 1}")
        print(sep_pequeno)

        unidades = ["°C", "%", "%", "%", "%", "", "%"]
        valores  = [temperatura, comunicacao, bateria, oxigenio,
                    estabilidade, fator_potencia, rendimento]

        pontuacao_ciclo = 0

        for i, (nome_area, classificacao, pontos, mensagem) in enumerate(resultados_ciclo):
            valor   = valores[i]
            unidade = unidades[i]

            if nome_area == "Fator de Potência":
                print(f"  {nome_area}: {valor:.3f} | {classificacao} | {mensagem}")
            else:
                print(f"  {nome_area}: {valor:.1f}{unidade} | {classificacao} | {mensagem}")

            pontuacao_ciclo += pontos
            pontuacao_acumulada_por_area[nome_area] += pontos

        print(f"\n  [ BALANÇO ENERGÉTICO DO CICLO ]")
        print(f"  Potência Ativa  (P) : {P:.2f} W      — P = U × I × cos(φ)")
        print(f"  Potência Reativa(Q) : {Q:.2f} VAr    — Q = √(S² - P²)")
        print(f"  Potência Aparente(S): {S:.2f} VA     — S = U × I")
        print(f"  Rendimento do motor : {rendimento:.2f} %    — η = P_útil / P_ativa")
        print(f"  Energia consumida   : {energia_kwh:.6f} kWh — E = P × Δt")

        classificacao_ciclo = classificar_ciclo(pontuacao_ciclo)
        recomendacao        = gerar_recomendacao(classificacao_ciclo, resultados_ciclo)

        print(f"\n  Pontuação de risco : {pontuacao_ciclo}")
        print(f"  Classificação      : {classificacao_ciclo}")
        print(f"  Recomendação       : {recomendacao}")

        riscos_por_ciclo.append(pontuacao_ciclo)

        if pontuacao_ciclo > maior_risco_registrado:
            maior_risco_registrado = pontuacao_ciclo
            ciclo_mais_critico     = indice_ciclo

    # --- Médias e relatório ---
    medias_operacionais = [t / quantidade_ciclos for t in totais_operacionais]
    medias_energeticas  = {k: v / quantidade_ciclos for k, v in totais_energeticos.items()}

    gerar_relatorio_final(
        riscos_por_ciclo,
        ciclo_mais_critico,
        pontuacao_acumulada_por_area,
        medias_operacionais,
        medias_energeticas,
        quantidade_ciclos
    )


if __name__ == "__main__":
    main()