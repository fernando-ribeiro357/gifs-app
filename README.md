## Running the App

```
docker compose up -d --build gifs-app
```

## Building

```
docker build -t fernandoribeiro357/gifs:latest .
```

To perform multi-architecture builds:

```
docker buildx build --push --platform linux/arm/v7,linux/arm64/v8,linux/amd64 --tag fernandoribeiro357/gifs:latest .
```

Projeto copiado de [mikesir87/cats](https://github.com/mikesir87/cats)