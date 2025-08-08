# Results of pdfalto comparison (

- pdfalto-aba6cec: the pdfalto version from the xpdf branch (https://github.com/kermitt2/pdfalto/pull/210)
- pdfalto-4d060d3: first iteration of memory leaks fixing on the xpdf branch

```shell
 python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-aba6cec-linux-x86_64 --run2 ../output-pdfalto/pdfalto-4d060d-linux-x86_64
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 1000      | 984       | 1998                  | 1943            |
| Chars (spaces)    | 170       | 79        | 375                   | 498             |
| Tokens            | 170       | 79        | 376                   | 498             |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984           | biorxiv-10k-test-2000 | PMC_sample_1943     |
|-------------------|-----------|---------------------|-----------------------|---------------------|
| Chars (no spaces) | 0.0       | 0.0                 | -0.0035               | 0.0                 |
| Chars (spaces)    | -17.314   | -47.177845528455286 | -28.7355              | -15.942357179619146 |
| Tokens            | -17.314   | -47.177845528455286 | -28.732               | -15.942357179619146 |