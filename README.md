# Backend de la prueba técnica desarrollador fullstack 4TheWords

Autor: Rubert Gonzalez Perez.

## Instalación del backend

1. Si quieres crear un entorno virtual para instalar las dependencias, puedes hacerlo con el siguiente comando:

```bash
python -m venv venv
```

2. Luego, activa el entorno virtual:

```bash
.\venv\Scripts\activate
```

3. Instala las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
```

4. Crea la base de datos y crea las tablas con el sql proporcionado en el archivo `.sql` que está en la raíz del proyecto.

5. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno para conectar con la base de datos:

```env
DATABASE_URL=mysql://usuario:contraseña@localhost:3306/4thewords_prueba_rubert_gonzalez
```

6. Inicia el servidor con el siguiente comando:

```bash
fastapi dev --port 8080
```

## Consideraciones

- Nombre base de datos: 4thewords_prueba_rubert_gonzalez
- Nombre del backend: 4thewords_backend_rubert_gonzalez
- Nombre del frontend: 4thewords_frontend_rubert_gonzalez