# Introduction
This is the repository for my bachelor thesis, conducted during my study in the Vrije Universiteit Amsterdam. This repository contains all necessary files, scripts have been used to run experiments and analyse data. However, this repository does not contain all written code to conduct this work since the code resides in another forked repository. You can refer to the code in this [Repository](https://github.com/cukibe123/opendc).

My bachelor thesis is about **Analysing The Impact of Temporal Shifting in Carbon Emissions of Datacenters**.

If you interested in reading my thesis, please refer to this [Overleaf](https://www.overleaf.com/read/gjcwqfbtrhch#04bcad).

## Repository Structure
```
vu_thesis_bachelor/
│
├── analysis/
├── carbon_traces/
├── experiments/
├── plots/
├── topologies/
├── visualisation/
├── workload_traces/

### Folder Description:
- analysis/: This folder contains all python scripts for data extraction from output files, produced by OpenDC.

- carbon_traces/: This folder contains all carbon traces in parquet and CSV formats. Parquet files are converted from CSV files,
provided by **Electricitymaps**.

- experiments/: This folder contains all experiment files under the JSON format. Each configuration for each scheduler is defined in this folder.

- plots/: This folder contains all plots, generated from the analysis/ folder. Some plots are displayed in the thesis already.

- topologies: This folder contains all topologies of ten countries. All countries use the same topology, provided by
the SURF Organization, however, each file uses a different carbon trace.

- visualisation/: This folder contains all python scripts used to generate the visualisation of schedulers.

- workload_traces/: This folder contains the workload trace used in this work, provided by the SURF Organisation.

```
## Repository for Code
For all implemented code inside OpenDC, you can refer to this [repository](https://github.com/cukibe123/opendc).

```
In the mentioned repository, the code is divided into four branches:
opendc/
│
├── master (default branch)
├── SingleThreshold_noTS
├── SingleThreshold
├── DoubleThreshold
├── WaitAWhile_2
├── WaitAWhile_3

### Branch Description:
- master: This is the default branch which is forked from the [OpenDC](https://github.com/atlarge-research/opendc) repository.

- SingleThreshold_noTS: This branch contains the default SingleThreshold scheduler.

- SingleThreshold: This branch contains the SingleThreshold scheduler, but it has Task Interruptions.

- DoubleThreshold: This branch contains the DoubleThreshold scheduler.

- WaitAWhile_2: This branch contains the Greenest-Window scheduler. 

- WaitAWhile_3: This branch contains the WaitAWhile scheduler.

You can switch between branches to use your desired scheduler with temporal shifting.
```

