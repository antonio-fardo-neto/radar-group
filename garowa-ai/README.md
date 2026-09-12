# GarowAÍ

Dois documentos sobre o posicionamento da **GarowAÍ**, a casa de IA do grupo Garowa, escritos a partir do bilhete de doze itens do fundador. Usam o mesmo sistema visual e o mesmo gerador do pacote do Radar Urbano.

| Arquivo | O que é |
|---|---|
| `01-HORIZONTE.md` | Expansão: trinta e seis posições possíveis em sete famílias, os quatro eixos de decisão, a crítica ao bilhete, onde o Radar Group entra e cinco empresas inteiras possíveis |
| `02-ESTRUTURA.md` | Aterrissagem: empresa e contratos, seis papéis, organograma em três tamanhos, caixa dos doze primeiros meses, dez peças da plataforma, operação, LGPD e risco, plano por portas e painel do fundador |

O primeiro abre o leque; o segundo fecha um recorte (motor, um vertical e uma voz) e monta a estrutura dele. Os capítulos de contrato, máquina, operação e conformidade do segundo valem para qualquer cenário do primeiro.

## Regras de conteúdo

1. Número do Radar Urbano é fechado e vem do pacote (`radar-urbano/`), sem ressalva.
2. Número de mercado (salário, imposto, honorário, comissão) é ordem de grandeza e aparece marcado como hipótese.
3. Sobre o grupo Garowa, o que o bilhete não diz aparece como pergunta, nunca como afirmação.
4. A disciplina da promessa do Radar vale aqui: nunca conversão, receita atribuída ou "novos clientes".

## Como gerar

```bash
python3 src/build.py garowa-ai/01-HORIZONTE.md --aba "Horizonte" \
  --titulo "O Horizonte da GarowAÍ" --marca "GarowAÍ · Radar Group" \
  --out dist/garowa-ai-horizonte.html
python3 src/build.py garowa-ai/02-ESTRUTURA.md --aba "Estrutura" \
  --titulo "A Estrutura Real da GarowAÍ" --marca "GarowAÍ · Radar Group" \
  --out dist/garowa-ai-estrutura.html
```

Acrescente `--out dist/fragmentos/<arquivo>.html --fragment` para a versão publicável como artifact. `--titulo` e `--marca` foram acrescentados ao gerador para que documentos de outra empresa do grupo não saiam assinados como Radar Urbano.
