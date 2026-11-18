# SQL Agent

Responde perguntas sobre os dados da FLIX-API usando a OpenAI para consultar o `db.sqlite3`.

## Como rodar

1. Crie um arquivo `.env` na raiz com a sua chave:

   ```env
   OPENAI_API_KEY=sk-...
   ```

2. Ative a venv e rode o script:

   ```powershell
   venv\Scripts\Activate
   python sql_agent.py
   ```

Para fazer outra pergunta, passe-a entre aspas:

```powershell
python sql_agent.py "Quantos filmes existem por gênero?"
```
