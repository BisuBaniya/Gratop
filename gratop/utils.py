import psutil #type: ignore
import platform
import matplotlib.pyplot as plt #type: ignore
from matplotlib.animation import FuncAnimation #type: ignore
import os

def display_system_info():
    """Display basic system information."""
    print("\n=== System Information ===")
    try:
        print(f"System: {platform.system()}")
        print(f"Node Name: {platform.node()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Machine: {platform.machine()}")
        print(f"Processor: {platform.processor()}")
        print(f"CPU Count: {psutil.cpu_count(logical=True)}")
        print(f"Total Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB")
        print(f"Used Memory: {psutil.virtual_memory().used / (1024**3):.2f} GB")
        print(f"Available Memory: {psutil.virtual_memory().available / (1024**3):.2f} GB")
        print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    except psutil.Error as e:
        print(f"Error fetching system info: {e}")

def plot_cpu_usage():
    """Plot CPU usage in real-time."""
    fig, ax = plt.subplots()
    ax.set_title('CPU Usage Over Time', fontsize=14)
    ax.set_xlabel('Time (seconds)', fontsize=12)
    ax.set_ylabel('CPU Usage (%)', fontsize=12)

    x_data = []
    y_data = []

    def update(frame):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
        except psutil.Error as e:
            print(f"Error fetching CPU usage: {e}")
            return
        x_data.append(frame)
        y_data.append(cpu_usage)

        ax.clear()
        ax.set_title('CPU Usage Over Time', fontsize=14)
        ax.set_xlabel('Time (seconds)', fontsize=12)
        ax.set_ylabel('CPU Usage (%)', fontsize=12)
        ax.plot(x_data, y_data, color='blue', linewidth=2, label='CPU Usage')
        ax.set_ylim(0, 100)
        ax.axhline(100, color='red', linestyle='--', linewidth=1)
        ax.grid(True, linestyle='--', alpha=0.6)

    anim = FuncAnimation(fig, update, interval=1000, cache_frame_data=False)
    plt.show(block=False)
    plt.close(fig)

def plot_memory_usage():
    """Plot memory usage in real-time."""
    fig, ax = plt.subplots()
    ax.set_title('Memory Usage Over Time', fontsize=14)
    ax.set_xlabel('Time (seconds)', fontsize=12)
    ax.set_ylabel('Memory Usage (%)', fontsize=12)

    x_data = []
    y_data = []

    def update(frame):
        try:
            memory_usage = psutil.virtual_memory().percent
        except psutil.Error as e:
            print(f"Error fetching memory usage: {e}")
            return
        x_data.append(frame)
        y_data.append(memory_usage)

        ax.clear()
        ax.set_title('Memory Usage Over Time', fontsize=14)
        ax.set_xlabel('Time (seconds)', fontsize=12)
        ax.set_ylabel('Memory Usage (%)', fontsize=12)
        ax.plot(x_data, y_data, color='green', linewidth=2, label='Memory Usage')
        ax.set_ylim(0, 100)
        ax.axhline(100, color='red', linestyle='--', linewidth=1)
        ax.grid(True, linestyle='--', alpha=0.6)

    FuncAnimation(fig, update, interval=1000)
    plt.show(block=False)
    plt.close(fig)

def kill_zombie_processes():
    """Kill zombie processes."""
    print("\n=== Killing Zombie Processes ===")
    zombie_count = 0
    for proc in psutil.process_iter(attrs=['pid', 'name', 'status']):
        if proc.info['status'] == psutil.STATUS_ZOMBIE:
            try:
                print(f"Killing zombie process: {proc.info['name']} (PID: {proc.info['pid']})")
                os.kill(proc.info['pid'], 9)
                zombie_count += 1
            except psutil.Error as e:
                print(f"Error killing process {proc.info['pid']}: {e}")
    if zombie_count == 0:
        print("No zombie processes found.")
