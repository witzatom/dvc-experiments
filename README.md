# DVC experiments

## Problem statement
We have a external shared mount with data with the following properties:
  * it is intended to be append only, new files are added, but should not be modified
  * there are many files (images) that can be used for modelling
For example:
```
- data
  - 01
    - foo
      - 10m.jpg
      - 20m.jpg
  - 02
    - bar
      - 10m.jpg
      - 20m.jpg
      - 30m.jpg
    - baz
      - 20m.jpg
      - 30m.jpg
```
Our modelling tasks uses a subset of the files in the shared data folder.

We want to have more control over reproducibility of our modelling. However we dont want to rerun training if data unrelated to the modelling tasks were added to the external data share.

Further, we do not want to have the data from the external data share imported into the repository (`dvc import-url`), since that will cause duplication of large data. It would be acceptable if the files were linked from the shared data directory.

## DVC Example Setup
DVC does not support something like this right out of the box. You could possibly still use it by adding a couple extre steps at the start of the pipeline. This repository is an example of this.

The repository contains 2 dvc stages, `define_dataset` and `train_model`. It also assumes there is an external data folder at `../data`.

We have the `define_dataset` step as the first part of the pipeline. This step will look into the data folder, list the subset of files that we use for our experiment and produce a file that must be:
* immutable to changes when data folder changes in ways we dont care about - for example if a new file is added that we wont use in our model
* changes if any file that we care about in our modelling changes

This is achieved simply by listing all the files we care about into a file, along with their md5 hashes.

The following steps, in my example `train_model` need to also adhere to these requirements:
* never depend (dvc dep) on the external data folder
* always only use the files that are listed in the file produced by the 'define_dataset' step

## Example usage

Run the following to see which stages are dirty, you might want to rerun.
```
dvc status
```

Lets make it dirty, the `define_dataset` step only cares about files that end with `inmodel.jpg` as a simple example:
```
touch ../data/newfile
```

Now the `define_dataset` step will be dirty. You can rerun it with

```
dvc repro
```

But, because the dataset definition `dataset.txt` did not change, the command did not trigger rerunning the `train_model` step.
