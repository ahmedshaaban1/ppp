import click

def fibonacci(N):
    if N < 2:
        return N

    return fibonacci(N - 2) + fibonacci(N - 1)

@click.command()
@click.option("-l", default=False, is_flag=True)
@click.argument('n', type=click.INT)
def main(n, l):
    if l:
        for i in range(n):
            print("The fibonacci number for '{}' is {}".format(
                i, fibonacci(i)), flush=True)

    print("The fibonacci number for '{}' is {}".format(
        n, fibonacci(n)))

if __name__ == "__main__":
    main()
