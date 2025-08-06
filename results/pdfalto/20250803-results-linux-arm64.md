# Results of pdfalto comparison (Linux x86_64)

- grobid: the pdfalto version shipped with grobid
- pdfalto-0b01931: the pdfalto version from the master branch (https://github.com/kermitt2/pdfalto)
- pdfalto-aba6cec: the pdfalto version from the xpdf branch (https://github.com/kermitt2/pdfalto/pull/210)

# Results Grobid vs 0b01931 (master branch)

```shell
python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-0b01931-linux-arm64 --run2 ../output-pdfalto/pdfalto-grobid
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 773       | 609       | 1685                  | 1567            |
| Chars (spaces)    | 485       | 262       | 1069                  | 1011            |
| Tokens            | 494       | 284       | 1082                  | 1033            |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984          | biorxiv-10k-test-2000 | PMC_sample_1943    |
|-------------------|-----------|--------------------|-----------------------|--------------------|
| Chars (no spaces) | 4.371     | 10.182926829268293 | 0.624                 | 1.743695316520844  |
| Chars (spaces)    | 5.007     | 11.927845528455284 | 0.3365                | 2.004632012352033  |
| Tokens            | 0.636     | 1.7449186991869918 | -0.2875               | 0.2609366958311889 |

# Grobid vs pdfalto aba6cec (xpdf branch)

```shell
python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-aba6cec-linux-arm64 --run2 ../output-pdfalto/pdfalto-grobid
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 773       | 609       | 1677                  | 1566            |
| Chars (spaces)    | 397       | 156       | 804                   | 871             |
| Tokens            | 403       | 163       | 808                   | 890             |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984          | biorxiv-10k-test-2000 | PMC_sample_1943    |
|-------------------|-----------|--------------------|-----------------------|--------------------|
| Chars (no spaces) | 4.371     | 10.182926829268293 | 1.005                 | 1.7519300051466804 |
| Chars (spaces)    | 7.313     | 20.29369918699187  | 8.4005                | 4.014925373134329  |
| Tokens            | 2.942     | 10.110772357723578 | 7.3955                | 2.262995367987648  |

# pdfalto (master) vs pdfalto (xpdf branch)

```shell
python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-0b01931-linux-arm64 --run2 ../output-pdfalto/pdfalto-aba6cec-linux-arm64
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 1000      | 984       | 1983                  | 1941            |
| Chars (spaces)    | 489       | 267       | 895                   | 1054            |
| Tokens            | 489       | 267       | 896                   | 1055            |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984          | biorxiv-10k-test-2000 | PMC_sample_1943       |
|-------------------|-----------|--------------------|-----------------------|-----------------------|
| Chars (no spaces) | 0.0       | 0.0                | -0.381                | -0.008234688625836336 |
| Chars (spaces)    | -2.306    | -8.365853658536585 | -8.064                | -2.0102933607822955   |
| Tokens            | -2.306    | -8.365853658536585 | -7.683                | -2.0020586721564593   |

Conclusion here: XPDF branch extracts more characters and tokens than the master branch.