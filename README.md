# environment
```
   conda env create -f environment.yml
```
python == 3.7
<br />deep-forest == 0.1.7
<br />deepchem == 2.7.1
<br />mol2vec == 0.2.2
<br />mordred == 1.2.0
<br />numpy == 1.21.6
<br />pandas == 1.3.5
<br />pubchempy == 1.0.4
<br />rdkit == 2023.3.2
<br />scikit-learn == 1.0.2

## usage

```
   $ conda activate hob
   $ python predict.py your_smiles.txt cutoff
   $ python predict.py your_smiles.txt method_name cutoff
```
## example
   With 50 as the cutoff, the default Mordred method predicts human oral bioavailability
```
   $ python predict.py smiles.txt 50
```
   With 20 as the cutoff, other method predicts human oral bioavailability，Take the circular method as an example
```
   $ python predict.py smiles.txt circular 20
```
