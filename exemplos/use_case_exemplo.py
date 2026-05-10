"""
Exemplo de Caso de Uso - Usando PromptdaJu Agent
"""

from prompt_agent import PromptAgent


def exemplo_1_listar_prompts():
    """Exemplo 1: Listar todos os prompts disponíveis."""
    print("\n" + "="*60)
    print("EXEMPLO 1: Listar Prompts Disponíveis")
    print("="*60)
    
    agent = PromptAgent(prompts_dir="../Prompts")
    
    categorias = agent.list_categories()
    print(f"\n✅ Categorias encontradas: {categorias}")
    
    todos_prompts = agent.list_prompts()
    for cat, prompts in todos_prompts.items():
        print(f"\n📂 {cat}: {len(prompts)} prompts")
        for prompt in prompts:
            print(f"   • {prompt}")


def exemplo_2_carregar_prompt():
    """Exemplo 2: Carregar um prompt específico."""
    print("\n" + "="*60)
    print("EXEMPLO 2: Carregar Prompt Específico")
    print("="*60)
    
    agent = PromptAgent(prompts_dir="../Prompts")
    
    # Carregar prompt de Coding
    prompt_content = agent.get_prompt("Coding", "gerar-funcao-javascript")
    
    if prompt_content:
        print("\n✅ Prompt carregado com sucesso!")
        print("\nExtraindo apenas o texto do prompt...")
        prompt_text = agent.extract_prompt_section(prompt_content)
        print(f"\n{prompt_text}")
    else:
        print("❌ Prompt não encontrado")


def exemplo_3_customizar_prompt():
    """Exemplo 3: Customizar prompt com variáveis."""
    print("\n" + "="*60)
    print("EXEMPLO 3: Customizar Prompt com Variáveis")
    print("="*60)
    
    agent = PromptAgent(prompts_dir="../Prompts")
    
    # Carregar prompt
    prompt = agent.get_prompt("Coding", "gerar-funcao-javascript")
    prompt_text = agent.extract_prompt_section(prompt)
    
    # Preparar variáveis
    variaveis = {
        "descricao da funcionalidade": "calcular o Fibonacci de um número",
        "seu exemplo aqui": "entrada: 10",
        "sua expectativa aqui": "saída: 55"
    }
    
    # Preencher template
    prompt_customizado = agent.fill_template(prompt_text, variaveis)
    
    print("\n✅ Prompt customizado:")
    print("-" * 60)
    print(prompt_customizado)
    print("-" * 60)


def exemplo_4_integrar_com_ia():
    """Exemplo 4: Integrar com API de IA (simulado)."""
    print("\n" + "="*60)
    print("EXEMPLO 4: Integração com IA (Simulado)")
    print("="*60)
    
    agent = PromptAgent(prompts_dir="../Prompts")
    
    # Carregar prompt
    prompt = agent.get_prompt("Writing", "gerar-artigo-tecnico")
    
    if prompt:
        # Customizar
        variaveis = {
            "tópico": "Programação em Python",
            "quantidade de palavras": "500",
            "descreva o público": "Iniciantes em programação",
            "formal/casual/técnico": "técnico com exemplos simples"
        }
        
        prompt_final = agent.fill_template(prompt, variaveis)
        
        print("\n✅ Prompt pronto para enviar à IA:")
        print("-" * 60)
        print(prompt_final[:200] + "...")
        print("-" * 60)
        print("\nEm produção, você enviaria isso para:")
        print("  • OpenAI GPT-4")
        print("  • Anthropic Claude")
        print("  • Google Gemini")
        print("  • Ou outro modelo de sua preferência")


def exemplo_5_workflow_completo():
    """Exemplo 5: Workflow completo."""
    print("\n" + "="*60)
    print("EXEMPLO 5: Workflow Completo - Brainstorming")
    print("="*60)
    
    agent = PromptAgent(prompts_dir="../Prompts")
    
    # Passo 1: Listar categorias
    print("\nPasso 1: Categorias disponíveis")
    categorias = agent.list_categories()
    for cat in categorias:
        print(f"  • {cat}")
    
    # Passo 2: Selecionar categoria
    categoria_selecionada = "General"
    print(f"\nPasso 2: Selecionada categoria '{categoria_selecionada}'")
    
    # Passo 3: Listar prompts da categoria
    print(f"\nPasso 3: Prompts em '{categoria_selecionada}':")
    prompts_cat = agent.list_prompts(categoria_selecionada)[categoria_selecionada]
    for i, prompt in enumerate(prompts_cat, 1):
        print(f"  {i}. {prompt}")
    
    # Passo 4: Selecionar prompt
    prompt_selecionado = prompts_cat[0]
    print(f"\nPasso 4: Selecionado prompt '{prompt_selecionado}'")
    
    # Passo 5: Exibir informações
    print(f"\nPasso 5: Detalhes do prompt:")
    agent.display_prompt_info(categoria_selecionada, prompt_selecionado)


def main():
    """Executa todos os exemplos."""
    print("\n" + "🤖 " * 20)
    print("  EXEMPLOS DE USO - PromptdaJu Agent")
    print("🤖 " * 20)
    
    # Executar exemplos
    exemplo_1_listar_prompts()
    exemplo_2_carregar_prompt()
    exemplo_3_customizar_prompt()
    exemplo_4_integrar_com_ia()
    exemplo_5_workflow_completo()
    
    print("\n" + "="*60)
    print("✅ Todos os exemplos executados com sucesso!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
