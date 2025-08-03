# Grobid text extraction metrics

These metrics are provided for comparing the extracted output from pdfAlto with the Grobid structure. 
The Grobid structure passes a set of models in cascade and  
We create this metrics using the four corpora already used in the Grobid end to end evaluation benchmarks: PLOS_1000, PMC_sample_1943, eLife_984, and biorxiv-10k-test-2000.

We calculate difference between the pdfalto text and the grobid text using character and token counting comparison.

## Metrics

Metrics are calculated as follows: 
- The pdfalto text is extracted from pdfalto with a specific transformation schema illustrated [here](https://github.com/kermitt2/pdfalto/tree/master/schema).  
- The grobid text is recusively extracted with a python XML parser
- Both text are then stripped of their breaklines, whitespaces and they are assembled into two strings: 
  - a version with spaces separating each words and symbol, used for the number of tokens comparison 
  - a version without spaces, used for the character length comparison 
- Two metrics are calculated for each version (character, tokens): 
  - difference, computed as `length_pdfalto - lenght_grobid` which could be difference in characters or number of tokens 
  - the percentage of difference, computed as (1 - (lenght/grobid / length_pdfalto)) * 100
- The average values were produced by corpus and by process type

### Preliminary discussion
- Ligatures are preserved in pdfalto and converted into single characters by Grobid, therefore the Grobid character lenght might be larger for certain PDF documents
- Footers and headers decoration are normally removed by Grobid and they are more frequent in PMC_sample_1943, PLOS_1000 and eLife_984, while preprint in biorxiv-10k-test-2000 are generally plain documents without headers/footers
- Reference callout may be unwrapped by Grobid (`[9-15]` may become `[9][10][11][12][13][14][15]`) leading to larger character and token count
- In the Grobid `standard` output, affiliation are usually duplicated in the author information, so depending on the number of authors the text in the Grobid `standard` output may be larger
- Cover page, generally ignored by Grobid, may contain relevant amount of text for certain publishers
- Grobid apply de-hypenisation, leading to a smaller increase in tokens count

### 2025-03-08


### 2025-03-07

Diff: https://github.com/kermitt2/grobid/compare/8b9d113d665bc1bd64c3c38e4ca93a19a7426cb9...8ccde015d5b07f6a431826ab406d069222d8fd33

#### Character length comparison


| Process type                                  | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 |
|:----------------------------------------------|----------:|----------:|----------------------:|----------------:|
| standard                                      |     11.82 |      9.64 |                  9.26 |            6.45 |
| standard (paragraphs)                         |     11.81 |      9.63 |                  9.23 |            6.45 |
| standard + collectDiscardedText               |      7.57 |      2.72 |                  2.92 |            3.75 |
| standard + collectDiscardedText (paragraphs)  |      7.57 |      2.71 |                  2.89 |            3.75 |
| light                                         |     12.45 |      6.85 |                  8.83 |            8.51 |
| light (paragraphs)                            |     12.45 |      6.85 |                  8.80 |            8.51 |
| light + collectDiscardedText                  |      3.18 |      3.33 |                  4.07 |            2.13 |
| light + collectDiscardedText (paragraphs)     |      3.18 |      3.33 |                  4.04 |            2.13 |


#### Token length comparison

| Process type                                     | PLOS_1000 | eLife_984 |   biorxiv-10k-test-2000 | PMC_sample_1943 |
|:-------------------------------------------------|----------:|----------:|------------------------:|----------------:|
| standard                                         |      8.08 |      5.46 |                    7.44 |            3.63 |
| standard (paragraphs)                            |      8.07 |      5.45 |                    7.37 |            3.63 |
| standard + collectDiscardedText                  |      3.62 |     -2.36 |                    0.42 |            0.62 |
| standard + collectDiscardedText (paragraphs)     |      3.61 |     -2.37 |                    0.35 |            0.62 |
| light                                            |      8.93 |      2.74 |                    5.66 |            5.12 |
| light (paragraphs)                               |      8.93 |      2.74 |                    5.59 |            5.12 |
| light + collectDiscardedText                     |     -0.10 |     -0.51 |                    1.39 |            -0.7 |
| light + collectDiscardedText (paragraphs)        |     -0.10 |     -0.51 |                    1.32 |            -0.7 |                                

### 2025-02-01

#### Character length comparison

| Process type                                            | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 (token) |
|---------------------------------------------------------|-----------|-----------|-----------------------|-------------------------|
| standard                                                | 11.27     | 9.69      | 9.33                  | 6.27                    |
| standard (paragraphs)                                   | 11.84     | 9.72      | 9.48                  | 6.53                    |
| standard + collect_discarded_text                       | 10.16     | 9.35      | 9.07                  | 5.76                    |   
| standard + collect_discarded_text (paragraphs)          | 10.73     | 9.38      | 9.22                  | 6.02                    |   
| article/light-ref                                       | 12.46     | 6.85      | 8.84                  | 8.52                    |
| article/light-ref (paragraphs)                          | 12.46     | 6.85      | 8.79                  | 8.52                    |
| article/light-ref + collect_discarded_text              | 3.18      | 3.32      | 4.08                  | 2.17                    | 
| article/light-ref + collect_discarded_text (paragraphs) | 3.18      | 3.32      | 4.04                  | 2.17                    | 

- `Standard` vs `standard + collectDiscardedText`, there is an increase about 1% in recovered text
- `Standard` vs `article/light-ref`, there is a fluctuation in term of text which does not indicate any specific trend, article/light-ref may loose some information such as the abstract and other header related information that are not covered by the lightweight header model. 
- `article/light-ref` vs `article/light-ref + collectDiscardedText` difference with pdfalto are decreasing as the text that is discarded by the `article/light-ref` header model is now recovered 


#### Token length comparison

| Process type                                             | PLOS_1000 | eLife_984 | biorxiv-10k-test-2000 | PMC_sample_1943 (token) |
|----------------------------------------------------------|-----------|-----------|-----------------------|-------------------------|
| standard                                                 | 7.62      | 5.55      | 7.63                  | 3.58                    |           
| standard (paragraphs)                                    | 8.11      | 5.58      | 7.73                  | 3.75                    |           
| standard + collect_discarded_text                        | 6.56      | 5.22      | 7.38                  | 3.09                    |          
| standard + collect_discarded_text  (paragraphs)          | 7.05      | 5.24      | 7.48                  | 3.28                    |          
| article/light-ref                                        | 8.94      | 2.74      | 5.66                  | 5.12                    |
| article/light-ref (paragraphs)                           | 8.94      | 2.74      | 5.58                  | 5.13                    |
| article/light-ref + collect_discarded_text               | -0.09     | -0.51     | 1.39                  | -0.72                   |           
| article/light-ref + collect_discarded_text (paragraphs)  | -0.09     | -0.51     | 1.32                  | -0.72                   |           


- `Standard` vs `standard + collectDiscardedText`, there is an increase about 0.5-1% in recovered text
- `Standard` vs `article/light-ref`, there is a fluctuation in term of text which does not indicate any specific trend, article/light-ref may loose some information such as the abstract and other header related information that are not covered by the lightweight header model.
- `article/light-ref` vs `article/light-ref + collectDiscardedText` difference with pdfalto are decreasing as the text that is discarded by the `article/light-ref` header model is now recovered
- The negative numbers in the `article/light-ref + collect_discarded_text` can be due to dehypenisation applied by Grobid 


## Notes

- grobid.v3: 8b9d113d665bc1bd64c3c38e4ca93a19a7426cb9 (before fixing issue #1264 and bug with the figure not being reverted)
- grobid.v4: https://github.com/kermitt2/grobid/pull/1264/commits/8ccde015d5b07f6a431826ab406d069222d8fd33 (after fixing collection of discarded text from the graphics aggregation)
- grobid.v5: https://github.com/kermitt2/grobid/pull/1266
- grobid.v6: https://github.com/kermitt2/grobid/pull/1268 


Diff v3 to v4: https://github.com/kermitt2/grobid/compare/8b9d113d665bc1bd64c3c38e4ca93a19a7426cb9...8ccde015d5b07f6a431826ab406d069222d8fd33