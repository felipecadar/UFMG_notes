# Princípios de sistemas distribuídos

Sistema distribuído: Um conjunto de computadores independentes que se comportam como um computador único

**Motivação**:
1. Organizar recursos
2. Aumentar a capacidade de processamento
   1. Escalabilidade
   2. Desempenho
   3. Latência reduzida
   4. Disponibilidade ( o sistema funciona mesmo se algumas partes falharem)

**Objetivos**:
1. Acessibilidade:
   1. Tornar recursos facilmente acessíveis
2. Transparência:
   1. Ocultar o fato que os rescursos estão distribuídos
      1. Acesso: Não preciso me preocupar em como acessar um recurso A ou B
      2. Localização: O usuário n precisa saber onde está a máquino que ele está usando
      3. Concorrência: Disparar um problema em várias máquinas ao mesmo tempo sem o programador se preocupar com isso
      4. Falhas: Continuar funcionando mesmo se algumas partes falharem
3. Abertura:
   1. O sistema deve seguir padrões que permitem que ele trabalhe com outros sistemas que não foram desenvolvidos junto com ele.
4. Escalabilidade:
   1. Sistema cresce com a demanda
      1. Carga (escala em processamento, amarmazenamento, rede)
      2. Localização (escala geograficamente)
      3. Administração ( tenho mais pessoas administrando o sistema)
   2. Técnicas:
      1. Comunicação assíncrona
      2. Particionamento (dividir e distribuír )
      3. Replicação (copia várias instancias que podem ser rodadas em paralelos)

**Exemplo**:
1. DNS: 
   1. Escalável
   2. Distribuídos geograficamente
   3. Administração descentralizada
   4. Altamente interoperável e aberto
   5. Transparência de localização
   6. Resistente a falhas e ataques

