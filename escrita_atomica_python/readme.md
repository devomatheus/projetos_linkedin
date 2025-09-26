# Escrita Atômica de Arquivos em Python

Este projeto demonstra uma função para escrita atômica de arquivos, implementada no arquivo `main.py`.

## O que é escrita atômica?
A escrita atômica garante que um arquivo seja atualizado de forma segura, evitando corrupção de dados, arquivos incompletos ou inconsistentes, especialmente em casos de falha de energia, travamento do sistema ou concorrência de processos.

## Benefícios
- **Segurança**: Evita que arquivos fiquem corrompidos durante a escrita.
- **Consistência**: Garante que o arquivo final sempre estará completo.
- **Concorrência**: Reduz problemas em ambientes onde múltiplos processos podem acessar o mesmo arquivo.

## Como funciona
A função cria um arquivo temporário, escreve os dados nele e só depois substitui o arquivo original. Isso evita que o arquivo fique em estado intermediário caso ocorra algum erro.

## Palavras-chave
`escrita atômica`, `Python`, `segurança`, `concorrência`, `arquivo`, `tempfile`, `pathlib`

## Linguagem e versão
- **Linguagem:** Python
- **Versão recomendada:** 3.8+

## Arquivo principal
- `main.py`: Implementação da função de escrita atômica.

---

Sinta-se à vontade para usar, adaptar e compartilhar este projeto!
