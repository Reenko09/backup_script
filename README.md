Script simples pra selecionar arquivos pra backup

1 - Verificar destino de backup:
  * DEFAULT: Cria uma pasta de backup na mesma pasta onde esta cada arquivo
  * CUSTOM: O script usa o path em "custom_path" para criar uma pasta de backups, e salvar todos os backups la
  * PARENT: Salva os backups em uma pasta junto do script

2 - Adicionar os paths de cada arquivo a ser salvo na lista backup_list[]
* Ex:
* backup_list[
   "C:\Users\lfree\OneDrive\Desktop\Projetos\testes de script\arquivo 1.txt",
   "C:\Users\lfree\OneDrive\Desktop\Projetos\testes de script\arquivo 2.txt",
   "C:\Users\lfree\OneDrive\Desktop\Projetos\testes de script\arquivo 3.txt"
  ]

* Contatar o Luigi em caso de sugestões ou feedback
