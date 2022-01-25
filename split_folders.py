import splitfolders  # or import split_folders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio("D:\Educational Files\RUSL\Group Project\System\data\images\Sinhala_Braille_Letters_dataset_150150 - 5 char", output="D:\Educational Files\RUSL\Group Project\System\data\images\Sinhala_Braille_Letters_dataset_150150 - 5 char test train", seed=1337, ratio=(.9, .0, .1), group_prefix=None) # default values
