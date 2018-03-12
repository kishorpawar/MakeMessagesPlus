import os
from importlib import import_module

from django.conf import settings
from django.core.management.commands.makemessages import Command as BaseMakemessages


class Command(BaseMakemessages):
    help = '''This command inherits from the base django makemessages to default
    to not add location lines and not wrap and allow makemessages for a single
    app or list of apps
    use --yes-location to turn location lines back on
    use --yes-wrap to turn line wrap back on
    '''

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

        parser.add_argument('--yes-location', action='store_true', dest='yes_location',
                            default=getattr(settings, 'ADD_LOCATION', False), 
                            help="Do write '#: filename:line' lines.")
        parser.add_argument('--yes-wrap', action='store_true', dest='yes_wrap',
                            default=getattr(settings, 'DO_WRAP', False), 
                            help="Do wrap long messages for 80 chars")
        parser.add_argument('apps', nargs='*', choices=settings.INSTALLED_APPS + [[],])

    def handle(self, *args, **options):
        self.stdout.write("running the MakeMessagesPlus command - see help for details\n")
        options['no_location'] = not options.get('yes_location')
        options['no_wrap'] = not options.get('yes_wrap')

        if len(options['apps']):
            for app in options['apps']:
                # change the working directory to the app directory
                module = import_module(app)
                os.chdir(os.path.dirname(module.__file__))

                # run base makemessages on single app
                self.stdout.write("processing app %s\n" % app)
                super(Command, self).handle(*args, **options)
        else:
            # run base makemessages on full project
            super(Command, self).handle(*args, **options)
