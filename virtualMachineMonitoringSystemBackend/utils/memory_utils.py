

def get_memory_usage(domain, interval):
    domain.setMemoryStatsPeriod(interval)
    memory_info = domain.memoryStats()
    free_memory = float(memory_info['unused'])
    total_memory = float(memory_info['available'])
    memory_usage = ((total_memory - free_memory) / total_memory) * 100
    return memory_usage
