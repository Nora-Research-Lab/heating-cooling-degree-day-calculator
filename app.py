import gradio as gr
from heating_cooling_degree_day_calculator import (
    parse_temperature_data,
    compute_degree_days,
    create_daily_table,
    create_daily_plot,
    generate_csv,
)
import tempfile
import os

def compute_and_display(
    temperature_text,
    hdd_base,
    cdd_base,
    method,
):
    try:
        data = parse_temperature_data(temperature_text)
    except ValueError as e:
        return f"Error parsing input: {e}", None, None, None

    daily = compute_degree_days(data, hdd_base, cdd_base, method)
    total_hdd = sum(d["hdd"] for d in daily)
    total_cdd = sum(d["cdd"] for d in daily)
    totals = f"**Total HDD:** {total_hdd:.3f}  \n**Total CDD:** {total_cdd:.3f}"

    table = create_daily_table(daily)
    plot = create_daily_plot(daily, hdd_base, cdd_base)

    csv_string = generate_csv(daily, total_hdd, total_cdd)
    tmpfile = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False)
    tmpfile.write(csv_string)
    tmpfile.close()
    return totals, plot, table, tmpfile.name

def clear_outputs():
    return "", None, None, None

# Example data
example_data = """15.0,22.0
10.5,18.0
-2.0,8.0
20.0,30.0
12.0,16.0
5.0,25.0"""

with gr.Blocks(title="Heating & Cooling Degree Day Calculator") as demo:
    gr.Markdown("# Heating & Cooling Degree Day Calculator")
    with gr.Row():
        with gr.Column(scale=1):
            temp_input = gr.Textbox(
                label="Daily Min and Max Temperatures (°C)",
                lines=8,
                placeholder="Enter one day per line: min,max",
                value=example_data,
            )
            hdd_base_input = gr.Number(label="HDD Base Temperature (°C)", value=18.3)
            cdd_base_input = gr.Number(label="CDD Base Temperature (°C)", value=18.3)
            method_dropdown = gr.Dropdown(
                choices=["Standard (average)", "Sinclair (max/min)"],
                label="Degree-day method",
                value="Standard (average)",
            )
            with gr.Row():
                compute_btn = gr.Button("Calculate", variant="primary")
                clear_btn = gr.Button("Clear")
        with gr.Column(scale=2):
            totals_output = gr.Markdown(label="Totals")
            plot_output = gr.Plot(label="Daily HDD / CDD")
            daily_table = gr.Dataframe(label="Daily Details")
            download = gr.File(label="Download CSV", file_types=[".csv"])

    compute_btn.click(
        fn=compute_and_display,
        inputs=[temp_input, hdd_base_input, cdd_base_input, method_dropdown],
        outputs=[totals_output, plot_output, daily_table, download],
    )
    clear_btn.click(
        fn=clear_outputs,
        inputs=[],
        outputs=[totals_output, plot_output, daily_table, download],
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
