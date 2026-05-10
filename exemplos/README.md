# Exemplos de Uso - PromptdaJu Agent

Este diretório contém exemplos práticos de como usar os prompts do PromptdaJu como um agente automatizado.

## Estrutura

```
exemplos/
├── README.md                  # Este arquivo
├── prompt_agent.py           # Agent principal para carregar e usar prompts
├── config_example.json       # Configuração de exemplo
└── use_case_exemplo.py       # Exemplo de caso de uso completo
```

## Como Funciona

O **PromptdaJu Agent** carrega prompts de arquivos Markdown e os organiza por categoria, permitindo:

1. **Listar prompts** por categoria
2. **Carregar um prompt** específico
3. **Usar o prompt** com variáveis customizáveis
4. **Integrar com APIs** de IA (OpenAI, Anthropic, etc.)

## Quick Start

```bash
python prompt_agent.py --list                    # Listar todos os prompts
python prompt_agent.py --category Coding         # Listar prompts da categoria Coding
python prompt_agent.py --use gerar-funcao-javascript --context "fibonacci sequence"
```

## Exemplo de Integração

```python
from prompt_agent import PromptAgent

agent = PromptAgent(prompts_dir="../Prompts")

# Carregar um prompt
prompt = agent.get_prompt("Coding", "gerar-funcao-javascript")

# Usar com customização
contexto = {"funcionalidade": "Validar email", "linguagem": "TypeScript"}
prompt_customizado = agent.fill_template(prompt, contexto)

# Enviar para IA
resposta = sua_api_ia(prompt_customizado)
print(resposta)
```

## Categorias Disponíveis

- **Coding**: Prompts para desenvolvimento
- **Writing**: Prompts para escrita
- **General**: Prompts gerais

## Próximos Passos

1. Configure sua API de IA em `config_example.json`
2. Customize os prompts conforme necessário
3. Integre o agent em seus workflows
4. Crie novos prompts em suas categorias

---

**Versão**: 1.0 | **Data**: May 10, 2026
