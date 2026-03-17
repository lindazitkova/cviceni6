import matplotlib.pyplot as plt

def load_signal_from_txt(path: str) -> list[float]:
    values = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                values.append(float(line))
    return values

def signal_min(values: list[float]) -> float:
    return min(values)

def signal_max(values: list[float]) -> float:
    return max(values)

def signal_avg(values: list[float]) -> float:
    return sum(values) / len(values)

def plot_signal(values: list[float]) -> None:
    plt.plot(values)
    plt.title("Signál")
    plt.xlabel("Vzorky")
    plt.ylabel("Hodnota")
    plt.grid(True)
    plt.show()


# ❗ Zkus si dát sem print("Modul byl načten!") a uvidíš, že se vypíše i při importu.

if __name__ == "__main__":
    path = "ekg_signal.txt"
    values = load_signal_from_txt(path)

    print("Minimum:", signal_min(values))
    print("Maximum:", signal_max(values))
    print("Průměr:", signal_avg(values))

    plot_signal(values)
