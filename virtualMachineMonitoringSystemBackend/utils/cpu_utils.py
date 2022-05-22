import time


def get_cpu_usage(domain, interval):
    cpu_number = domain.info()[3]
    t1 = time.time()
    cpu_stats1 = domain.getCPUStats(total=True)
    time.sleep(interval)
    t2 = time.time()
    cpu_stats2 = domain.getCPUStats(total=True)
    usage = (cpu_stats2[0]['cpu_time'] - cpu_stats1[0]['cpu_time']) * 100 / ((t2 - t1) * cpu_number * 1e9)

    return usage
