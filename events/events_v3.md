# Eventos V3

### Esta é uma nova definição de eventos, baseado em melhores praticas e evolução dos eventos anteriores 

### Esta nova definição segue a especificação de [CloudEvents](https://github.com/cloudevents/spec/tree/main)

#### Exemplo de um evento:
```json
{
  "specversion": "1.0",
  "type": "health.nutrition.liquid_summary.calculated.v1",
  "source": "/services/nutri-track",
  "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "time": "2025-04-19T14:40:00Z",
  "datacontenttype": "application/json",
  "dataschema": "https://github.com/alves-dev/SyncLife/tree/main/evens/schema/health/schema_v1.json",
  "data": {
    "person_id": "igor_alves", 
    "total_liquid": {
      "healthy": 1200,
      "unhealthy": 300
    }
  },
  "extensions": {
    "correlation_id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
    "causation_id": "original-event-uuid",
    "origin": "NutriTrack"
  }
}
```
- `specversion`: Fixo `1.0` enquanto usar o CloudEvents 1.x
- `type`: Nome do evento no formato `<domain>.<sub-domain>.<event>.<version>`
  - `event` pode ser divididos em duas partes para mais controle, também separados por `.`
  - `version` deve esta no formado `v` mais o número, por exemplo: `v1`, `v2`
- `source`: Uma reférencia da origem do evento no formato de `URI`
- `id`: UUID único para identificação do evento
- `time`: Um Timestamp do momento que o evento foi criado
- `datacontenttype`: Neste caso fixo `application/json`
- `dataschema`: Link para o schema do evento, o schema utilizado é [Draft 2020-12](https://json-schema.org/draft/2020-12)
- `data`: Contém os dados do domínio em se
- `extensions`: Metadados adicionais


### Use esta [ferramenta](https://www.jsonschemavalidator.net/) para validar o json schema


-----
- **Updated**: xxxx-xx-xx
- **Created**: 2025-04-22
