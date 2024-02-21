import argparse
import sqlite3

def importCommand(args):
    """Imports a TOML file to generate an SQLite database and sort data into a table. If table is already created
     it will add new rows for any new entries and/or update the data for entries that already exist if new data is provided """
    print(f"import command run {args.pathString}")


def getKey(args):
    """Retrieves a row from the SQLite database and displays in terminal window"""
    print(f"get-key command run {args.keyString}")


# Sets up parser and subcommand parser
parser = argparse.ArgumentParser(prog='CLI-app')
subparser = parser.add_subparsers(help='sub-command help', required=True)

# establish the subcommands, what argument they will take, and what function they will run when called
import_parser = subparser.add_parser('import', help='import command')
import_parser.add_argument('pathString', help='Path to the file that will be imported')
import_parser.set_defaults(func=importCommand)

key_parser = subparser.add_parser('get-key', help='get key command')
key_parser.add_argument('keyString', help='Key that will be searched for in database')
key_parser.set_defaults(func=getKey)


if __name__ == "__main__":
# parse the Command Line for commands and arguments, then pass the arguments read to the appropriate function based on
# the subcommand called
    args = parser.parse_args()
    args.func(args)
