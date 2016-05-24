import platform
import psutil

psutil.disk_partitions()

psutil.disk_usage('/')

psutil.disk_io_counters(perdisk=False)


platform.machine()
platform.version()
platform.platform()
platform.uname()
platform.system()
platform.processor()
