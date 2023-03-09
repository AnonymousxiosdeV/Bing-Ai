import os
import psutil
import tkinter as tk

def get_cpu_temperature():
    """Return the CPU temperature in Fahrenheit."""
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    cpu_temp = float(cpu_temp.replace("temp=", "").replace("'C\n", ""))
    return f"{cpu_temp * 9/5 + 32:.1f} °F"

def get_memory_usage():
    """Return the memory usage as a percentage."""
    memory = psutil.virtual_memory()
    return f"{memory.percent:.1f}%"

def get_disk_usage():
    """Return the disk usage as a percentage."""
    disk = psutil.disk_usage('/')
    return f"{disk.percent:.1f}%"

def get_network_activity():
    """Return the network activity in bytes sent/received per second."""
    net_io_counters = psutil.net_io_counters(pernic=True)
    bytes_sent = sum([net_io_counters[nic].bytes_sent for nic in net_io_counters])
    bytes_recv = sum([net_io_counters[nic].bytes_recv for nic in net_io_counters])
    return f"Sent: {bytes_sent} B/s\nReceived: {bytes_recv} B/s"

class Gauge(tk.Canvas):
    """A simple circular gauge widget."""
    
root = tk.Tk()
root.title("Raspberry Pi System Information")

cpu_temperature_label = tk.Label(root, text=f"CPU Temperature: {get_cpu_temperature()}")
cpu_temperature_label.pack()

memory_usage_label = tk.Label(root,text=f"Memory Usage: {get_memory_usage()}")
memory_usage_label.pack()

disk_usage_label=tk.Label(root,text=f"Disk Usage: {get_disk_usage()}")
disk_usage_label.pack()

network_activity_label=tk.Label(root,text=f"Network Activity:\n{get_network_activity()}")
network_activity_label.pack()

reboot_button=tk.Button(root,text="Reboot",command=lambda:os.system("sudo reboot"))
reboot_button.pack()

close_button=tk.Button(root,text="Close",command=root.destroy)
close_button.pack()

def update_labels():
  cpu_temperature_label["text"] = f"CPU Temperature: {get_cpu_temperature()}"
  memory_usage_label["text"] = f"Memory Usage: {get_memory_usage()}"
  disk_usage_label["text"]=f"Disk Usage: {get_disk_usage()}"
  network_activity_label["text"]=f"Network Activity:\n{get_network_activity()}"

root.after(1000, update_labels)

root.mainloop()