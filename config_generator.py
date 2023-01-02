import argparse

if __name__ == "__main__" : 

    parser = argparse.ArgumentParser()
    parser.add_argument("--cpu-freq", default="800", type=str, help="Specifiy the cpu frequency")
    parser.add_argument("--gpu-freq", default="800", type=str, help="Specifiy the gpu frequency")
    parser.add_argument("--emc-freq", default="800", type=str, help="Specifiy the emc frequency")

    args = parser.parse_args()

    cpu_freq = int(float(args.cpu_freq)*1000000)
    gpu_freq = int(float(args.gpu_freq)*1000000000)
    emc_freq = int(float(args.emc_freq)*1000000000)

    file_path = './nvpmodel.conf'
    with open(file_path, "w") as file:
        file.write("< PARAM TYPE=FILE NAME=CPU_ONLINE >\n")
        file.write("CORE_0 /sys/devices/system/cpu/cpu0/online\n")
        file.write("CORE_1 /sys/devices/system/cpu/cpu1/online\n")
        file.write("CORE_2 /sys/devices/system/cpu/cpu2/online\n")
        file.write("CORE_3 /sys/devices/system/cpu/cpu3/online\n")
        file.write("CORE_4 /sys/devices/system/cpu/cpu4/online\n")
        file.write("CORE_5 /sys/devices/system/cpu/cpu5/online\n")
        file.write("\n")

        file.write("< PARAM TYPE=FILE NAME=GPU_POWER_CONTROL_ENABLE >\n")
        file.write("GPU_PWR_CNTL_EN /sys/devices/gpu.0/power/control\n")
        file.write("\n")

        file.write("< PARAM TYPE=FILE NAME=GPU_POWER_CONTROL_DISABLE >\n")
        file.write("GPU_PWR_CNTL_DIS /sys/devices/gpu.0/power/control\n")
        file.write("\n")

        file.write("< PARAM TYPE=CLOCK NAME=CPU_A57 >\n")
        file.write("FREQ_TABLE /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies\n")
        file.write("MAX_FREQ /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq\n")
        file.write("MIN_FREQ /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq\n")
        file.write("FREQ_TABLE_KNEXT /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies\n")
        file.write("MAX_FREQ_KNEXT /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq\n")
        file.write("MIN_FREQ_KNEXT /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq\n")
        file.write("\n")

        file.write("< PARAM TYPE=CLOCK NAME=CPU_DENVER >\n")
        file.write("FREQ_TABLE /sys/devices/system/cpu/cpu1/cpufreq/scaling_available_frequencies\n")
        file.write("MAX_FREQ /sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq\n")
        file.write("MIN_FREQ /sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq\n")
        file.write("FREQ_TABLE_KNEXT /sys/devices/system/cpu/cpu1/cpufreq/scaling_available_frequencies\n")
        file.write("MAX_FREQ_KNEXT /sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq\n")
        file.write("MIN_FREQ_KNEXT /sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq\n")
        
        file.write("< PARAM TYPE=CLOCK NAME=GPU >\n")
        file.write("FREQ_TABLE /sys/devices/17000000.gp10b/devfreq/17000000.gp10b/available_frequencies\n")
        file.write("MAX_FREQ /sys/devices/17000000.gp10b/devfreq/17000000.gp10b/max_freq\n")
        file.write("MIN_FREQ /sys/devices/17000000.gp10b/devfreq/17000000.gp10b/min_freq\n")
        file.write("FREQ_TABLE_KNEXT /sys/devices/17000000.gp10b/devfreq/devfreq0/available_frequencies\n")
        file.write("MAX_FREQ_KNEXT /sys/devices/17000000.gp10b/devfreq/devfreq0/max_freq\n")
        file.write("MIN_FREQ_KNEXT /sys/devices/17000000.gp10b/devfreq/devfreq0/min_freq\n")
        file.write("\n")

        file.write("< PARAM TYPE=CLOCK NAME=EMC >\n")
        file.write("MAX_FREQ /sys/kernel/nvpmodel_emc_cap/emc_iso_cap\n")
        file.write("MAX_FREQ_KNEXT /sys/kernel/nvpmodel_emc_cap/emc_iso_cap\n")
        file.write("\n")

        file.write("< POWER_MODEL ID=17 NAME=MODE_17 >\n")
        
        file.write("CPU_ONLINE CORE_0 1\n")
        file.write("CPU_ONLINE CORE_1 1\n")
        file.write("CPU_ONLINE CORE_2 1\n")
        file.write("CPU_ONLINE CORE_3 1\n")
        file.write("CPU_ONLINE CORE_4 1\n")
        file.write("CPU_ONLINE CORE_5 1\n")

        file.write("CPU_A57 MIN_FREQ 0\n")
        file.write("CPU_A57 MAX_FREQ "+str(cpu_freq)+"\n")

        file.write("GPU_POWER_CONTROL_ENABLE GPU_PWR_CNTL_EN on\n")

        file.write("GPU MIN_FREQ 0\n")
        file.write("GPU MAX_FREQ "+str(gpu_freq)+"\n")
        file.write("GPU_POWER_CONTROL_DISABLE GPU_PWR_CNTL_DIS auto\n")

        file.write("EMC MAX_FREQ "+str(emc_freq)+"\n")

        file.write("\n")
        file.write("\n")

        file.write("< PM_CONFIG DEFAULT=17 >\n")
        file.write("< FAN_CONFIG DEFAULT=quiet >\n")
        file.write("\n")
        file.write("\n")

