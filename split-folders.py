import splitfolders
splitfolders.ratio("./dataset", output="output",
    seed=1337, ratio=(.8, .1, .1), group_prefix=None, move=False) # default value
