---

## 2) gerador-de-senhas  
*Descrição sugerida:* Gerador simples de senhas em Python.

*Arquivo:* gerador_senha.py  
```python
import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if _name_ == "_main_":
    try:
        tamanho = int(input("Digite o tamanho da senha (padrão 12): ") or 12)
    except ValueError:
        tamanho = 12
    print("Senha gerada:", gerar_senha(tamanho))
