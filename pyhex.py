#!/usr/bin/env python3
import click
import hexdump
import sys

@click.command()
@click.argument('file', type=str, default="")
@click.option('-c', 'inline', help='Display canonical Unicode inline', default=False, is_flag=True)
@click.option('-C', 'outside', help='Display canonical Unicode', default=False, is_flag=True)
@click.option('-G', 'color', help='Display hexadecimal as color', default=False, is_flag=True)
@click.version_option(version='0.0.1')
@click.help_option('--help', '-h')

def main(file, inline, outside, color):
    """Print FILE, or if none given STDIN, in hexadecimal."""
    
    if file == "":
        raw = sys.stdin.buffer.read().hex()
    else:
        try:
            with open(file, "rb") as f:
                raw = f.read().hex()
        except FileNotFoundError:
            print(f"pyhex: {file}: No such file or directory")
            exit()

    if outside:
        split = [raw[i:i+2] for i in range(0, len(raw), 2)]
        hexdump.cprint_hex_w_unicode(split)
    else:
        split = [raw[i:i+2] for i in range(0, len(raw), 2)]
        hexdump.cprint_hex_wout_unicode(split)
        
if __name__ == '__main__':
    main()