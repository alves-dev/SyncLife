# Lista de Eventos V2

Aqui listarei todos os eventos possíveis

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


#### Event: `NOTIFICATION.V1`
- **Context**: ` `
- **Created**: `2025-02-10`
- **Triggers**: `ALL`
- **Listeners**: `EventSync`
- **routing_key**: `notification`

```json
[
  {
    "type": "NOTIFICATION.V1",
    "person_id": "igor_alves",
    "datetime": "2025-01-19T06:00",
    "notification": {
      "recipient_type": "PERSON",
      "recipient_id": "igor_alves",
      "level": "MEDIUM",
      "type": "NOTIFICATION",
      "title": "Sleep: Igor",
      "message": "Tempo de sono não atende as regras",
      "id": "6748fdca-0098-41cd-9db1-8b121e59039d",
      "origin": "Body Track",
      "private": false,
      "showBefore": "2025-02-10 16:03"
    },
    "meta_data": {}
  },
  {
    "type": "NOTIFICATION.V1",
    "person_id": "igor_alves",
    "datetime": "2025-02-27T11:00",
    "notification": {
      "recipient_type": "PERSON",
      "recipient_id": "igor_alves",
      "level": "MEDIUM",
      "type": "QUESTION_3",
      "title": "Comeu!!!",
      "message": "Já fez o almoço ?",
      "origin": "Body Track",
      "id": "hora_almoco",
      "private": false,
      "option_1": "Sim",
      "option_2": "Não",
      "option_3": "Faz tempo",
      "show_after": "2025-02-27 11:00",
      "show_before": "2025-02-27 14:00"
    },
    "meta_data": {}
  }
]
```
- **recipient_type**: `PERSON` aqui pode vir a ser um dispositivo em especifico
- **recipient_id**: `person_id` para quando `recipient_type` for `PERSON`
- **level**: `LOW`, `MEDIUM`, `HIGH`
- **type**: `DEBUG`, `NOTIFICATION`, `REMINDER`, `QUESTION_2`, `QUESTION_3` isso ajuda em como vai ser desenhado no HA
- **id**: identificador único, usado para deletar uma notificação por exemplo
- **private**: indica se a mensagem deve ser tratada como privada (não anunciar na Alexa por exemplo)
- **show_after**: `Opcional` - datas utilizadas para mostrar ou não a notificação
- **show_before**: `Opcional` - datas utilizadas para mostrar ou não o notificação

-----
- **Updated on**: 2025-02-10