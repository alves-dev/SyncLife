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

-----
- **Updated on**: 2024-11-23