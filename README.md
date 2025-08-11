# Pump Operating Window Analysis Tool

<img width="1790" height="1190" alt="image" src="https://github.com/user-attachments/assets/020dd3a9-3488-4d19-b718-39d03e13181f" />
*Example output showing operating windows for different pump configurations*

## Overview
This Python tool analyzes and visualizes the operating characteristics of various pump configurations in a water treatment system. It helps engineers evaluate pump performance across different operating scenarios, including variable speed operation and parallel pump configurations.

## Key Fluid Mechanics Concepts

### Best Efficiency Point (BEP)
- The BEP represents the optimal operating condition where a pump operates at its highest efficiency
- Operating at or near BEP ensures:
  - Maximum energy efficiency
  - Minimal wear and tear
  - Reduced maintenance costs
  - Extended equipment lifespan

### Preferred Operating Range (POR)
- The range of flow rates where the pump operates within acceptable efficiency (typically 70-120% of BEP flow)
- POR-: Lower efficiency bound (typically 70% of BEP flow)
- POR+: Upper efficiency bound (typically 120% of BEP flow)
- Operating within this range ensures stable and efficient pump operation

### Variable Speed Operation
- Pumps can operate at different speeds (typically 70-100% of rated speed)
- Affinity laws govern the relationship between pump speed and performance:
  - Flow ∝ Speed (Q₁/Q₂ = N₁/N₂)
  - Head ∝ Speed² (H₁/H₂ = (N₁/N₂)²)
  - Power ∝ Speed³ (P₁/P₂ = (N₁/N₂)³)

## Code Requirements

### Dependencies
- Python 3.6+
- NumPy
- Matplotlib
- Pandas

### Installation
```bash
pip install numpy matplotlib pandas
```

## Code Structure

The script analyzes five pump configurations:
1. Small Pump Only
2. Large Pump Only
3. Small Pump + Large Pump in Parallel
4. Two Large Pumps in Parallel
5. Two Large Pumps + Small Pump in Parallel

The smaller pump should have a lower required flow rate and the large pump should operate at a higher flow rate.

### Key Components

#### 1. Data Input
- Pump performance curves at different speeds (70%, 80%, 90%, 100%)
- System curve data (min/max head)
- POR and BEP data for each configuration

#### 2. Main Functions
- `plot_scenario()`: Helper function to plot pump performance curves
- System curve plotting
- POR and BEP curve visualization

#### 3. Visualization
- Flow rate (MLD) on x-axis
- Head (m) on primary y-axis
- Color-coded pump configurations
- Line styles for different operating conditions

## Example Usage

```python
# Run the analysis
python operating-windows-for-pump-scenarios.py
```

## Interpreting the Results
- **Solid Lines**: Pump performance curves at different speeds
- **Dashed Lines**: POR- (lower efficiency bound)
- **Dash-Dot Lines**: POR+ (upper efficiency bound)
- **Dotted Lines**: BEP (Best Efficiency Point)
- **Thick Lines**: POR Window (preferred operating range)
- **Black Lines**: System curves (min/max)

## Expected Output

The script generates a plot showing:
1. Pump performance curves for all configurations at different speeds
2. System curves (min/max)
3. POR and BEP curves for each configuration
4. Operating windows for each pump configuration

## Customization

To modify the analysis:
1. Update the pump performance data in the respective arrays
2. Adjust the system curve parameters
3. Modify the plotting parameters as needed

## Best Practices
1. Always operate pumps within their POR when possible
2. Consider variable speed drives for systems with varying demand
3. Regularly monitor pump performance against the operating window
4. Schedule maintenance when operation deviates significantly from BEP

## Troubleshooting
- Ensure all required packages are installed
- Verify input data units (MLD for flow, meters for head)
- Check for any negative flow or head values in the input data
- Adjust figure size if legend overlaps with plots
