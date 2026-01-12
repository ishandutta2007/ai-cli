# ai-cli

aim/
├── aim/
│   ├── __init__.py
│   ├── cli.py               # Main Click CLI group + core commands
│   ├── models.py            # Model registration, base classes, get_model()
│   ├── plugins.py           # Plugin discovery + registration logic
│   ├── keys.py              # API key management (like llm keys)
│   ├── utils.py             # Shared helpers (logging, etc.)
│   └── providers/           # (optional) built-in dummy/example providers
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_basic.py
├── .gitignore
├── pyproject.toml           # Build config + entry points + deps
├── README.md
├── LICENSE                  # MIT or Apache-2.0
└── setup.cfg                # Optional, if you prefer over pyproject only