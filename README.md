# Welcome to **Snippy Core**
#### Originally designed as a thin layer over the argparse library, Snippy provides a slightly more *rigid* structure for building command line interfaces.

</br>
</br>
* <a href="https://github.com/WilkinsonK/Snippy/blob/testing/README.md#out-of-the-box">Out of the Box</a>
</br>
* <a href="https://github.com/WilkinsonK/Snippy/blob/testing/README.md#your-first-project">Your First Project</a>
</br>
* <a href="https://github.com/WilkinsonK/Snippy/blob/testing/README.md#command-objects">Command Objects</a>
</br>
</br>

## **Out of the Box**
   Snippy provides two commands to help you get started.

    >>> py -m snippy init [proj_name]
    >>> py -m snippy help [command]
</br>
</br>

### **Init**
<p>
   The init command is available only as a Snippy command and cannot be used as
   a Snippy project command. On initiation, a very brief prompt will ask for
   basic details, then create the project directory structure. This includes a
   settings.py, __main__.py and directory space for your commands/command
   files.
</p>
</br>
</br>

   Typical dir structure will look like this:
   ```
   --my_project
        |
        |--commands
        |     |--__init__.py
        |     |--command01.py
        |     |--command02.py
        |
        |--__main__.py
        |--settings.py
   ```
</br>

### **Help**
<p>
   The help command looks through all loaded commands from the project it is
   called from, then prints out the appropriate information concerning that
   command(s).
   For example, if no argument follows calling 'help', a brief description of
   all of the available commands will be presented to the user. If a specified
   command does follow the help call, then a more detailed explanation of how
   to use that command will be expressed in more depth.
</p>

    >>> python -m snippy help
    | Snippy Core | CLI framework
    | seamlessly build commandline interfaces:
    |
    |   [help] display application help
    |   [add]  add a new command to your project
    |   [init] create a new snippy project
    |
    | use snippy help [command] for more info
</br>

## **Your First Project**
<p>
   Getting started with your first project is quick and easy. To begin, open
   up your terminal to the directory you will be working from, then following
   these instructions:
</p>
</br>

1. <u>Run the command</u> 'init **\[proj_name\]**'
    * proj_name will be the title for your cli application.
    * description being the application's purpose
    * help text will be additional description of how your application\
    is to be used.\

2. <u>Overview your settings</u>. The config is primitive, but comes in handy\
for what it's worth. Make sure the settings are completely to your liking.\
The key thing to pay attention to will be the COMMANDS tuple.\

3. <u>Run the command</u> '**\[proj_name\]** add **\[command\]**'
    * proj_name will be the title of your cli application.
    * description will be the description of your new command
    * the '**add**' command goes through a simple prompt, then creates a\
    blank command template, based on the name provided. 
    * it's recommended to create the command file/directory/etc. yourself,\
    but this command was added for ease of development.

4. <u>Start building</u>. By including the import path of your new\
command in your settings, you're all set! By default, a new command\
object is identified in snippy by a lowercased version of it's class name.
</br>
</br>

## **Command Objects**
<p>
   Command Objects are the bread and butter of Snippy. Rather, this is what
   Snippy derives it's '<i>rigid</i>' structure from. At bare minimum, the
   only required changes to a class that derives from BaseCommand will be the
   'parameters' dictionary within the class, and the 'execute' method
   implementation (If you want your command to do something anyway.)
</p>
</br>

<h3><b>BaseCommand</b></h3>
<p>
   The standard abstract class all command objects directly inherit from.
   When defining a new command object, you will use this class to interact
   with the snippy core application. The aim of this class is to be be
   flexible enough to provide developmental freedom, but rigid enough to
   give first-timers an easier place to start on creating their own project.
</p>
</br>

```python
from snippy.core.commands import BaseCommand


class MyAppCommand(BaseCommand):
    name = 'mycommand'
    description = 'This is my Snippy command!'
    parameters = {
        ('text'): {
            'help': 'the string of text being printed to the console',
            'type': str,
            'nargs': '?',
            'default': 'Hello World!'
        } 
    }

    def execute(self, argv):
        print(argv.text)
```
</br>

```
>>> python -m [proj_name] mycommand "I just sent my application to the ministry of silly walks"
```

* Available Attributes:

    * **name** <str\> modifies what the command identifier will be when\
    trying to execute this command.

    * **description** <str\> effectively the help text specific to the\
    command's purpose.

    * **parameters** <dict\[tuple, dict]> because Snippy is built off\
    of argparse, the format for defining arguments follows its pattern.\
    In other words, the key of the outer dict will be the param name(s)\
    within a tuple, then the values will be a dictionary of kwargs that\
    apply to that param.

    * **is_cached** <bool/> still currently in development/up in the air\
    whether or not it's practical to implement this...
