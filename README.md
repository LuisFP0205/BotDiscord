### Estrutura do Projeto

```
discord_bot/
├── cogs/
│   ├── info.py
│   ├── moderation.py
│   ├── utility.py
│   ├── valorant.py
│   └── voice.py
├── config.py
├── bot.py
└── README.md
```

- `bot.py`: O arquivo principal do bot que inicializa o cliente Discord e carrega os cogs.
- `config.py`: Contém configurações como o prefixo do comando e a lista de mapas do Valorant. **É aqui que você deve definir o token do seu bot.**
- `cogs/`: Este diretório contém os módulos (cogs) para cada funcionalidade do bot:
    - `info.py`: Comandos de informação (ex: `!comandos`, `!musica_comandos`, `!help`).
    - `moderation.py`: Comandos de moderação (ex: `!limpar`).
    - `valorant.py`: Comandos relacionados ao Valorant (ex: `!mapa`).
    - `voice.py`: Comandos relacionados a canais de voz (ex: `!time`, `!reunir`).
    - `utility.py`: Comandos de utilidade geral (ex: `!moeda`).

### Configuração

1.  **Token do Bot:**
    Para executar o bot, você precisa definir o token do seu bot Discord.
    Substitua `SEU_TOKEN_AQUI` pelo token real do seu bot.
    ⚠️ Nunca compartilhe o seu token em repositórios públicos!

2.  **Dependências:**
    Certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalá-las usando pip:
    ```bash
    pip install discord.py
    ```

### Como Executar o Bot

1.  Navegue até o diretório `discord_bot` no seu terminal:
    ```bash
    cd discord_bot
    ```
2.  Substitua o token: `DISCORD_BOT_TOKEN`.
3.  Execute o arquivo principal do bot:
    ```bash
    python bot.py
    ```

O bot deverá ficar online e pronto para uso no seu servidor Discord.


