# bot-discord

![Python](https://img.shields.io/badge/python-3.11+-blue)
![Docker](https://img.shields.io/badge/docker-supported-blue)
![Discord](https://img.shields.io/badge/discord-bot-5865F2)
![License](https://img.shields.io/badge/license-GPLv3-green)

Bot de Discord desarrollado en **Python** que envía un mensaje de bienvenida automático cuando un nuevo usuario entra al servidor.

Este proyecto está diseñado siguiendo **buenas prácticas de ingeniería de software** y es ideal para ejecutarse de forma permanente en servidores, Raspberry Pi o infraestructuras Docker administradas con **Portainer**.

---

# Características

* Mensaje automático de bienvenida a nuevos miembros
* Compatible con servidores pequeños y grandes
* Configuración mediante variables de entorno
* Despliegue sencillo mediante Docker
* Compatible con Raspberry Pi
* Integración directa con Portainer
* Dependencias instaladas con **uv** para mayor velocidad

---

# Arquitectura del proyecto

```
                    ┌───────────────────┐
                    │ Discord Server    │
                    │                   │
                    │ Nuevo usuario     │
                    └─────────┬─────────┘
                              │
                              │ evento
                              ▼
                    ┌───────────────────┐
                    │ Discord Welcome   │
                    │ Bot (Python)      │
                    │ discord.py        │
                    └─────────┬─────────┘
                              │
                              │ mensaje
                              ▼
                    ┌───────────────────┐
                    │ Canal de          │
                    │ bienvenida        │
                    └───────────────────┘
```

---

# Estructura del proyecto

```
bot-discord
│
├── bot
│   ├── main.py
│   └── config.py
│
├── .env.example
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# Tecnologías utilizadas

* Python 3.11+
* discord.py
* Docker
* Docker Compose
* uv (gestor rápido de dependencias Python)

---

# Requisitos

Para desarrollo local:

* Python 3.11
* uv
* Git

Para despliegue en servidor:

* Docker
* Docker Compose
* Portainer (opcional)

---

# Crear el bot en Discord

1. Ir al portal de desarrolladores:

```
https://discord.com/developers/applications
```

2. Crear una nueva aplicación.

3. Ir a la sección **Bot**.

4. Presionar **Add Bot**.

5. Copiar el **Token del bot**.

6. Activar el siguiente intent:

```
SERVER MEMBERS INTENT
```

Este permiso permite detectar cuando un usuario entra al servidor.

---

# Invitar el bot al servidor

En el panel de desarrollador ir a:

```
OAuth2 → URL Generator
```

Seleccionar:

Scopes

```
bot
applications.commands
```

Permisos mínimos:

```
Send Messages
Read Messages
View Channels
```

Abrir la URL generada para invitar el bot.

---

# Instalación local

Clonar el repositorio:

```
git clone https://github.com/KrlitosForever/bot-discord.git
cd bot-discord
```

---

# Configuración

Crear archivo `.env`:

```
cp .env.example .env
```

Editar `.env`:

```
DISCORD_TOKEN=tu_token
GUILD_ID=id_servidor
WELCOME_CHANNEL_ID=id_canal
```

---

# Ejecutar en modo desarrollo

Instalar uv:

MacOS:

```
brew install uv
```

Crear entorno virtual:

```
uv venv --python 3.11
```

Activar entorno:

```
source .venv/bin/activate
```

Instalar dependencias:

```
uv pip install -r requirements.txt
```

Ejecutar bot:

```
python bot/main.py
```

Salida esperada:

```
Bot conectado como NombreBot
```

---

# Ejecutar con Docker

Construir imagen:

```
docker compose build
```

Levantar servicio:

```
docker compose up -d
```

Ver logs:

```
docker compose logs -f
```

Detener servicio:

```
docker compose down
```

---

# Despliegue en Portainer usando GitHub

Este proyecto puede desplegarse directamente desde un repositorio GitHub usando **Stacks en Portainer**.

---

## Paso 1 — Subir el proyecto a GitHub

Ejemplo:

```
https://github.com/usuario/bot-discord.git
```

---

## Paso 2 — Crear Stack

En Portainer:

```
Stacks
→ Add stack
```

Seleccionar:

```
Repository
```

---

## Paso 3 — Configurar repositorio

Name

```
bot-discord
```

Repository URL

```
https://github.com/KrlitosForever/bot-discord.git
```

Compose path

```
docker-compose.yml
```

---

## Paso 4 — Variables de entorno

Agregar:

```
DISCORD_TOKEN=tu_token
GUILD_ID=tu_servidor
WELCOME_CHANNEL_ID=tu_canal
```

---

## Paso 5 — Deploy

Presionar:

```
Deploy the stack
```

Portainer automáticamente:

1. Clona el repositorio
2. Construye la imagen Docker
3. Inicia el contenedor

---

# Verificar funcionamiento

Ir a:

```
Containers
```

Seleccionar:

```
bot-discord
```

Revisar logs.

Salida esperada:

```
Bot conectado como NombreBot
```

---

# Reinicio automático

El contenedor usa la política:

```
restart: unless-stopped
```

Esto significa que el bot se reiniciará automáticamente si:

* el servidor se reinicia
* el contenedor falla

---

# Seguridad

Nunca subir el archivo `.env` al repositorio.

El `.gitignore` ya incluye:

```
.env
```

Solo se debe subir:

```
.env.example
```

---

# Troubleshooting

## Error: audioop module not found

Este error ocurre cuando se usa **Python 3.14**.

Solución:

Usar Python **3.11 o 3.12**.

---

## Bot no envía mensajes

Verificar:

* que el bot tenga permisos de escritura
* que el `WELCOME_CHANNEL_ID` sea correcto
* que `SERVER MEMBERS INTENT` esté habilitado

---

# Licencia

<div align="left">

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**GNU General Public License v3**

</div>
