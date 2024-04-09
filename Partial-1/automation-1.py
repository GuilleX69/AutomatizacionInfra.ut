#!/bin/python
import argparse
import datetime
import subprocess

class DateTimeHandler:
    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class FibonacciGenerator:
    @staticmethod
    def generate_fibonacci_series(n):
        fib_series = [0, 1]  # Inicializamos la serie de Fibonacci con los primeros dos números
        for _ in range(2, n):
            next_number = fib_series[-1] + fib_series[-2]
            fib_series.append(next_number)
        return fib_series[:n]

class WebsiteChecker:
    @staticmethod
    def check_websites(urls):
        for pag in urls:
            salida = subprocess.check_output(['curl', '-s', '-I', pag]).decode()
            if "200" in salida:
                print(f"{pag} OK")
            else:
                print(f"{pag} FAIL")

class SystemMonitor:
    @staticmethod
    def monitor_system():
        subprocess.call("clear")
        print("Rendimiento CPU:")
        cpu_usage = subprocess.check_output(["top", "-bn1"]).decode()
        print("Uso de CPU:", cpu_usage)

        print("Uso RAM:")
        ram_usage = subprocess.check_output(["free", "-m"]).decode()
        print("Memoria Utilizada:", ram_usage)

        print("Uso almacenamiento:")
        storage_usage = subprocess.check_output(["df", "-h"]).decode()
        print("Almacenamiento utilizado:", storage_usage)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Automation script.')
    parser.add_argument('-d', '--datetime', action='store_true', help='Get current date and time')
    parser.add_argument('-f', '--fibonacci', type=int, metavar='N', help='Generate Fibonacci series with N terms')
    parser.add_argument('-w', '--website-check', nargs='+', metavar='URL', help='Check websites for availability')
    parser.add_argument('-s', '--system-monitor', action='store_true', help='Monitor system performance')
    
    args = parser.parse_args()

    if args.datetime:
        print("La fecha y hora actual es:", DateTimeHandler.get_current_datetime())

    if args.fibonacci:
        fib_series = FibonacciGenerator.generate_fibonacci_series(args.fibonacci)
        print(f"La serie de Fibonacci con {args.fibonacci} términos es: {fib_series}")

    if args.website_check:
        WebsiteChecker.check_websites(args.website_check)

    if args.system_monitor:
        SystemMonitor.monitor_system()