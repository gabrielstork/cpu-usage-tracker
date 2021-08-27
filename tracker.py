import psutil


CPU = [f'CPU{str(n)}' for n in range(1, psutil.cpu_count() + 1)]


def track():
    with open('tracker.csv', 'w') as file:
        file.write(','.join(CPU))

    while True:
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        cpu_usage = [str(usage) for usage in cpu_usage]

        with open('tracker.csv', 'a') as file:
            file.write(f'\n{",".join(cpu_usage)}')


if __name__ == '__main__':
    track()
