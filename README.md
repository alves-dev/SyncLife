![logo_horizontal.png](assets%2Flogo_horizontal.png)

# Sobre

A ideia deste projeto é construir um eco sistema de dados e informações referente as minhas atividades diárias; 
utilizando as mais diversas ferramentas e aplicações diferentes. 
Idealmente quero utilizar frameworks e linguagens diferentes; 
então algumas escolhas não fazem sentido do ponto de vista de uma arquitetura ideal, porém o objetivo maior aqui é aprender.

## System designer

Foi definido as seguintes separações:
- **Conexto**: Um contexto tem varios dominios, cada contexto deve delimitar sua área conforme os dados.
- **Dominio**: É uma especificação dentro do contexto, onde deve limitar a algum dado em especifico.

#### Lista:
| Domain                                                                | Context | Description                                                                                            |
|-----------------------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------|
| [RabbitMQ]()                                                          |         | [Eventos](events.md)                                                                                   |
| [NutriTrack](https://github.com/alves-dev/SyncLife-Health-NutriTrack) | Saúde   | Tudo aquilo que eu ingiro; água, comida, suplementos e outros                                          |
| [BodyTrack]()                                                         | Saúde   | Aquilo que eu faço/tem haver com o meu corpo; medidas, atividades fisicas, mapeamento do sono e outros |

-----
- **Updated on**: 2024-11-18 | **Updated by**: Igor Alves
- **Updated on**: 2024-11-08 | **Updated by**: Igor Alves
- **Created on**: 2024-10-29 | **Created by**: Igor Alves
