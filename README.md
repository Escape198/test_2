- **Кастомная аутентификация:** 
  - Приложение использует кастомный менеджер безопасности (`CustomAuthSecurityManager`), который позволяет доступ с использованием стандартных учетных данных `admin/admin`.

- **OAuth через GitHub:**
  - OAuth настроен на работу с GitHub, позволяя пользователям входить в систему, используя свои учетные записи GitHub.

## Начало работы

### Предварительные требования

- Docker
- Docker Compose

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Escape198/test.git
   cd yourproject


2. Создайте файл `.env` в корневой директории и задайте следующие переменные окружения:

   ```dotenv
   SECRET_KEY=ваш_секретный_ключ
   GITHUB_CLIENT_ID=ваш_github_client_id
   GITHUB_CLIENT_SECRET=ваш_github_client_secret
   VENDOR_GITHUB_API=https://api.github.com
   VENDOR_GITHUB_AUTH=https://github.com/login/oauth

3. Соберите и запустите Docker-контейнеры:
   ```bash
   docker-compose up --build


## Использование

- 🌐 **Откройте приложение** по адресу: [http://localhost:5000](http://localhost:5000).
- 🔐 **Войдите в систему**, используя один из следующих способов:
  - **GitHub OAuth**: Авторизация через GitHub.
  - **Стандартные учетные данные**: Введите `admin/admin` для входа как администратор.
- 🔧 **Конфигурация AUTH_TYPE**:
  - `AUTH_OAUTH`: Включает авторизацию через GitHub.
  - `AUTH_DB`: Используется для входа администратора.