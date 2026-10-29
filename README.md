Análise da distribuição das horas semanais de uso de IA

O histograma apresenta uma distribuição aproximadamente unimodal, com maior concentração de registros entre 20 e 30 horas semanais de uso de inteligência artificial.

A média (24,57 horas) e a mediana (24,50 horas) são próximas, indicando que a tendência central não apresenta uma assimetria acentuada.

Observa-se uma redução gradual na frequência de registros com uso semanal mais elevado, especialmente acima de 40 horas.

Como o dataset é sintético, esses resultados representam características dos cenários simulados, não padrões observados na população real.

Análise bivariada: uso semanal de IA e dependência

O gráfico de dispersão apresenta uma tendência positiva entre as horas semanais de uso de inteligência artificial e a pontuação de dependência.

Observa-se que registros com maior frequência de uso tendem a apresentar valores mais elevados de dependência, embora exista dispersão entre os pontos.

Essa associação será quantificada pelo coeficiente de correlação de Pearson, permitindo avaliar a intensidade da relação linear.

Como o dataset é sintético, o padrão identificado representa uma característica dos dados simulados e não permite estabelecer uma relação causal em situações reais.

Identificação de outliers e análise de correlação

Foi aplicado o método da amplitude interquartil (IQR) à variável Weekly_AI_Usage_Hours, identificando um limite inferior de -12,30 horas e um limite superior de 61,30 horas.

Foram encontrados três registros acima do limite superior, correspondendo a aproximadamente 0,0058% do dataset.

Optou-se inicialmente por manter esses registros, pois não foram identificadas evidências de valores inválidos ou erros de preenchimento.

Em seguida, foi analisada a relação entre as horas semanais de uso de IA e a pontuação de dependência, obtendo-se um coeficiente de correlação de Pearson de 0,9094.

O resultado indica uma associação linear positiva muito forte nos dados simulados. Essa associação não demonstra causalidade e pode refletir regras utilizadas na geração do dataset.

Correlação entre horas de uso e dependência de IA

A análise identificou um coeficiente de correlação de Pearson de 0,9094 entre Weekly_AI_Usage_Hours e AI_Dependency_Score.

Esse resultado indica uma associação linear positiva muito forte: nos cenários simulados, maiores quantidades de horas semanais de uso de inteligência artificial tendem a estar associadas a maiores pontuações de dependência.

A relação também foi observada visualmente no gráfico de dispersão.

Entretanto, como os dados são sintéticos, essa associação pode refletir regras utilizadas na geração do dataset e não constitui evidência de causalidade no mundo real.

Relação entre dependência de IA e pensamento crítico

A correlação de Pearson entre AI_Dependency_Score e Critical_Thinking_Ability foi de -0,2379, indicando uma associação linear negativa fraca.

Esse resultado sugere que, nos cenários simulados, pontuações mais elevadas de dependência de IA tendem a estar associadas a pontuações ligeiramente menores de pensamento crítico.

Entretanto, a baixa intensidade da correlação indica que existe considerável variabilidade na capacidade de pensamento crítico que não é explicada por essa associação linear isolada.

Por se tratar de um dataset sintético, o resultado deve ser interpretado como um padrão da simulação, e não como evidência de efeitos reais da IA sobre a cognição humana.

Análise da relação entre dependência de IA e pensamento crítico

O gráfico de dispersão entre AI_Dependency_Score e Critical_Thinking_Ability apresenta uma distribuição bastante dispersa, coerente com a correlação linear negativa fraca de Pearson (r = -0,2379).

Observa-se que registros com pontuações elevadas de dependência podem apresentar diferentes níveis de pensamento crítico.

A distribuição também sugere a possível existência de subgrupos ou relações não lineares, especialmente nos níveis mais elevados de dependência.

Diante disso, será investigado se a variável Scenario está associada a diferenças no comportamento dessas pontuações.

Como o dataset é sintético, os padrões encontrados representam características da simulação e não evidências de efeitos cognitivos reais.


Análise da correlação por cenário

A correlação geral entre dependência de IA e pensamento crítico foi de -0,2379, indicando uma associação linear negativa fraca.

Entretanto, ao separar os registros por cenário, foram identificadas diferenças expressivas:

Mixed: r = -0,0121

Neutral: r = -0,3382

Optimistic: r = +0,8200

Pessimistic: r = -0,7971

Os resultados mostram que a direção e a intensidade da associação variam conforme o cenário simulado.

No cenário otimista, maiores pontuações de dependência estão associadas a maiores pontuações de pensamento crítico. Já no cenário pessimista, ocorre o comportamento inverso.

Essa descoberta demonstra a importância de analisar subgrupos, pois a correlação geral pode ocultar padrões distintos.

Como o dataset é sintético, essas relações podem refletir regras estabelecidas durante a geração dos cenários, não constituindo evidência sobre efeitos reais da inteligência artificial.


Análise dos indicadores cognitivos por classificação

A comparação das médias por Outcome_Label revelou diferenças entre os grupos simulados.

A classe Cognitive Decline Risk apresentou as menores médias de criatividade (52,56), pensamento crítico (53,00), bem-estar mental (52,97) e atenção (34,92 minutos), além da maior pontuação média de dependência de IA (57,54).

A classe Positive Growth apresentou as maiores médias dos quatro indicadores cognitivos analisados, enquanto Stagnant / Moderate apresentou valores intermediários.

Entretanto, a dependência média foi maior em Positive Growth (50,84) do que em Stagnant / Moderate (40,47), indicando que a relação entre dependência e classificação não segue uma ordem simples.

Esses resultados descrevem padrões presentes no dataset sintético. Ainda é necessário investigar como Outcome_Label foi gerado para determinar se os indicadores cognitivos participaram diretamente da definição das classes.