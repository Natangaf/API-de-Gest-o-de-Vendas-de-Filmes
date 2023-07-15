# API de Gestão de Vendas de Filmes

Este é o repositório da API de gestão de vendas de filmes. O objetivo desta API é proporcionar uma solução para gerenciar usuários, filmes e compras, substituindo processos manuais utilizando papel e planilhas desorganizadas. A API oferecerá recursos de autenticação e controle de acesso para diferentes tipos de usuários.

## Visão Geral do Projeto

Nesta entrega, serão desenvolvidas as seguintes funcionalidades e recursos:

1. Configuração do Projeto:
   - Estruturação do projeto com arquivos essenciais.
   - Configuração do ambiente virtual e dependências.

2. Customização de Usuário:
   - Utilização do `AbstractUser` para personalização do modelo de usuário.

3. Django Admin:
   - Registro dos models no Django Admin para permitir uma interface de administração.

4. Serializers Convencionais:
   - Implementação de serializers para a manipulação dos dados.

5. Validação Customizada:
   - Definição de regras de validação personalizadas para garantir a integridade dos dados.

6. Sobrescrita de Métodos de Serializers:
   - Personalização de métodos nos serializers para atender requisitos específicos.

7. Proteção de Rotas com JWT:
   - Implementação de autenticação JWT para proteger as rotas sensíveis da API.

8. Permissões Customizadas do Django Rest Framework:
   - Definição de permissões de acesso customizadas para diferentes tipos de usuário.

9. Tabela Pivô Customizada:
   - Criação de tabela pivô personalizada para facilitar o gerenciamento de relacionamentos complexos.

10. Campos de Escolha para Atributos de Model:
    - Utilização de campos de escolha para garantir consistência nos atributos do modelo.

11. Paginação com APIView:
    - Implementação de paginação nos resultados da API usando APIView.

