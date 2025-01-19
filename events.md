# Lista de Eventos

Aqui listarei todos os eventos possiveis

### Todos os eventos vão ter os seguintes campos:

__base event:__
```json
{
  "type": "EVENT_TYPE",
  "person_id": "igor_alves",
  "datetime": "2024-01-23T14:40",

  "meta_data":{
    "origin": "application_name",
    "created_at": "2024-01-23T14:45"
  }
}
```
- **meta_data.origin**: Aplicação que lançou o evento
- **meta_data.created_at**: Hora em que o evento foi lançado/criado
--------------------------------------------------------------

## Health

#### Event: `HEALTH.NUTRI_TRACK.LIQUID.V1`
- **Context**: `Health`
- **Created**: `2024-11-23`
- **Triggers**: `Home assistant`
- **Listeners**: `NutriTrack`
- **routing_key**: `health.nutri-track`

```json
{
  "type": "HEALTH.NUTRI_TRACK.LIQUID.V1",
  "person_id": "igor_alves",
  "datetime": "1998-01-31T14:40",
  "liquid": "Água",
  "amount": 200,
  "meta_data": {}
}
```
- **amount**: Inteiro em ml


#### Event: `HEALTH.NUTRI_TRACK.LIQUID_SUMMARY.V1`
- **Context**: `Health`
- **Created**: `2024-11-26`
- **Triggers**: `NutriTrack`
- **Listeners**: `EventSync`
- **routing_key**: `orchestrator.event-sync`

```json
{
  "type": "HEALTH.NUTRI_TRACK.LIQUID_SUMMARY.V1",
  "person_id": "igor_alves",
  "datetime": "1998-01-31T14:40",
  "total_liquid": {
    "healthy": 1200,
    "unhealthy": 300
  },
  "meta_data": {}
}
```
- **total_liquid.healthy**: Inteiro em ml - Total de líquidos saudáveis ingeridos no dia
- **total_liquid.healthy**: Inteiro em ml - Total de líquidos não saudáveis ingeridos no dia


#### Event: `HEALTH.NUTRI_TRACK.LIQUID_ACCEPTABLE.V1`
- **Context**: `Health`
- **Created**: `2024-11-27`
- **Triggers**: `NutriTrack`
- **Listeners**: `EventSync`
- **routing_key**: `orchestrator.event-sync`

```json
{
  "type": "HEALTH.NUTRI_TRACK.LIQUID_ACCEPTABLE.V1",
  "person_id": "system",
  "datetime": "1998-01-31T14:40",
  "accepted_liquids": ["Água", "Suco Natural", "Chá", "Leite"],
  "meta_data": {}
}
```
- **accepted_liquids**: lista de 


#### Event: `HEALTH.NUTRI_TRACK.SOLID.V1`
- **Context**: `Health`
- **Created**: `2024-12-17`
- **Triggers**: `Home assistant`
- **Listeners**: `NutriTrack`
- **routing_key**: `health.nutri-track`

```json
{
  "type": "HEALTH.NUTRI_TRACK.SOLID.V1",
  "person_id": "igor_alves",
  "datetime": "1998-01-31T14:40",
  "meal": "Almoço",
  "food": "Frango",
  "weight": 123,
  "meta_data": {}
}
```
- **food**: alimento
- **weight**: `Opcional` peso em gramas do alimento


#### Event: `HEALTH.BODY_TRACK.SLEEP.V1`
- **Context**: `Health`
- **Created**: `2025-01-19`
- **Triggers**: `Home assistant`
- **Listeners**: `BodyTrack`
- **routing_key**: `health.body-track`

```json
{
  "type": "HEALTH.BODY_TRACK.SLEEP.V1",
  "person_id": "igor_alves",
  "datetime": "2025-01-19T06:00",
  "action": "WAKE_UP",
  "meta_data": {
    "origin": "home",
    "created_at": "2022-01-18T22:30"
  }
}
```
- **action**: `SLEEP` ou `WAKE_UP`

-----
- **Updated on**: 2025-01-19