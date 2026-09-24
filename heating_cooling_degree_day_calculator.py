import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import csv
from typing import List, Dict, Tuple

def parse_temperature_data(text: str) -> List[Tuple[float, float]]:
    """Parse input text into list of (tmin, tmax) tuples."""
    lines = text.strip().splitlines()
    data = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # replace commas with spaces for uniform handling
        parts = line.replace(",", " ").split()
        if len(parts) == 0:
            continue
        if len(parts) == 1:
            raise ValueError(f"Expected two numbers (min,max) per line, got '{line}'")
        try:
            tmin = float(parts[0])
            tmax = float(parts[1])
        except ValueError:
            raise ValueError(f"Invalid numbers in line: '{line}'")
        if tmin > tmax:
            # swap silently, or warn? We'll swap for robustness.
            tmin, tmax = tmax, tmin
        data.append((tmin, tmax))
    if not data:
        raise ValueError("No valid temperature data found.")
    return data

def compute_degree_days(
    data: List[Tuple[float, float]],
    hdd_base: float,
    cdd_base: float,
    method: str,
) -> List[Dict]:
    """Compute daily HDD and CDD for each day."""
    daily = []
    for tmin, tmax in data:
        if method == "Standard (average)":
            tavg = (tmin + tmax) / 2.0
            hdd = max(0.0, hdd_base - tavg)
            cdd = max(0.0, tavg - cdd_base)
        else:  # Sinclair
            # HDD uses max temperature, CDD uses min temperature
            hdd = max(0.0, hdd_base - tmax)
            cdd = max(0.0, tmin - cdd_base)
        daily.append({"tmin": tmin, "tmax": tmax, "hdd": hdd, "cdd": cdd})
    return daily

def create_daily_table(daily: List[Dict]) -> List[Dict]:
    """Return table as list of dicts for Gradio Dataframe."""
    return [
        {"Day": i+1, "Tmin (°C)": d["tmin"], "Tmax (°C)": d["tmax"],
         "HDD": round(d["hdd"], 3), "CDD": round(d["cdd"], 3)}
        for i, d in enumerate(daily)
    ]

def create_daily_plot(daily: List[Dict], hdd_base: float, cdd_base: float) -> plt.Figure:
    """Create a grouped bar chart of daily HDD and CDD."""
    days = np.arange(len(daily))
    hdd_vals = [d["hdd"] for d in daily]
    cdd_vals = [d["cdd"] for d in daily]

    fig, ax = plt.subplots(figsize=(10, 5))
    width = 0.35
    bars1 = ax.bar(days - width/2, hdd_vals, width, label="HDD", color="#1f77b4")
    bars2 = ax.bar(days + width/2, cdd_vals, width, label="CDD", color="#ff7f0e")
    ax.set_xlabel("Day")
    ax.set_ylabel("Degree Days (°C)")
    ax.set_title(f"Daily HDD and CDD (HDD base={hdd_base}°C, CDD base={cdd_base}°C)")
    ax.set_xticks(days)
    ax.legend()
    fig.tight_layout()
    return fig

def generate_csv(daily: List[Dict], total_hdd: float, total_cdd: float) -> str:
    """Generate CSV string with daily results and totals."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Day", "Tmin", "Tmax", "HDD", "CDD"])
    for i, d in enumerate(daily, start=1):
        writer.writerow([i, d["tmin"], d["tmax"], round(d["hdd"], 3), round(d["cdd"], 3)])
    writer.writerow([])
    writer.writerow(["","","Total HDD", round(total_hdd, 3)])
    writer.writerow(["","","Total CDD", round(total_cdd, 3)])
    return output.getvalue()
