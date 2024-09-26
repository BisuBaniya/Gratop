# gratop.py

from utils import display_system_info, plot_cpu_usage, plot_memory_usage, kill_zombie_processes

class SystemMonitor:
    def main_menu(self):
        """Main menu for user interaction."""
        while True:
            print("\n=== System Monitor ===")
            print("1. System Info")
            print("2. CPU Usage")
            print("3. Memory Usage")
            print("4. Both (CPU and Memory Usage)")
            print("5. Kill Zombie Processes")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                display_system_info()
            elif choice == '2':
                plot_cpu_usage()
            elif choice == '3':
                plot_memory_usage()
            elif choice == '4':
                plot_cpu_usage()
                plot_memory_usage()
            elif choice == '5':
                kill_zombie_processes()
            elif choice == '6':
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.main_menu()
