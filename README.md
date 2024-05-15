# AI News Summarizer and Telegram Bot

## Descripción

AI News Summarizer and Telegram Bot es una herramienta que busca notas sobre Inteligencia Artificial (IA) en la web, las resume y las envía a través de un bot de Telegram. Esta aplicación está diseñada para mantenerte al día con los últimos desarrollos en IA de una manera rápida y eficiente.

## Características
* Búsqueda automatizada: Encuentra notas y artículos sobre IA de diversas fuentes en la web.
* Resúmenes inteligentes: Utiliza técnicas avanzadas de procesamiento de lenguaje natural (NLP) para resumir los contenidos.
* Notificaciones por Telegram: Envía los resúmenes directamente a tu cuenta de Telegram.

### newsBot/

```bash
├── logging/
│   └── 2024-04-23        # .log generado diariamente
├── newsSave/
│   └── 2024-04-23_0      # Carpeta con notas encontradas en la 
│       │                 # primera busqueda del dia
│       ├── mitpage_0     # Primera nota encontrada en MIT
│       └── wiredPage_0   # Primera nota encontrada en wired
│
├── scripts               # Módulos
│   ├── helpFunctions.py  # Genera índices aleatorios para noticias
│   ├── htmlInfo.py       # Extrae y limpia contenido web
│   ├── initFunc.py       # Inicializa objetos de páginas web
│   ├── llmGemini.py      # Depreciated
│   ├── llmOpenIA.py      # Mejora resúmenes de texto automáticamente
│   ├── objWeb.py         # Obtiene enlaces de páginas web
│   ├── resumeFunc.py     # Analiza y resume contenido web
│   ├── saveTxt.py        # Crea carpetas y archivos
│   └── similarityText.py # Verifica la similitud entre textos
│
├── .gitignore            # Archivos y carpetas a ignorar por Git
├── OpenIA.txt            # API KEY de OpenIA
├── README.md             # Documentación del proyecto
├── TelegramKey.txt       # KEY del bot de Telegram
├── main.py               # Archivo principal
└── requirements.txt      # Lista de dependencias del proyecto
```

## Cómo recibir las noticias
1. Abre Telegram y busca el bot llamado News Ferebell. Puedes encontrar el bot en Telegram 📡 [aquí](https://t.me/NewsFerebellBot).
2. Inicia una conversación con el bot y envía el comando **/registro**.
3. Una vez registrado, comenzarás a recibir los resúmenes de notas sobre IA directamente en tu cuenta de Telegram.

## ¡Siguenos en nuestras redes sociales! 🚀

- [YouTube](https://youtube.com/@ferebell-ia202?si=jHk48xPbQZ0k2M-4)
- [Instagram](https://www.instagram.com/ferebell.ia?igsh=em85NGgwY2x4MXNn) 📸
- LinkedIn: [¡Conéctate conmigo en LinkedIn!](www.linkedin.com/in/rafael-ortiz-feregrino-7bab01186) 💼


### Licencia
Este proyecto está licenciado bajo la Licencia MIT.