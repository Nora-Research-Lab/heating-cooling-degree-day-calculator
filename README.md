![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Heating & Cooling Degree Day Calculator
 
*For climate analysts and energy planners: enter daily high/low temperatures and a base temperature to instantly compute heating degree days (HDD) and cooling degree days (CDD) for a single day or a time series.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Climate & Earth Systems
 
The user provides (a) a comma-separated or line-separated list of daily minimum and maximum temperatures (°C), (b) a base temperature (°C, default 18.3°C for HDD, 18.3°C for CDD — but the user enters one base for both calculations or can choose separate bases), and (c) an optional toggle to use the Sinclair method (alternative averaging) instead of the standard method. The core logic: For each day, compute the average daily temperature = (Tmin + Tmax) / 2. For HDD: if average < base, HDD = base - average; else 0. For CDD: if average > base, CDD = average - base; else 0. Optionally, the user can choose a separate CDD base. The tool sums all daily values to give total HDD and CDD over the period. It also shows a simple bar chart of daily HDD and CDD values for visualization. The UI has: a large text area for input data (with example data pre-loaded), two number inputs for HDD base and CDD base, a checkbox for 'Use alternative averaging method (Sinclair method) — if checked, the average is computed as (Tmin + Tmax)/2 only if Tmax > base? Actually Sinclair method: HDD = (base - Tmax) if Tmax < base else 0; but often used for energy. Better to keep simple; allow user to choose 'Degree-day method' dropdown: Standard (average) or modified (Sinclair). Output: two numbers (total HDD, total CDD) plus a plot (bar chart using matplotlib) of daily contributions. Also a table of daily values can be displayed. No AI/ML component. The tool is purely arithmetic. A 'Download CSV' button exports the daily and total results.
 
## Run it
 
```bash
docker build -t heating-cooling-degree-day-calculator .
docker run -p 7860:7860 heating-cooling-degree-day-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-24.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
