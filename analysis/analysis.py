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
#diretamente ligado ao outcome_label
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

#Grafico distribuicao de outcome_label por scenario

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


#selecionado 5 features:
#Weekly_AI_Usage_Hours, AI_Dependency_Score, Cognitive_Load_Index, Critical_Thinking_Ability, Human_Creativity_Score e Mental_Wellbeing_Score


#Grafico relacao da Cognitive_Load_Index com Dependence_IA

sns.scatterplot(
    data=df_new,
    x="AI_Dependency_Score",
    y="Cognitive_Load_Index",
    alpha=0.3
)

plt.title("AI Dependency vs Cognitive Load")
plt.xlabel("AI Dependency Score")
plt.ylabel("Cognitive Load Index")
#plt.show()
plt.close("all")

#correlacao 
correlacao_cognitive = df_new["AI_Dependency_Score"].corr(
    df_new["Cognitive_Load_Index"]
)
print(correlacao_cognitive)

#carga cognitiva x pensamento critico

sns.scatterplot(
    data=df_new,
    x="Cognitive_Load_Index",
    y="Critical_Thinking_Ability",
    alpha=0.3
)

plt.title("Cognitive Load vs Critical Thinking")
plt.xlabel("Cognitive Load Index")
plt.ylabel("Critical Thinking Ability")
#plt.show()
plt.close("all")

#correlacao

correlacao_thinking = df_new["Cognitive_Load_Index"].corr(
    df_new["Critical_Thinking_Ability"]
    )
print(correlacao_thinking)

#criatividade x pensamento critico


sns.scatterplot(
    data=df_new,
    x="Human_Creativity_Score",
    y="Critical_Thinking_Ability",
    alpha=0.3
)

plt.title("Human Creativity vs Critical Thinking")
plt.xlabel("Human Creativity Score")
plt.ylabel("Critical Thinking Ability")
#plt.show()
plt.close("all")

#correlacao criativadade x pensamento critico
correlacao_criatividade= df_new["Human_Creativity_Score"].corr(
    df_new["Critical_Thinking_Ability"]
)
print(correlacao_criatividade)

# bem estar mental x carga cognitiva

sns.scatterplot(
    data=df_new,
    x="Mental_Wellbeing_Score",
    y="Cognitive_Load_Index",
    alpha= 0.3
)

plt.title("Mental Wellbeing x Cognitive Load")
plt.xlabel("Mental Wellbeing")
plt.ylabel("Cognitive Load")
#plt.show()
plt.close("all")

#correlacao mental x cognitive
correlacao_mental = df_new["Mental_Wellbeing_Score"].corr(
    df_new["Cognitive_Load_Index"]
)
print(correlacao_mental)


#correlacao das 6 features escolhidas
features = [
    "Weekly_AI_Usage_Hours",
    "AI_Dependency_Score",
    "Cognitive_Load_Index",
    "Critical_Thinking_Ability",
    "Human_Creativity_Score",
    "Mental_Wellbeing_Score"
]

corr = df_new[features].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1
)

plt.title("Correlation Matrix - Selected Features")
#plt.show()

plt.close("all")

