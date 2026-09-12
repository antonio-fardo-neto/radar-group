# Garowa.AI

Dois documentos sobre a **Garowa.AI**, a casa de IA do grupo Garowa, escritos a partir do bilhete de doze itens do fundador: um abre o horizonte, o outro monta a estrutura. Usam o mesmo sistema visual e o mesmo gerador do pacote do Radar Urbano.

| Arquivo | Propósito | O que tem |
|---|---|---|
| `01-HORIZONTE.md` | Abrir o leque | Os doze itens do bilhete mapeados em famílias, seis réguas para ler qualquer posição, trinta e seis posições em três anéis de distância (ao alcance agora, em um ou dois anos, a fronteira), as quatro portas que o Radar Urbano abre, as combinações que só o grupo consegue fazer e cinco formas inteiras de empresa |
| `02-ESTRUTURA.md` | Aterrissar | O que precisa existir para qualquer forma operar: empresa, as duas formas de atender o grupo, contratos, seis papéis, organograma em três tamanhos e por forma, montagem e conta dos doze meses, dez peças da máquina, cadências, LGPD e risco, as quatro janelas do primeiro ano, as portas e o painel |

O primeiro não escolhe: abre. O segundo não escolhe: garante que, escolhida qualquer forma, a segunda-feira seguinte tenha empresa, contrato, gente com nome, caixa contado e máquina de pé. Nenhum dos dois julga o bilhete; os dois partem dele.

## Regras de conteúdo

1. Número do Radar Urbano é fechado e vem do pacote (`radar-urbano/`), sem ressalva.
2. Número de mercado (salário, imposto, honorário, comissão) é ordem de grandeza e aparece marcado como hipótese.
3. Sobre o grupo Garowa, o que o bilhete não diz aparece como pergunta, nunca como afirmação.
4. A disciplina da promessa do Radar vale aqui: nunca conversão, receita atribuída ou "novos clientes".

## Como gerar

```bash
python3 src/build.py garowa-ai/01-HORIZONTE.md --aba "Horizonte" \
  --titulo "O Horizonte da Garowa.AI" --marca "Garowa.AI · Radar Group" \
  --out dist/garowa-ai-horizonte.html
python3 src/build.py garowa-ai/02-ESTRUTURA.md --aba "Estrutura" \
  --titulo "A Estrutura Real da Garowa.AI" --marca "Garowa.AI · Radar Group" \
  --out dist/garowa-ai-estrutura.html
```

Acrescente `--out dist/fragmentos/<arquivo>.html --fragment` para a versão publicável como artifact. `--titulo` e `--marca` foram acrescentados ao gerador para que documentos de outra empresa do grupo não saiam assinados como Radar Urbano.
