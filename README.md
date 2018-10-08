# Bioimaging
### William (image-recog)
    Adapted from [https://gogul09.github.io/software/flower-recognition-deep-learning]
     1. Download dataset from [https://mega.nz/#F!eRdWwC6Z!roFvMmDfxIR455wdX_Z8dA]
     2. Run extract_features.py
     3. Run train.py
     4. Run test.py to test on images in dataset/test folder
     # Known Issues
        1. Extract_Features.py causes a memory error. I am working on correcting this.

### Dax (googlenet-scratch)
    Inception-V3 using Keras
    Notes:
    1. Currently WIP and is incomplete. Using architecture based on [2] with features based on [1].
    2. Is missing localized response normalization used by [2]. Information about LRN can be found in [3]. However, the
    effectiveness of LRN is disputed, and in case studies of convolution networks such as VGGNet, LRN was omitted from the
    network [4].
    3. Keras implementation of Inception-v3 is trained on ImageNet, automatically making this implementation transfer
    learning.
    Papers:     [1] https://arxiv.org/pdf/1512.00567v1.pdf
                [2] https://bmcevolbiol.biomedcentral.com/articles/10.1186/s12862-017-1014-z
                [3] http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf
                [4] https://arxiv.org/pdf/1409.1556.pdf
    ~Dakila Ledesma
