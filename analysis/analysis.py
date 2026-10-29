import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('dataset/AI_Impact_on_Human_Mental_Growth.csv')

#analisando o dataset

#criando categoria "Not Informed" na coluna AI_Tool_Category

df_new = df.copy()

df_new["AI_Tool_Category"] = (df_new["AI_Tool_Category"].fillna("Not Informed"))

#print(df_new["AI_Tool_Category"].isnull().sum())
#print(df_new["AI_Tool_Category"].value_counts())
#print(df_new.isnull().sum())


plt.figure(figsize=(9, 5))

#Analisando registros de uso semanais

sns.histplot(
    data=df_new,
    x="Weekly_AI_Usage_Hours",
    bins=30,
    kde=True
)

plt.title("Distribuição das horas semanais de uso de IA")
plt.xlabel("Horas semanais")
plt.ylabel("Quantidade de registros")
#plt.show()
plt.close("all")

#Mediana, quartis e valores dos registros de uso semanais
sns.boxplot(
    data=df_new,
    x="Weekly_AI_Usage_Hours"
)

plt.title("Boxplot das horas semanais de uso de IA")
plt.xlabel("Horas semanais")
#plt.show()
plt.close("all")


#confirmando os outliers

Q1 = df_new["Weekly_AI_Usage_Hours"].quantile(0.25)
Q3 = df_new["Weekly_AI_Usage_Hours"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df_new[
    (df_new["Weekly_AI_Usage_Hours"] < limite_inferior) |
    (df_new["Weekly_AI_Usage_Hours"] > limite_superior)
]

print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)
print("Quantidade de outliers:", len(outliers))


#Analisando se a quantidade de horas semanais é relacionado com a dependência da IA

sns.scatterplot(
    data=df_new,
    x="Weekly_AI_Usage_Hours",
    y="AI_Dependency_Score",
    alpha=0.2,
    s=12
)

plt.title("Relação entre horas de uso e dependência de IA")
plt.xlabel("Horas semanais de uso de IA")
plt.ylabel("Pontuação de dependência")
#plt.show()
plt.close("all")


correlacao = df_new[
    "Weekly_AI_Usage_Hours"
].corr(
    df_new["AI_Dependency_Score"],
    method="pearson"
)

print(f"Correlação de Pearson: {correlacao:.4f}")

#Investigando sobre a dependencia e a capacidade de senso crítico

correlacao_senso = df_new["AI_Dependency_Score"].corr(
    df_new["Critical_Thinking_Ability"]
)

print(f"Correlação: {correlacao:.4f}")

#Grafico 
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df_new,
    x="AI_Dependency_Score",
    y="Critical_Thinking_Ability",
    alpha=0.15,
    s=10,
    ax=ax
)

ax.set_title("Dependência de IA × Pensamento crítico")
ax.set_xlabel("Pontuação de dependência de IA")
ax.set_ylabel("Capacidade de pensamento crítico")

plt.tight_layout()
#plt.show()
plt.close("all")

#Analisando o Scenario
df_new["Scenario"].value_counts()

media_por_scenario = df_new.groupby("Scenario")[
    ["AI_Dependency_Score", "Critical_Thinking_Ability"]
].mean().round(2)

print(media_por_scenario)


#correlacao dentro de cada scenario

correlacoes_scenario = df_new.groupby("Scenario").apply(
    lambda grupo: grupo["AI_Dependency_Score"].corr(
        grupo["Critical_Thinking_Ability"]
    ),
    include_groups=False
)

print(correlacoes_scenario)

#Grafico da relação entre dependencia e pensamento crítico, separando por scenario

g = sns.lmplot(
    data=df_new,
    x="AI_Dependency_Score",
    y="Critical_Thinking_Ability",
    col="Scenario",
    col_wrap=2,
    height=4,
    scatter_kws={
        "alpha": 0.08,
        "s": 8
    },
    line_kws={
        "color": "red"
    },
    ci=None
)

g.set_axis_labels(
    "Dependência de IA",
    "Pensamento crítico"
)

g.set_titles("{col_name}")

g.fig.suptitle(
    "Dependência de IA × Pensamento crítico por cenário",
    y=1.03
)

#plt.show()
plt.close("all")


#Identificando como as 3 fases do Outcome Label se distribuem entre os scenarios

tabela = pd.crosstab(
    df_new["Scenario"],
    df_new["Outcome_Label"],
    normalize="index"
)

print((tabela * 100).round(2))


#verificando se outras variáveis também possuem relações deterministicas com o resultado
tabela_scenario = pd.crosstab(
    df_new["Scenario"],
    df_new["Outcome_Label"]
)


print(tabela_scenario )

#Verificando se as classes de Outcome_Label também apresentam diferenças nas pontuações cognitivas

colunas = [
    "AI_Dependency_Score",
    "Human_Creativity_Score",
    "Critical_Thinking_Ability",
    "Mental_Wellbeing_Score",
    "Attention_Span_Minutes"
]

tabela_cognitivos = df_new.groupby("Outcome_Label")[colunas].mean().round(2)

print(tabela_cognitivos)

#Grafico

tabela = pd.crosstab(
    df_new["Scenario"],
    df_new["Outcome_Label"],
    normalize="index"
) * 100

ax = tabela.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 5)
)

plt.title("Distribuição de Outcome_Label por cenário")
plt.xlabel("Cenário")
plt.ylabel("Percentual de registros")
plt.xticks(rotation=0)
plt.legend(
    title="Classificação",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

plt.tight_layout()
#plt.show()
plt.close("all")