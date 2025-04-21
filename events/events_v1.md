# Lista de Eventos V1

## Primeira definição de eventos

### Algumas coisas se perderam no caminho, outras não foram implementados

# Events list

Aqui listarei todos os eventos possiveis

### Todos os eventos vao ter os seguintes campos:

```json
{
  "type": "EVENT_TYPE",
  "person_id": "f81ac9d2-f365-4254-a374-6vd2bb337e16",
  "datetime": "2024-01-23T14:45-03:00"
}
```
--------------------------------------------------------------


<a id="person_tracking"></a>
#### PERSON_TRACKING: *routing_key* -> _person_tracking_
```json
[
  {
    "type": "PERSON_TRACKING",
    "person_id": "f82ac9d8-f165-4254-a374-1ad2bb317e16",
    "datetime": "2024-01-23T14:45-03:00",
    "action": "CAME_IN",
    "local": "ACADEMY",
    "origin": "Home assistant"
  },
  {
    "type": "PERSON_TRACKING",
    "person_id": "f82ac9d8-f165-4254-a374-1ad2bb317e16",
    "datetime": "2024-01-23T14:45-03:00",
    "action": "WENT_OUT",
    "local": "ACADEMY",
    "origin": "Home assistant"
  },
  {
    "type": "PERSON_TRACKING",
    "person_id": "f82ac9d8-f165-4254-a374-1ad2bb317e16",
    "datetime": "2024-01-23T14:45-03:00",
    "action": "REMAINED",
    "local": "ACADEMY",
    "minutes": 45,
    "origin": "Home assistant"
  }
]
```
- __action__: [CAME_IN, WENT_OUT, REMAINED]
--------------------------------------------------------------


<a id="exercise"></a>
#### EXERCISE: *routing_key* -> _exercises_
```json
{
  "type": "EXERCISE",
  "person_id": "f81ac9d8-f165-4254-a374-1ad2bb337e16",
  "datetime": "2024-01-23T14:45-03:00",
  "type_exercise": "RACE",
  "minutes": 45.55,
  "detail": {
    "origin": "Strava",
    "external_id": "2561523"
  }
}
```
--------------------------------------------------------------


<a id="medidas"></a>
#### MEDIDAS CORPORAIS: *routing_key* -> _body_measurements_
```json
{
  "type": "BODY_MEASUREMENTS",
  "person_id": "f81ac9d8-f165-4254-a374-1ad2bb337e16",
  "datetime": "2024-01-23T14:45-03:00",
  "measure": "peso",
  "value": 67.5
}
```
--------------------------------------------------------------


<a id="alimentacao"></a>
#### ALIMENTAÇÃO: *routing_key* -> _food_
```json
{
  "type": "FOOD",
  "person_id": "f81ac9d8-f165-4254-a374-1ad2bb337e16",
  "datetime": "2024-01-23T14:45-03:00",
  "food": "arroz",
  "weight": 200
}
```
- __weight__: em gramas

#### ALIMENTAÇÃO: *routing_key* -> _food_
```json
{
  "type": "LIQUID_FOOD",
  "person_id": "f81ac9d8-f165-4254-a374-1ad2bb337e16",
  "datetime": "2024-01-23T14:45-03:00",
  "liquid": "water",
  "amount": 200
}
```
- __amount__: Inteiro em ml
--------------------------------------------------------------
