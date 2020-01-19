from __future__ import print_function, division

import imgaug as ia
import imgaug.augmenters as iaa

from .utils import run_and_save_augseq


def main():
    chapter_augmenters_randaugment()


def chapter_augmenters_randaugment():
    fn_start = "collections/randaugment"

    aug = iaa.RandAugment(n=2, m=9)
    run_and_save_augseq(
        fn_start + "_standard_case.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(8*1)], cols=8, rows=1)

    aug = iaa.RandAugment(m=30)
    run_and_save_augseq(
        fn_start + "_strong_magnitude.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(8*1)], cols=8, rows=1)

    aug = iaa.RandAugment(m=(0, 9))
    run_and_save_augseq(
        fn_start + "_random_magnitude.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(8*1)], cols=8, rows=1)

    aug = iaa.RandAugment(n=(0, 3))
    run_and_save_augseq(
        fn_start + "_random_iterations.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(8*1)], cols=8, rows=1)


if __name__ == "__main__":
    main()
