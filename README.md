# Aiogram Template

This template is recommended to use in your Telegram bots written on <a href='https://github.com/aiogram/aiogram'>AIOgram</a>.


## About the template

**Structure:**

```
tgbot_template/
├── run.py
├── loader.py
├── config.py
├── bot_app.py
├── tgbot/
│   ├── __init__.py
│   ├── database/
│   ├── states/
│   ├── services/
│   ├── keyboards/
│   ├── misc/
│   ├── utils/
│   ├── filters/
│   ├── handlers/
│   └── middlewares/
```

- The `tgbot` package is the root package for the bot, and it contains sub-packages for **filters**, **handlers**, **middlewares** and another.

- The `filters` package contains classes that define **custom filters** for the bot's message handlers.

- The `handlers` package contains classes that define the bot's **message handlers**, which specify the actions to take
  in response to incoming messages.

- The `middlewares` package contains classes that define **custom middlewares** for the bot's dispatcher, which can be
  used to perform additional processing on incoming messages.

## Detailed description

The `run.py` script is the entry point for the template Telegram bot.

### `tgbot/bot_app.py`

It performs the following steps to start and run the bot:

1. Set up logging: The `logging` module is imported and configured to log messages to the console.
2. Load the configuration: The `load_config()` function from the `tgbot.config` module is called to read the configuration
   from the environment.
3. Set up the storage: Depending on the `use_redis` flag in the configuration, either a `MemoryStorage` or a `RedisStorage2`
   instance is created to store the bot's state.
4. Create the bot and the dispatcher: A `Bot` instance is created using the bot token from the configuration, and a
   `Dispatcher` instance is created using the `Bot` instance and the storage.
5. Register middlewares, filters, and handlers: The `register_all_middlewares()` and `register_all_filters()`functions are called to register all the middlewares, filters, and handlers that are used by
   the bot.
6. Start the polling loop: The `start_polling()` method of the Dispatcher instance is called to start the main event loop
   for the bot. This method listens for incoming messages and routes them to the appropriate handler.

### `config.py`

The `config.py` script defines a data structure for storing configuration options for the bot, such as the Telegram bot
token, database credentials, and other parameters.

The config.py script also includes a `load_config` function for loading the configuration from a file using
the `environs` library.

The config.py file defines a `Config` class, which is used to store configuration settings for the bot.

The Config class has three nested classes, `TgBot`, `DataBaseConfig`, and `Miscellaneous`, which are used to store
configuration settings for the Telegram bot, the database, and miscellaneous settings, respectively.

The `load_config` function is used to load the configuration settings from an environment file and create a `Config`
object.

### `tgbot/filters/IsAdminFilter.py`

The `IsAdminFilter.py` file defines an `AdminFilter` class, which is used to filter messages so that only messages from
authorized users **(i.e., users who are listed in the ADMINS configuration setting)** are processed by the bot.

The `AdminFilter` class is a subclass of `BoundFilter` from the **aiogram** library, and it defines a key property that
specifies the name of the filter. The `AdminFilter` class also defines an `__init__` method that takes a `is_admin`
parameter, which specifies whether the user who sent the message is an authorized user.

The `AdminFilter` class also defines a `check` method that checks whether the user who sent the message is an admin
user, and if so, it returns `True`, indicating that the message should be processed by the bot. Otherwise, it returns
`False`, indicating that the message should be ignored by the bot. The `check` method is called by the bot's dispatcher
when a message is received.

### `tgbot/handlers/admin_handlers.py`

The `admin_handlers.py` file defines functions, which is used to register event handlers for messages that are
sent by authorized users (**i.e., users who are listed in the ADMINS configuration setting**).

For example, it might register an event handler that responds to commands that are sent by authorized users, such as
the `/echo` command, which causes the bot to repeat the text of the message back to the user.

### `tgbot/handlers/echo_handlers.py`

The `echo_handlers.py` file defines a functions, which is used to register an event handler for the `/echo`
command.

This event handler is responsible for repeating the text of the message back to the user. The `register_echo` function
takes a `Dispatcher` object as its parameter, and it uses this object to register the `/echo` command handler.

