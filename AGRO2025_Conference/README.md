Climate Sensitivity of Maize Agroecosystems in Kikuyu Sub-County (1981–2022)
=============================================================================

This repository supports the AGRO 2025 Biennial Conference abstact submission titled:

"Climate change impact on maize agroecosystems: Linear climate sensitivities and scenario projections in Kikuyu Sub-County 1981–2022"  
Author: Jean-Marie Vianney Minani  
Institution: University of Nairobi, Faculty of Agriculture, Department of LARMAT  
Contact: jeanmarie.minani2@gmail.com | jeanmarie@students.uonbi.ac.ke  
ORCID: 0009-0005-7471-5089

Project Overview
----------------
This study explores how maize yield in Kikuyu Sub-County responds to climate variability using a data-driven simulation framework. It combines:

- FAO-reported national maize yield data (1981–2022)
- NASA POWER monthly climate data (T2M, PRECTOTCORR, GWETTOP)
- Linear regression models (OLS) to estimate climate sensitivities
- Scenario grid analysis to simulate yield under 35 climate futures

Analysis & Modeling
-------------------

- linear_predictions_1981_2022.py: Python script for fitting OLS models and generating climate sensitivity outputs
- panel.json: Configuration or metadata for scenario panel setup
- grid2.json: Scenario grid with projected yields under ΔT and ΔP combinations

Visualizations
--------------
- projected_yield_heatmap.png: Heatmap of yield response to temperature and precipitation shifts
- projected_yield_heatmap_gw.png: Heatmap including GWETTOP (soil wetness) as a third predictor
- scenario_grid_table.png: Tabular summary of 35 climate scenarios with yield values
- 1_1_plot_observed_vs_predicted.png: 1:1 plot comparing observed vs predicted maize yields
- Kikuyu_full_data_1981-2022.png: Visualization of full maize yield and climate dataset
- maize_yield_comparison.png: Comparative yield analysis across models or years
- maize_panel_gw.gif: Animated panel showing GWETTOP-based yield dynamics

Findings
--------
- Precipitation has a stronger influence on yield than temperature
- Most projected yield changes fall within RMSE bounds (±0.161 t/ha)
- Moderate warming (+1.5°C) with increased rainfall (+10%) may improve yield by ~2.3%
- The model explains ~23% of yield variability using climate variables

Conference Context
------------------
This work aligns with:
- Sub-theme 1: Innovative Crop Production Systems
- Sub-theme 4: Innovations for Dryland Ecosystems Management  
under the AGRO 2025 Biennial Conference hosted by the University of Nairobi.
