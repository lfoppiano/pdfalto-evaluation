# Results of pdfalto comparison (Linux x86_64) 

- grobid: the pdfalto version shipped with grobid 
- pdfalto-0b01931: the pdfalto version from the master branch (https://github.com/kermitt2/pdfalto)
- pdfalto-aba6cec: the pdfalto version from the xpdf branch (https://github.com/kermitt2/pdfalto/pull/210)


# Results Grobid vs 0b01931 (master branch)

```shell
python scripts/text_comparison.py --run1 ../../pdfalto/output/pdfalto-0b01931/ --run2 ../../pdfalto/output/pdfalto-grobid
```

## Matching Documents

| Metric            | eLife_984 | PLOS_1000 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 609       | 773       | 1684                  | 1567            |
| Chars (spaces)    | 257       | 499       | 1074                  | 1017            |
| Tokens            | 294       | 508       | 1093                  | 1052            |

## Differences (Averages) run 1 - run 2

| Metric            | eLife_984          | PLOS_1000 | biorxiv-10k-test-2000 | PMC_sample_1943     |
|-------------------|--------------------|-----------|-----------------------|---------------------|
| Chars (no spaces) | 10.182926829268293 | 4.371     | 0.626                 | 1.743695316520844   |
| Chars (spaces)    | 11.748983739837398 | 4.927     | 0.6755                | 2.0087493566649512  |
| Tokens            | 1.5660569105691058 | 0.556     | 0.0495                | 0.26505404014410705 |

# Grobid vs pdfalto aba6cec (xpdf branch)

```shell
python scripts/text_comparison.py  --run1 ../../pdfalto/output/pdfalto-aba6cec/ --run2 ../../pdfalto/output/pdfalto-grobid/
```

## Matching Documents

| Metric            | eLife_984 | PLOS_1000 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 609       | 773       | 1677                  | 1566            |
| Chars (spaces)    | 164       | 386       | 794                   | 866             |
| Tokens            | 168       | 388       | 799                   | 876             |

## Differences (Averages) run 1 - run 2

| Metric            | eLife_984          | PLOS_1000 | biorxiv-10k-test-2000 | PMC_sample_1943    |
|-------------------|--------------------|-----------|-----------------------|--------------------|
| Chars (no spaces) | 10.182926829268293 | 4.371     | 1.005                 | 1.7519300051466804 |
| Chars (spaces)    | 19.86280487804878  | 7.336     | 8.112                 | 3.981986618630983  |
| Tokens            | 9.679878048780488  | 2.965     | 7.107                 | 2.2300566134843027 |

# pdfalto (master) vs pdfalto (xpdf branch)

```shell
 python scripts/text_comparison.py  --run1 ../../pdfalto/output/pdfalto-0b01931/ --run2 ../../pdfalto/output/pdfalto-aba6cec/
```

## Matching Documents

| Metric            | eLife_984 | PLOS_1000 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 984       | 1000      | 1981                  | 1941            |
| Chars (spaces)    | 261       | 485       | 881                   | 1062            |
| Tokens            | 261       | 485       | 883                   | 1062            |

## Differences (Averages)

| Metric            | eLife_984          | PLOS_1000 | biorxiv-10k-test-2000 | PMC_sample_1943       |
|-------------------|--------------------|-----------|-----------------------|-----------------------|
| Chars (no spaces) | 0.0                | 0.0       | -0.379                | -0.008234688625836336 |
| Chars (spaces)    | -8.113821138211382 | -2.409    | -7.4365               | -1.9732372619660319   |
| Tokens            | -8.113821138211382 | -2.409    | -7.0575               | -1.9650025733401957   |