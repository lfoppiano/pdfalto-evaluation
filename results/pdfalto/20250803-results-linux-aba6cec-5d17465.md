# Results of pdfalto comparison (

- pdfalto-aba6cec: the pdfalto version from the xpdf branch (https://github.com/kermitt2/pdfalto/pull/210)
- pdfalto-5d16465: second iteration of memory leaks fixing on the xpdf branch - possible fixed some regressions

```shell
 python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-aba6cec-linux-x86_64 --run2 ../output-pdfalto/pdfalto-5d17465-linux-x86_64
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 1000      | 984       | 1998                  | 1941            |
| Chars (spaces)    | 374       | 255       | 836                   | 972             |
| Tokens            | 374       | 255       | 838                   | 971             |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984          | biorxiv-10k-test-2000 | PMC_sample_1943       |
|-------------------|-----------|--------------------|-----------------------|-----------------------|
| Chars (no spaces) | 0.0       | 0.0                | -0.0035               | -0.001029336078229542 |
| Chars (spaces)    | 5.391     | -3.671747967479675 | 1.345                 | 1.1065362840967576    |
| Tokens            | 5.391     | -3.671747967479675 | 1.3485                | 1.107565620174987     |