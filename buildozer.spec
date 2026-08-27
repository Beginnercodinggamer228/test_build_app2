[app]

# Название приложения
title = Test app

# Имя пакета (без пробелов, только латиница)
package.name = testapp

# Домен пакета
package.domain = me.genkasapps.android.test

# Исходный код приложения (где лежит main.py)
source.dir = .

# Расширения файлов для включения в сборку
source.exts = py,png,jpg,kv,atlas

# Версия приложения
version = 0.1

# Зависимости приложения (обязательно укажите python3 и kivy)
requirements = python3,kivy

# Ориентация экрана (portrait, landscape, all)
orientation = portrait

# Поддерживаемые платформы (сейчас только android)
osx.python_version = 3
osx.kivy_version = 1.9.1

# Права доступа (например, интернет)
android.permissions = INTERNET

# Минимальная версия API Android
android.api = 33

# Предупреждение об архитектуре (armeabi-v7a, arm64-v8a)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# Уровень логирования (0 = только ошибки, 2 = максимум информации)
log_level = 2

# Автоматическое принятие лицензий SDK
android.accept_sdk_license = True
