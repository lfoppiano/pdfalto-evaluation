# Results of pdfalto comparison (aba6cec branch Linux x86_64 vs arm64)

- grobid: the pdfalto version shipped with grobid
- pdfalto-0b01931: the pdfalto version from the master branch (https://github.com/kermitt2/pdfalto)
- pdfalto-aba6cec: the pdfalto version from the xpdf branch (https://github.com/kermitt2/pdfalto/pull/210)

# LINUX ARM vs X86_64 aba6cec (xpdf branch)

```shell
python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-aba6cec-linux-arm64 --run2 ../output-pdfalto/pdfalto-aba6cec-linux-x86_64
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 1000      | 984       | 2000                  | 1943            |
| Chars (spaces)    | 642       | 425       | 1245                  | 1275            |
| Tokens            | 642       | 425       | 1245                  | 1275            |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984           | biorxiv-10k-test-2000 | PMC_sample_1943      |
|-------------------|-----------|---------------------|-----------------------|----------------------|
| Chars (no spaces) | 0.0       | 0.0                 | 0.0                   | 0.0                  |
| Chars (spaces)    | -0.023    | 0.43089430894308944 | 0.2885                | 0.032938754503345345 |
| Tokens            | -0.023    | 0.43089430894308944 | 0.2885                | 0.032938754503345345 |
