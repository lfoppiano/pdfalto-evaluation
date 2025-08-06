# Results of pdfalto comparison (Linux x86_64)

- grobid: the pdfalto version shipped with grobid
- pdfalto-0b01931: the pdfalto version from the master branch (https://github.com/kermitt2/pdfalto)
- pdfalto-aba6cec: the pdfalto version from the xpdf branch (https://github.com/kermitt2/pdfalto/pull/210)

# Results Grobid vs 0b01931 (master branch)

```shell
python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-0b01931-mac-arm64 --run2 ../output-pdfalto/pdfalto-grobid
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 773       | 608       | 1684                  | 1566            |
| Chars (spaces)    | 238       | 56        | 379                   | 514             |
| Tokens            | 250       | 63        | 391                   | 540             |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984          | biorxiv-10k-test-2000 | PMC_sample_1943     |
|-------------------|-----------|--------------------|-----------------------|---------------------|
| Chars (no spaces) | 4.371     | 10.193285859613429 | 0.631815907953977     | 1.744593202883625   |
| Chars (spaces)    | -7.601    | -23.14242115971516 | -27.72336168084042    | -11.693614830072091 |
| Tokens            | -11.972   | -33.33570701932859 | -28.355177588794398   | -13.438208032955716 |

# Grobid vs pdfalto aba6cec (xpdf branch)

```shell
python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-aba6cec-mac-arm64 --run2 ../output-pdfalto/pdfalto-grobid
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 773       | 608       | 1676                  | 1565            |
| Chars (spaces)    | 238       | 56        | 379                   | 513             |
| Tokens            | 250       | 63        | 391                   | 540             |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984          | biorxiv-10k-test-2000 | PMC_sample_1943     |
|-------------------|-----------|--------------------|-----------------------|---------------------|
| Chars (no spaces) | 4.371     | 10.193285859613429 | 1.0130065032516258    | 1.752832131822863   |
| Chars (spaces)    | -7.601    | -23.14242115971516 | -27.25862931465733    | -11.685890834191555 |
| Tokens            | -11.972   | -33.33570701932859 | -28.271635817908955   | -13.438722966014419 |

# pdfalto (master) vs pdfalto (xpdf branch)

```shell
python scripts/text_comparison.py --run1 ../output-pdfalto/pdfalto-0b01931-mac-arm64 --run2 ../output-pdfalto/pdfalto-aba6cec-mac-arm64
```

## Matching Documents

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|-------------------|-----------|-----------|-----------------------|-----------------|
| Chars (no spaces) | 1001      | 983       | 1984                  | 1940            |
| Chars (spaces)    | 1001      | 983       | 1966                  | 1940            |
| Tokens            | 1001      | 983       | 1981                  | 1941            |

## Differences (Averages)

| Metric            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943        |
|-------------------|-----------|-----------|-----------------------|------------------------|
| Chars (no spaces) | 0.0       | 0.0       | 0.3808095952023988    | 0.008238928939237899   |
| Chars (spaces)    | 0.0       | 0.0       | 0.4642678660669665    | 0.007723995880535531   |
| Tokens            | 0.0       | 0.0       | 0.08345827086456771   | -0.0005149330587023687 |

