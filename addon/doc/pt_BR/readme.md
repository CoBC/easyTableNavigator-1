# Navegação fácil em tabelas #

* Autores: Corentin Bacqué-Cazenave, Joseph Lee
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* Compatibilidade com NVDA: 2019.3 e posterior

Esse plug-in adiciona um comando de camada para usar uma combinação de
teclas simplificada para navegar pelas células da tabela.  Quando os
comandos em camadas estão ativados, você pode executar as seguintes ações:

* Navegue até a célula anterior ou seguinte horizontal ou verticalmente
  usando as teclas de seta
* Navegue até a primeira ou última célula da linha ou coluna usando as
  teclas de controle+seta ou Home, End, PageUp e PageDown
* Leia toda a linha ou coluna sem mover o cursor do sistema usando
  Windows+Seta para esquerda / Windows+Seta para cima
* Ler a linha ou coluna a partir da célula atual usando Windows+Seta para a
  direita / Windows+Seta para baixo

As tabelas atualmente suportadas são:

* Modo de navegação (Internet Explorer, Firefox etc.).
* Microsoft Word.

## Comandos

* Liga e desliga a camada de navegação em tabelas (não-atribuído).

## Mudanças na 2.4

Para este lançamento, muito obrigado a Cyrille Bougot por seu trabalho.

* Navegação de tabela corrigida no MS Word
* Introduzir novos comandos de acordo com as alterações no NVDA 2022.2 e
  2022.4

    * home/end/pgUp/pgDown para ir para o início/fim da linha/coluna
    * control+esquerda/direita/cima/baixo para pular para o início/fim da
      linha/coluna (tecla de atalho alternativa para o mesmo resultado)
    * NVDA+esquerda/cima para ler a linha/coluna inteira a partir da
      primeira célula sem mover a posição atual do cursor
    * NVDA+direita/baixo para dizerTudo em linha/coluna, ou seja, ler as
      células da linha/coluna atual, começando pela célula atual e movendo a
      posição do cursor durante a leitura até a última célula da
      linha/coluna.

* Remanejou algumas teclas para evitar conflitos:

    * NVDA+seta para cima/seta para a esquerda se tornou Windows+seta para
      cima/seta para a esquerda (para ler a coluna/linha inteira)
    * NVDA+seta para baixo/seta para a direita se tornou Windows+seta para
      baixo/seta para a direita (digamos, tudo em coluna/linha)

* Compatibilidade com o NVDA 2023.1

## Mudanças na 2.3

* Agora é possível desativar a camada de navegação da tabela em qualquer
  lugar
* Compatibilidade com o NVDA 2022.1
* Corrigir erro ao recarregar o addon

## Mudanças na 2.2.1

* Correção de um erro em alguns tipos de documentos, incluindo Word e
  Outlook

## Mudanças na 2.2

* Atualizar o estilo da documentação do modelo de complementos
* Primeira versão traduzida

## Mudanças na 2.1.1

* Novo autor no manifest e na documentação

## Mudanças na 2.1

* Compatibilidade com o NVDA 2021.1

## Mudanças na 2.0

* Requer NVDA 2019.3 ou posterior.
* Tornadas traduzíveis várias mensagens do complemento.

## Mudanças na 1.2

* Alterações internas para suportar futuras versões do NVDA.

## Mudanças na 1.1

* Corrigido um problema no qual erros poderiam ser ouvidos ao consultar
  erros ortográficos no Outlook.

## Mudanças na 1.0

*   Lançamento inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev
