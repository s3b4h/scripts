import telnetlib
import time
import getpass
import argparse


class PasswordPromptAction(argparse.Action):
    def __call__(self, parser, args, values, option_string):
        if values is None:
            values = getpass.getpass()
        setattr(args, self.dest, values)

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', dest='username',
                    help='Usuario para acesso via Telnet', default=getpass.getuser())

parser.add_argument('-p', '--password', dest='password',
                    action=PasswordPromptAction, nargs='?', type=str, required=True)

parser.add_argument('-f', '--file', dest='file_host', default='hosts.txt',
                    help='Arquivo de hosts, padrao "hosts.txt"')

parser.add_argument('-c', '--commands', dest='command_list', default='comandos.txt', 
                    help='Arquivo com comandos, padrao "comandos.txt"')

args = parser.parse_args()

try:
    with open(args.file_host, 'r') as hosts:

        host = [line.strip() for line in hosts]
        for hostname in host:
            conect = telnetlib.Telnet(hostname)

            conect.read_until(b"username: ", 3)
            conect.write(args.username.encode('ascii') + b"\n")
            conect.read_until(b"password: ", 3)
            time.sleep(1)
            conect.write(args.password.encode('ascii') + b"\n")

            with open(args.command_list) as listadecomandos:
                comandos = [line.strip() for line in listadecomandos]
                for comando in comandos:
                    conect.write((comando + '\r' + '\n').encode('ascii'))
                    conect.write(("\n").encode('ascii'))
                    time.sleep(2)
            conect.write(b" exit\n")

            with open("output.txt", "a") as saida:
                print(conect.read_all().decode('ascii'), file=saida)

except IOError as err:
    print("Erro: {0}".format(err))