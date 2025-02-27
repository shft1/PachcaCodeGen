# 🔧 ***builder***

## 🛠️ Инструменты для генерации библиотеки

### 📋 Порядок действий (работать в папке `builder` при активированном `venv`):

1. **Для запуска MakeFile командой make из VSCode нужно установить через PowerShell или cmd:**

    - winget install GnuWin32.Make.

2. **Создание зависимостей для работы сборки библиотеки:**

    ```bash
        pip install requirements_builder.txt  
    ```

3. **Создание зависимостей для библиотеки:**

    ```bash
        pipenv install requirements.txt  
    ```

4. **В папке проекта pachca_code_gen_team2 в файле .env указать:**
    - PACKAGE_VERSION=<Версия пакета>
    - TWINE_USERNAME=<Имя пользвателя сервиса TestPyPI>
    - TWINE_API_TOKEN=<Токен пользвателя сервиса TestPyPI>

4. **Запуск создания и загрузки библиотеки на серис TestPyPI при помощи команды:**

    ```bash
        make upload
    ```
5. **Установка бибилотеки с сериса TestPyPI:**

    - pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pachca-generator1
    - pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pachca-generator2

## 📂 Структура генератора

_src/builder/_

#### 📜 requirements_builder.txt
- файл, содержащий список пакетов или библиотек, необходимых для работы упаковщика библиотеки.

#### 📜 requirements.txt
- файл, содержащий список пакетов или библиотек, необходимых для работы над библиотек.

#### 📄 Pipfile
- файл, используемый виртуальной средой Pipenv для управления зависимостями библиотек.

#### 🔒 Pipfile.lock
-  файл в формате JSON хранит контрольные суммы пакетов, которые устанавливаются в проект, что даёт гарантию, что развёрнутые на разных машинах окружения будут идентичны друг другу. 

#### 🛠️ Makefile 
- файл с инструкциями для утилиты make, которая нужна для автоматической сборки проекта.

#### 📦 setup_generator1.py, setup_generator2.py
- файл с описанием, каким именно образом будет упакован код для медотов генерации