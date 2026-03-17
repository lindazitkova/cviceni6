import signal_plot_ops as sp

path = "ekg_signal.txt"

values = sp.load_signal_from_txt(path)
print("Průměr signálu:", sp.signal_avg(values))

sp.plot_signal(values)
