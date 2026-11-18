# FLIX-API

API REST de catálogo de filmes (gêneros, atores, filmes e avaliações) com autenticação JWT. O script `sql_agent.py` responde perguntas sobre o banco em português.

## Como rodar

```powershell
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API em [http://127.0.0.1:8000/](http://127.0.0.1:8000/) e admin em [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

Para carregar os atores de exemplo: `python manage.py import_actors actors.csv`.

As rotas ficam em `/api/v1/` (`genres`, `actors`, `movies`, `reviews` e `movies/stats`). O token sai de `POST /api/v1/authentication/token/` com `username` e `password`, e vai no header `Authorization: Bearer <access>`. O usuário precisa da permissão Django do recurso.

## Agente SQL

Crie um `.env` na raiz com `OPENAI_API_KEY=sk-...` e, com a venv ativa:

```powershell
python sql_agent.py
python sql_agent.py "Quantos filmes existem por gênero?"
```
