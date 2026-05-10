"""
PromptdaJu Agent - Agente para carregar e gerenciar prompts de IA
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional


class PromptAgent:
    """Agente para carregar, organizar e usar prompts de IA."""
    
    def __init__(self, prompts_dir: str = "../Prompts"):
        """
        Inicializa o agente.
        
        Args:
            prompts_dir: Caminho para o diretório de prompts
        """
        self.prompts_dir = Path(prompts_dir)
        self.prompts = self._load_prompts()
    
    def _load_prompts(self) -> Dict[str, Dict[str, str]]:
        """Carrega todos os prompts organizados por categoria."""
        prompts = {}
        
        if not self.prompts_dir.exists():
            print(f"⚠️ Diretório de prompts não encontrado: {self.prompts_dir}")
            return prompts
        
        for category_path in self.prompts_dir.iterdir():
            if category_path.is_dir():
                category_name = category_path.name
                prompts[category_name] = {}
                
                for prompt_file in category_path.glob("*.md"):
                    prompt_name = prompt_file.stem
                    with open(prompt_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    prompts[category_name][prompt_name] = content
        
        return prompts
    
    def list_categories(self) -> List[str]:
        """Lista todas as categorias disponíveis."""
        return sorted(self.prompts.keys())
    
    def list_prompts(self, category: Optional[str] = None) -> Dict:
        """
        Lista prompts disponíveis.
        
        Args:
            category: Se fornecido, lista apenas prompts dessa categoria
            
        Returns:
            Dicionário com categorias e seus prompts
        """
        if category:
            return {category: list(self.prompts.get(category, {}).keys())}
        
        result = {}
        for cat, prompts_dict in self.prompts.items():
            result[cat] = list(prompts_dict.keys())
        return result
    
    def get_prompt(self, category: str, prompt_name: str) -> Optional[str]:
        """
        Obtém um prompt específico.
        
        Args:
            category: Categoria do prompt
            prompt_name: Nome do prompt
            
        Returns:
            Conteúdo do prompt ou Nenhum se não encontrado
        """
        return self.prompts.get(category, {}).get(prompt_name)
    
    def extract_prompt_section(self, content: str) -> str:
        """
        Extrai apenas a seção "Prompt" de um arquivo Markdown.
        
        Args:
            content: Conteúdo completo do arquivo
            
        Returns:
            Apenas o texto do prompt
        """
        # Procura pela seção ## Prompt
        match = re.search(r'## Prompt\n```\n(.*?)\n```', content, re.DOTALL)
        if match:
            return match.group(1)
        return content
    
    def fill_template(self, prompt: str, variables: Dict[str, str]) -> str:
        """
        Preenche variáveis no template do prompt.
        
        Args:
            prompt: Texto do prompt com placeholders
            variables: Dicionário com chave=valor para substituição
            
        Returns:
            Prompt preenchido
        """
        resultado = prompt
        for chave, valor in variables.items():
            placeholder = f"[{chave}]"
            resultado = resultado.replace(placeholder, valor)
        return resultado
    
    def display_prompt_info(self, category: str, prompt_name: str) -> None:
        """Exibe informações completas sobre um prompt."""
        prompt = self.get_prompt(category, prompt_name)
        if not prompt:
            print(f"❌ Prompt não encontrado: {category}/{prompt_name}")
            return
        
        print(f"\n📝 Prompt: {prompt_name}")
        print(f"📂 Categoria: {category}")
        print("─" * 60)
        print(prompt)
        print("─" * 60)
    
    def get_prompt_text_only(self, category: str, prompt_name: str) -> Optional[str]:
        """Obtém apenas o texto do prompt, sem metadados."""
        conteudo = self.get_prompt(category, prompt_name)
        if not conteudo:
            return None
        return self.extract_prompt_section(conteudo)


def main():
    """Função principal para demonstração."""
    import sys
    
    # Inicializa o agente
    agent = PromptAgent(prompts_dir="../Prompts")
    
    # Se não houver argumentos, mostra menu
    if len(sys.argv) == 1:
        print("\n🤖 PromptdaJu Agent")
        print("=" * 60)
        print("\nCategorias disponíveis:")
        for cat in agent.list_categories():
            prompts = agent.list_prompts(cat)[cat]
            print(f"\n  📂 {cat}")
            for prompt in prompts:
                print(f"     • {prompt}")
        
        print("\n\nUso:")
        print("  python prompt_agent.py --listar")
        print("  python prompt_agent.py --categoria Coding")
        print("  python prompt_agent.py --exibir Coding gerar-funcao-javascript")
        return
    
    # Processa argumentos
    if sys.argv[1] == "--listar":
        todos_prompts = agent.list_prompts()
        for cat, prompts in todos_prompts.items():
            print(f"\n{cat}:")
            for prompt in prompts:
                print(f"  • {prompt}")
    
    elif sys.argv[1] == "--categoria" and len(sys.argv) > 2:
        cat = sys.argv[2]
        prompts = agent.list_prompts(cat)
        if cat in prompts:
            print(f"\nPrompts em {cat}:")
            for prompt in prompts[cat]:
                print(f"  • {prompt}")
        else:
            print(f"❌ Categoria não encontrada: {cat}")
    
    elif sys.argv[1] == "--exibir" and len(sys.argv) > 3:
        cat = sys.argv[2]
        nome_prompt = sys.argv[3]
        agent.display_prompt_info(cat, nome_prompt)
    
    else:
        print("❌ Comando não reconhecido")


if __name__ == "__main__":
    main()