### `tgbot/handlers/user`

The `user_start_handlers.py` file defines a functions, which is used to register event handlers for messages that are
sent by non-authorized users (i.e., users who are not listed in the ADMINS configuration setting).

### `tgbot/middlewares/environment.py`

`environment.py` is a file that contains the `EnvironmentMiddleware` class, which is a middleware used in the Telegram
bot.

A middleware is a piece of code that sits between the incoming request and the handler function. In this case, the
`EnvironmentMiddleware` class allows the bot to access the configuration data that was loaded by the `load_config`
function
in the `config.py` file. This configuration data can then be accessed by other parts of the bot, such as the handlers,
to
customize its behavior.

### `tgbot/keyboards/(inline|reply).py`

The `inline.py` and `reply.py` files define classes that are used to create inline and reply keyboards, respectively.

The `InlineKeyboard` class is a subclass of `InlineKeyboardMarkup` from the **aiogram** library, and it defines a
`__init__` method that takes a `inline_keyboard` parameter, which specifies the buttons that should be included in the
keyboard.

The `ReplyKeyboard` class is a subclass of `ReplyKeyboardMarkup` from the **aiogram** library, and it defines a
`__init__` method that takes a `keyboard` parameter, which specifies the buttons that should be included in the
keyboard.

### `tgbot/misc`

In general, a package called "misc" might be used to store miscellaneous code that doesn't fit into any of the other
packages or modules in a project. This could include utility functions, helper classes, or other types of code that are
used by multiple parts of the project.

### `tgbot/states`

In this case define files, which defines a `StateGroup` class that is used to define
the states that are used by the bot.

### `tgbot/services`

This package can also be named `infrastructure`. It contains the code that is used to interact with external services.

A package called "services" could contain code that defines services that are used by an application. In software
development, a service is a self-contained piece of functionality that performs a specific task or provides a specific
capability. A service is typically defined as a class or a set of functions that implement the desired functionality.

Examples of services that might be included in a services package could include a **database access service, a caching
service, a messaging service**, or any other type of functionality that is used by the application. The exact contents
of
a services package would depend on the specific needs of the application and the services that it requires.

The `services` package can contain a `database.py` file, which defines a `Database` class that is used to connect to the
database and perform database operations.

## docker-compose.yml
The `docker-compose.yml` file defines the services that are used by the application, as well as the networks and volumes
that are needed by the application. The file begins by specifying the version of the Docker Compose file format that is
being used.

The `services` section of the file defines the containers that should be run as part of the application. In this example,
there is only one service, called `bot`, which is based on the `tg_bot-image` Docker image. The `container_name` specifies the
name that should be used for the container, and the `build` section specifies the location of the Dockerfile that should
be used to build the image.

The `working_dir` specifies the working directory that should be used by the container, and the `volumes` section specifies
the files and directories that should be mounted into the container. In this case, the entire project directory is
mounted into the container, which allows the application to access the files on the host machine.

The `command` specifies the command that should be run when the container is started, and the `restart` setting specifies
that the container should be automatically restarted if it exits. 

The `env_file` setting specifies the location of the `.env` file, which contains the configuration settings for the application.

The `networks` section defines the networks that the container should be connected to. In this example, there is only one
network, called `tg_bot`, which is based on the bridge driver. This network allows the containers in the application to
communicate with each other.

## Dockerfile
The `Dockerfile` defines the instructions for building the Docker image that is used by the bot service. The file begins
by specifying the base image that should be used for the image, which in this case is `python:3.11-alpine`. The `ENV`
instruction sets the value of the `BOT_NAME` environment variable, which is used by the `WORKDIR` instruction to specify the
working directory for the container.

The `COPY` instructions are used to copy the `requirements.txt` file and the entire project directory into the image. The
`RUN` instruction is used to install the Python dependencies from the `requirements.txt` file. This allows the application
to run in the container with all the necessary dependencies.
`requirements_safe.txt` file contains a list of libraries used at the time this template was created.